# MiniMax H3 人工评测数据集（58 条）

58 条用例 = **核心包 36**（T2VA / FL2VA / REF2VA 各 12）+ **困难包 22**（7 类困难样本）。
每条用例是一张自包含的提示单：中文执行版提示词、原文、音频要求、参考资产清单、
预期输出、公共／专项评测维度、硬失败规则、资产准备与改编说明。

| 模态 | 条数 | 输入形式 | 目录 |
| --- | --- | --- | --- |
| T2VA | 22 | 纯文本 | `core/t2va/`（12）+ `hard/`（10） |
| FL2VA | 12 | 文本 + 首帧 + 尾帧 | `core/fl2va/` |
| REF2VA | 24 | 文本 + 图／视频／音频参考 | `core/ref2va/`（12）+ `hard/`（12） |

- 全部用例索引：[`docs/index.md`](docs/index.md)
- 覆盖统计与目标值核对：[`docs/coverage.md`](docs/coverage.md)
- 来源与权利：[`docs/sources-and-rights.md`](docs/sources-and-rights.md)
- 跑测约定与评分口径：[`docs/how-to-run.md`](docs/how-to-run.md)

## 快速开始

```bash
cd diffusion_testcase/h3-eval-58
python assets/fetch_assets.py --dry-run     # 看要抓哪些参考资产
python assets/fetch_assets.py               # 抓取模型输入资产到 assets/files/
```

一条用例的用法：打开 `docs/index.md` 找到目标 `case_id` → 读该条的提示单 →
按「参考资产」表的编号顺序上传 → 用「评测维度」「硬失败规则」评分。

## 目录结构

```
h3-eval-58/
├── README.md                  # 本文件
├── cases.csv                  # 58 条索引（UTF-8 BOM，Excel 可直接打开）
├── cases.jsonl                # 完整字段 + 解析后的资产清单，供脚本消费
├── core/
│   ├── t2va/T2VA-01.md … T2VA-12.md
│   ├── fl2va/FL2VA-01.md … FL2VA-12.md
│   └── ref2va/REF2VA-01.md … REF2VA-12.md
├── hard/                      # HARD-{HS,FH,MP,PI,CM,ST,TX}-NN.md，共 22 条
├── assets/
│   ├── assets.csv             # 参考资产：编号 / 用途 / URL / 落地文件名
│   └── fetch_assets.py        # 抓取脚本（媒体不入库）
├── docs/
│   ├── index.md               # 58 条全量链接索引（生成）
│   ├── coverage.md            # 覆盖统计（生成）
│   ├── how-to-run.md
│   └── sources-and-rights.md
├── source/H3评测数据集_58条.xlsx   # 唯一数据源
└── tools/build_from_xlsx.py   # 由工作簿重新生成本包
```

## 数据源与再生成

`source/H3评测数据集_58条.xlsx` 是唯一数据源，Markdown／CSV／JSONL 都是它的渲染结果。
改动用例时改工作簿，然后：

```bash
python tools/build_from_xlsx.py
```

脚本只用标准库（办公机无 openpyxl，直接解析 xlsx 的 XML），会重写 `core/`、`hard/`、
`cases.csv`、`cases.jsonl`、`assets/assets.csv`、`docs/index.md`、`docs/coverage.md`。

## 重要约定

1. **中文执行版 ≠ 官方原文**：`source_prompt_original` 是原题或摘录，提示单里的
   「提示词（中文执行版）」是统一改写版，对外引用时必须区分。
2. **媒体不随包分发**：第三方参考媒体授权不明，仓库只存 URL 与角色说明；
   离线资产用 `fetch_assets.py` 自行抓取，`assets/files/` 已在 `.gitignore` 中。
3. **先硬失败后打分**：先按每条的硬失败规则筛掉无效样本，再评公共／专项维度与音轨。
4. **同参数同 Seed**：跨方案对比时模型、时长、画幅、采样步数与 seed 必须一致，
   建议每条 ≥3 个 seed 并同时报告最差样本。

## 权利提醒

含真实商标或可识别人物肖像的条目（REF2VA-11、HARD-TX-03、HARD-FH-01、REF2VA-03 等）
仅建议内部技术评测；对外发布生成结果或素材前需另行确认授权，详见
[`docs/sources-and-rights.md`](docs/sources-and-rights.md)。
