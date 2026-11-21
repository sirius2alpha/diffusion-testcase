#!/usr/bin/env python3
"""Regenerate the H3 eval-58 case pack from the source workbook.

Reads ``source/H3评测数据集_58条.xlsx`` (sheet ``全部测试用例``) and writes:

* ``cases.jsonl``          full record per case, machine readable
* ``cases.csv``            58-row index, UTF-8 with BOM so Excel opens it cleanly
* ``assets/assets.csv``    every reference asset URL with its slot and usage
* ``core/<modality>/*.md`` one prompt sheet per core case
* ``hard/*.md``            one prompt sheet per hard case
* ``docs/coverage.md``     coverage statistics computed from the data

The workbook is the single source of truth for prompts; the generated
Markdown is only a rendering. Re-run this script after editing the workbook::

    python tools/build_from_xlsx.py

Only the standard library is used on purpose: the office workstation has no
openpyxl available.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
import zipfile
from collections import Counter, OrderedDict
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

PACK_ROOT = Path(__file__).resolve().parents[1]
WORKBOOK = PACK_ROOT / "source" / "H3评测数据集_58条.xlsx"
CASE_SHEET = "全部测试用例"

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"

# Workbook column -> record key, in source order.
COLUMNS = [
    ("A", "case_id"),
    ("B", "modality"),
    ("C", "input_modality"),
    ("D", "subtask"),
    ("E", "business_scenario"),
    ("F", "source_prompt_original"),
    ("G", "prompt_zh"),
    ("H", "audio_requirements"),
    ("I", "reference_assets"),
    ("J", "asset_roles"),
    ("K", "source_name"),
    ("L", "source_url"),
    ("M", "source_asset_url"),
    ("N", "reuse_type"),
    ("O", "rights_status"),
    ("P", "difficulty"),
    ("Q", "duration_seconds"),
    ("R", "aspect_ratio"),
    ("S", "expected_output"),
    ("T", "common_eval_dimensions"),
    ("U", "modality_eval_dimensions"),
    ("V", "hard_fail_rules"),
    ("W", "asset_preparation"),
    ("X", "adaptation_notes"),
    ("Y", "package"),
    ("Z", "difficulty_category"),
]

ASSET_LINE = re.compile(r"^(?:(?P<label>[^：:]{1,60})[：:])\s*(?P<url>https?://\S+)\s*$")
SLOT = re.compile(r"(Input\s+Video|Video|Image|Audio)\s*(\d+)?")
EXT_KIND = {
    ".webp": "image",
    ".png": "image",
    ".jpg": "image",
    ".jpeg": "image",
    ".mp4": "video",
    ".webm": "video",
    ".mp3": "audio",
    ".wav": "audio",
    ".ogg": "audio",
}


# --------------------------------------------------------------------------- #
# workbook reading
# --------------------------------------------------------------------------- #
def _cell_text(cell: ET.Element) -> str:
    inline = cell.find(NS + "is")
    if inline is not None:
        return "".join(node.text or "" for node in inline.iter(NS + "t"))
    value = cell.find(NS + "v")
    return value.text if value is not None and value.text else ""


def read_sheet(path: Path, sheet_name: str) -> list[dict[str, str]]:
    """Return the sheet rows as dicts keyed by title from the header row."""
    with zipfile.ZipFile(path) as book:
        workbook = ET.fromstring(book.read("xl/workbook.xml"))
        rels = ET.fromstring(book.read("xl/_rels/workbook.xml.rels"))
        targets = {rel.get("Id"): rel.get("Target") for rel in rels}
        rel_ns = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
        target = None
        for sheet in workbook.iter(NS + "sheet"):
            if sheet.get("name") == sheet_name:
                target = targets[sheet.get(rel_ns)]
                break
        if target is None:
            raise SystemExit(f"sheet {sheet_name!r} not found in {path}")
        xml_path = target.lstrip("/")
        sheet_root = ET.fromstring(book.read(xml_path))

    raw_rows: list[dict[str, str]] = []
    for row in sheet_root.iter(NS + "row"):
        row_cells = {}
        for cell in row:
            ref = cell.get("r") or ""
            row_cells[re.sub(r"\d", "", ref)] = _cell_text(cell)
        raw_rows.append(row_cells)

    header = {col: name for col, name in
              ((col, raw_rows[0].get(col, "")) for col, _ in COLUMNS) if name}
    records = []
    for row_cells in raw_rows[1:]:
        if not any(row_cells.values()):
            continue
        record = {}
        for col, key in COLUMNS:
            record[key] = (row_cells.get(col) or "").strip()
        records.append(record)
    del header
    return records


# --------------------------------------------------------------------------- #
# asset parsing
# --------------------------------------------------------------------------- #
def parse_assets(record: dict[str, str]) -> list[dict[str, str]]:
    """Split the free-text asset cell into one entry per URL."""
    cell = record["reference_assets"]
    if cell in ("", "无", "无。"):
        return []

    assets: list[dict[str, str]] = []
    for line in cell.splitlines():
        line = line.strip()
        if not line:
            continue
        match = ASSET_LINE.match(line)
        if match:
            label, url = (match.group("label") or "").strip(), match.group("url")
        elif line.startswith("http"):
            label, url = "", line.split()[0]
        else:
            continue
        assets.append({"label": label, "url": url})

    for index, asset in enumerate(assets, start=1):
        label = asset["label"]
        slot_match = SLOT.search(label)
        slot = ""
        if slot_match:
            slot = slot_match.group(1).replace("  ", " ")
            if slot_match.group(2):
                slot = f"{slot} {slot_match.group(2)}"
        asset["slot"] = slot
        asset["usage"] = classify_usage(label, slot)
        asset["kind"] = EXT_KIND.get(
            Path(urlparse(asset["url"]).path).suffix.lower(), "other"
        )

    # Some rows only say "首帧：<url>" / "尾帧：<url>"; number those slots
    # by kind so the upload order is still explicit.
    seen: Counter = Counter()
    for asset in assets:
        if asset["slot"] or not asset["usage"].startswith("input"):
            continue
        seen[asset["kind"]] += 1
        prefix = {"image": "Image", "video": "Video", "audio": "Audio"}.get(
            asset["kind"], "Asset"
        )
        asset["slot"] = f"{prefix} {seen[asset['kind']]}"

    for index, asset in enumerate(assets, start=1):
        digest = hashlib.sha1(asset["url"].encode("utf-8")).hexdigest()[:8]
        suffix = Path(urlparse(asset["url"]).path).suffix.lower() or ".bin"
        stem = (asset["slot"] or f"asset{index}").replace(" ", "_").lower()
        asset.update(
            {
                "ordinal": str(index),
                "suffix": suffix,
                "file": f"{record['case_id']}_{stem}_{digest}{suffix}",
            }
        )
    return assets


def classify_usage(label: str, slot: str) -> str:
    if "提取末帧" in label:
        return "derived_tail_frame_source"
    if "仅作参考" in label or "不进入模型输入" in label:
        return "reference_output_not_input"
    if "尾帧" in slot or "尾帧" in label:
        return "input_last_frame"
    if "首帧" in slot or "首帧" in label:
        return "input_first_frame"
    if "Video" in slot:
        return "input_video"
    if "Audio" in slot:
        return "input_audio"
    if "Image" in slot:
        return "input_image"
    return "input_other"


# --------------------------------------------------------------------------- #
# markdown rendering
# --------------------------------------------------------------------------- #
def md_cell(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", "<br>").strip()


def case_dir(record: dict[str, str]) -> Path:
    if record["package"] == "困难包":
        return PACK_ROOT / "hard"
    return PACK_ROOT / "core" / record["modality"].lower()


def render_case(record: dict[str, str], assets: list[dict[str, str]]) -> str:
    front = OrderedDict(
        [
            ("case_id", record["case_id"]),
            ("package", record["package"]),
            ("modality", record["modality"]),
            ("input_modality", record["input_modality"]),
            ("subtask", record["subtask"]),
            ("business_scenario", record["business_scenario"]),
            ("difficulty", record["difficulty"]),
            ("difficulty_category", record["difficulty_category"] or "-"),
            ("duration_seconds", record["duration_seconds"]),
            ("aspect_ratio", record["aspect_ratio"]),
            ("source", record["source_name"]),
            ("reuse_type", record["reuse_type"]),
        ]
    )
    out = ["---"]
    for key, value in front.items():
        out.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    out += ["---", ""]
    out.append(f"# {record['case_id']} · {record['subtask']}")
    out.append("")
    out.append(
        f"{record['package']} / {record['modality']} / {record['input_modality']} · "
        f"{record['duration_seconds']} 秒 · {record['aspect_ratio']} · "
        f"难度 {record['difficulty']}/5"
        + (f" · 困难类别：{record['difficulty_category']}"
           if record["difficulty_category"] else "")
    )
    out.append("")

    out += ["## 提示词（中文执行版）", "", "```text", record["prompt_zh"], "```", ""]

    out += ["## 音频要求", "", record["audio_requirements"], ""]

    out.append("## 参考资产")
    out.append("")
    if record["asset_roles"] and record["asset_roles"] != "无":
        out.append(record["asset_roles"])
        out.append("")
    if assets:
        out.append("| # | 编号 | 用途 | 类型 | URL |")
        out.append("| --- | --- | --- | --- | --- |")
        for asset in assets:
            out.append(
                f"| {asset['ordinal']} | {md_cell(asset['slot']) or '-'} | "
                f"{USAGE_LABEL[asset['usage']]} | {asset['kind']} | <{asset['url']}> |"
            )
        out.append("")
        up = "../" * (len(doc_relpath(record).split("/")) - 1)
        derived = [a for a in assets if a["usage"] == "derived_tail_frame_source"]
        if derived:
            out.append(
                "尾帧需从上方第 "
                + "、".join(a["ordinal"] for a in derived)
                + " 条官方输出视频提取最后一帧得到（该视频本身不作为模型输入）；"
                + f"取帧命令见 [`{up}docs/how-to-run.md`]({up}docs/how-to-run.md)。"
            )
            out.append("")
        out.append(
            f"本地文件名见 [`{up}assets/assets.csv`]({up}assets/assets.csv)；"
            f"在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。"
        )
    else:
        out.append("无需输入资产（纯文本题）。")
    out.append("")

    out += ["## 预期输出", "", record["expected_output"], ""]

    out += ["## 评测维度", ""]
    out.append(f"- 公共维度：{record['common_eval_dimensions']}")
    out.append(f"- 专项维度：{record['modality_eval_dimensions']}")
    out.append("")

    out += ["## 硬失败规则", ""]
    for rule in split_rules(record["hard_fail_rules"]):
        out.append(f"- {rule}")
    out.append("")

    out += ["## 资产准备", "", record["asset_preparation"], ""]
    out += ["## 改编说明", "", record["adaptation_notes"], ""]

    out += ["## 来源与权利", ""]
    out.append(f"- 来源：{record['source_name']}")
    if record["source_url"]:
        out.append(f"- 来源页面：<{record['source_url']}>")
    out.append(f"- 复用方式：`{record['reuse_type']}`")
    out.append(f"- 权利状态：{record['rights_status']}")
    out.append("")

    out += ["## 原文（source_prompt_original，仅供对照）", "", "```text",
            record["source_prompt_original"], "```", ""]
    return "\n".join(out)


def split_rules(text: str) -> list[str]:
    parts = [p.strip().rstrip("。") for p in re.split(r"[；;]\s*", text) if p.strip()]
    return parts or [text]


USAGE_LABEL = {
    "input_image": "模型输入·图片",
    "input_first_frame": "模型输入·首帧",
    "input_last_frame": "模型输入·尾帧",
    "input_video": "模型输入·视频",
    "input_audio": "模型输入·音频",
    "input_other": "模型输入",
    "derived_tail_frame_source": "派生尾帧的来源输出（不直接输入）",
    "reference_output_not_input": "官方示例输出（仅参考，不输入）",
}


# --------------------------------------------------------------------------- #
# index / coverage
# --------------------------------------------------------------------------- #
def doc_relpath(record: dict[str, str]) -> str:
    return case_dir(record).relative_to(PACK_ROOT).as_posix() + f"/{record['case_id']}.md"


def write_cases_csv(records, assets_by_case) -> None:
    fields = [
        "case_id", "package", "modality", "input_modality", "difficulty",
        "difficulty_category", "subtask", "business_scenario",
        "duration_seconds", "aspect_ratio", "doc", "input_asset_count",
        "needs_derived_tail_frame", "input_asset_urls", "source_name", "source_url",
        "reuse_type", "rights_status", "expected_output", "hard_fail_rules",
    ]
    path = PACK_ROOT / "cases.csv"
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            assets = assets_by_case[record["case_id"]]
            inputs = [a for a in assets if a["usage"].startswith("input")]
            writer.writerow(
                {
                    "case_id": record["case_id"],
                    "package": record["package"],
                    "modality": record["modality"],
                    "input_modality": record["input_modality"],
                    "difficulty": record["difficulty"],
                    "difficulty_category": record["difficulty_category"],
                    "subtask": record["subtask"],
                    "business_scenario": record["business_scenario"],
                    "duration_seconds": record["duration_seconds"],
                    "aspect_ratio": record["aspect_ratio"],
                    "doc": doc_relpath(record),
                    "input_asset_count": len(inputs),
                    "needs_derived_tail_frame": "yes" if any(
                        a["usage"] == "derived_tail_frame_source" for a in assets
                    ) else "no",
                    "input_asset_urls": " ".join(a["url"] for a in inputs),
                    "source_name": record["source_name"],
                    "source_url": record["source_url"],
                    "reuse_type": record["reuse_type"],
                    "rights_status": record["rights_status"],
                    "expected_output": record["expected_output"],
                    "hard_fail_rules": record["hard_fail_rules"],
                }
            )


def write_assets_csv(assets_by_case) -> None:
    path = PACK_ROOT / "assets" / "assets.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["case_id", "ordinal", "slot", "usage", "kind", "label", "url", "file"]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for case_id, assets in assets_by_case.items():
            for asset in assets:
                writer.writerow({"case_id": case_id, **{k: asset[k] for k in fields[1:]}})


def write_jsonl(records, assets_by_case) -> None:
    path = PACK_ROOT / "cases.jsonl"
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            payload = dict(record)
            payload["doc"] = doc_relpath(record)
            payload["assets"] = assets_by_case[record["case_id"]]
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")


def write_coverage(records, assets_by_case) -> None:
    def table(counter: Counter, total: int, header: str) -> list[str]:
        lines = [f"| {header} | 用例数 | 占比 |", "| --- | --- | --- |"]
        for name, count in counter.most_common():
            lines.append(f"| {name} | {count} | {count / total:.0%} |")
        lines.append(f"| **合计** | **{total}** | 100% |")
        return lines

    total = len(records)
    packages = Counter(r["package"] for r in records)
    modalities = Counter(r["modality"] for r in records)
    categories = Counter(r["difficulty_category"] for r in records
                         if r["difficulty_category"])
    durations = Counter(f"{r['duration_seconds']} 秒" for r in records)
    ratios = Counter(r["aspect_ratio"] for r in records)
    difficulty = Counter(r["difficulty"] for r in records)
    with_assets = [r for r in records if assets_by_case[r["case_id"]]]
    input_assets = sum(
        len([a for a in assets_by_case[r["case_id"]] if a["usage"].startswith("input")])
        for r in records
    )

    out = ["# 覆盖统计", "",
           "由 `tools/build_from_xlsx.py` 从源工作簿自动统计，修改用例后请重新生成。", "",
           f"总用例数：**{total}**（唯一 case_id 数 {len({r['case_id'] for r in records})}）", ""]
    out += ["## 用例包", ""] + table(packages, total, "用例包") + [""]
    out += ["## 模态", ""] + table(modalities, total, "模态") + [""]
    out += ["## 困难类别（仅困难包）", ""] + table(categories, sum(categories.values()),
                                                   "困难类别") + [""]
    out += ["## 难度分值", ""] + table(difficulty, total, "难度") + [""]
    out += ["## 时长", ""] + table(durations, total, "时长") + [""]
    out += ["## 画幅", ""] + table(ratios, total, "画幅") + [""]
    out += ["## 参考资产", "",
            f"- 含参考资产的用例：{len(with_assets)} / {total}",
            f"- 模型输入资产条目合计：{input_assets}",
            "- 逐条清单见 `assets/assets.csv`", "",
            "## 目标值核对", "",
            "| 项目 | 目标 | 实际 | 达标 |", "| --- | --- | --- | --- |",
            f"| T2VA | 22 | {modalities.get('T2VA', 0)} | "
            f"{'是' if modalities.get('T2VA') == 22 else '否'} |",
            f"| FL2VA | 12 | {modalities.get('FL2VA', 0)} | "
            f"{'是' if modalities.get('FL2VA') == 12 else '否'} |",
            f"| REF2VA | 24 | {modalities.get('REF2VA', 0)} | "
            f"{'是' if modalities.get('REF2VA') == 24 else '否'} |",
            f"| 核心包 | 36 | {packages.get('核心包', 0)} | "
            f"{'是' if packages.get('核心包') == 36 else '否'} |",
            f"| 困难包 | 22 | {packages.get('困难包', 0)} | "
            f"{'是' if packages.get('困难包') == 22 else '否'} |",
            ""]
    (PACK_ROOT / "docs").mkdir(parents=True, exist_ok=True)
    (PACK_ROOT / "docs" / "coverage.md").write_text("\n".join(out), encoding="utf-8")


def write_index(records, assets_by_case) -> None:
    """Full-link index of all cases, grouped for browsing on GitHub."""
    groups = [
        ("核心包 · T2VA", [r for r in records
                          if r["package"] != "困难包" and r["modality"] == "T2VA"]),
        ("核心包 · FL2VA", [r for r in records
                           if r["package"] != "困难包" and r["modality"] == "FL2VA"]),
        ("核心包 · REF2VA", [r for r in records
                            if r["package"] != "困难包" and r["modality"] == "REF2VA"]),
    ]
    hard = [r for r in records if r["package"] == "困难包"]
    for category in OrderedDict.fromkeys(r["difficulty_category"] for r in hard):
        groups.append((f"困难包 · {category}",
                       [r for r in hard if r["difficulty_category"] == category]))

    out = ["# 用例索引（58 条）", "",
           "由 `tools/build_from_xlsx.py` 生成。点击 case_id 进入该条提示单。", ""]
    for title, items in groups:
        if not items:
            continue
        out += [f"## {title}（{len(items)} 条）", "",
                "| case_id | 输入 | 子任务 | 业务场景 | 难度 | 时长 | 画幅 | 资产 |",
                "| --- | --- | --- | --- | --- | --- | --- | --- |"]
        for r in items:
            inputs = [a for a in assets_by_case[r["case_id"]] if a["usage"].startswith("input")]
            out.append(
                f"| [{r['case_id']}](../{doc_relpath(r)}) | {md_cell(r['input_modality'])} | "
                f"{md_cell(r['subtask'])} | {md_cell(r['business_scenario'])} | "
                f"{r['difficulty']}/5 | {r['duration_seconds']}s | {r['aspect_ratio']} | "
                f"{len(inputs)} |"
            )
        out.append("")
    (PACK_ROOT / "docs" / "index.md").write_text("\n".join(out), encoding="utf-8")


# --------------------------------------------------------------------------- #
def main() -> int:
    if not WORKBOOK.exists():
        raise SystemExit(f"workbook not found: {WORKBOOK}")
    records = read_sheet(WORKBOOK, CASE_SHEET)
    if not records:
        raise SystemExit("no records parsed from workbook")
    assets_by_case = {r["case_id"]: parse_assets(r) for r in records}

    for record in records:
        target = case_dir(record) / f"{record['case_id']}.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render_case(record, assets_by_case[record["case_id"]]),
                          encoding="utf-8")

    write_cases_csv(records, assets_by_case)
    write_assets_csv(assets_by_case)
    write_jsonl(records, assets_by_case)
    write_coverage(records, assets_by_case)
    write_index(records, assets_by_case)

    counts = Counter(r["package"] for r in records)
    print(f"cases: {len(records)} ({dict(counts)})")
    print(f"assets: {sum(len(v) for v in assets_by_case.values())} "
          f"across {sum(1 for v in assets_by_case.values() if v)} cases")
    print(f"written to {PACK_ROOT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
