#!/usr/bin/env python3
"""Download the model-input assets listed in ``assets.csv``.

Binaries are intentionally not committed to this repository: reference images,
videos and audio come from third-party hosts with unclear redistribution terms,
so the pack ships URLs plus this downloader instead of copies.

Usage::

    python assets/fetch_assets.py                # all model-input assets
    python assets/fetch_assets.py --case REF2VA-01 FL2VA-05
    python assets/fetch_assets.py --dry-run      # only print the plan
    python assets/fetch_assets.py --include-derived
                                                 # also fetch the public output
                                                 # videos used as tail frames

Files land in ``assets/files/`` with the deterministic names from
``assets.csv``. Existing files are skipped unless ``--force`` is given.
"""

from __future__ import annotations

import argparse
import csv
import sys
import urllib.request
from pathlib import Path

ASSET_DIR = Path(__file__).resolve().parent
CSV_PATH = ASSET_DIR / "assets.csv"
FILES_DIR = ASSET_DIR / "files"
USER_AGENT = "h3-eval-58-fetch/1.0 (+https://github.com/sirius2alpha/diffusion-testcase)"


def load_rows(cases: set[str], include_derived: bool) -> list[dict[str, str]]:
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    selected = []
    for row in rows:
        usage = row["usage"]
        wanted = usage.startswith("input") or (
            include_derived and usage == "derived_tail_frame_source"
        )
        if not wanted:
            continue
        if cases and row["case_id"] not in cases:
            continue
        selected.append(row)
    return selected


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--case", nargs="*", default=[], metavar="ID",
                        help="only fetch these case ids")
    parser.add_argument("--dry-run", action="store_true", help="print, do not download")
    parser.add_argument("--force", action="store_true", help="re-download existing files")
    parser.add_argument("--include-derived", action="store_true",
                        help="also fetch the public output videos used as tail frames")
    args = parser.parse_args(argv)

    rows = load_rows(set(args.case), args.include_derived)
    if not rows:
        print("nothing to do")
        return 0

    FILES_DIR.mkdir(parents=True, exist_ok=True)
    failures = []
    for row in rows:
        target = FILES_DIR / row["file"]
        label = f"{row['case_id']} {row['slot'] or '-'} {row['usage']}"
        if target.exists() and not args.force:
            print(f"skip   {label} -> {target.name}")
            continue
        if args.dry_run:
            print(f"plan   {label} -> {target.name}  {row['url']}")
            continue
        request = urllib.request.Request(row["url"], headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                payload = response.read()
        except Exception as error:  # noqa: BLE001 - report and continue
            failures.append((label, str(error)))
            print(f"FAIL   {label}: {error}")
            continue
        target.write_bytes(payload)
        print(f"ok     {label} -> {target.name} ({len(payload)} bytes)")

    if failures:
        print(f"\n{len(failures)} asset(s) failed:")
        for label, error in failures:
            print(f"  - {label}: {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
