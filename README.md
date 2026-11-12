# Diffusion Test Cases

Small, reusable test-case packs for joint audio-video diffusion models
(MiniMax H3 today).

| Pack | Contents | Location |
| --- | --- | --- |
| **H3 eval-58** | 58 case pack: core 36 (T2VA / FL2VA / REF2VA, 12 each) + hard 22 across seven difficulty categories. Chinese execution prompts with source text, media requirements, expected output, scoring dimensions and hard-fail rules for every case. | [`diffusion_testcase/h3-eval-58/`](diffusion_testcase/h3-eval-58/README.md) |
| **Ref2VA pilot** | The original five Ref2VA pilot cases (dog identity / scene separation / motion transfer / sound conditioning / multimodal composition) with CC-licensed media included. Kept standalone and unchanged. | [`diffusion_testcase/ref2va-pilot/`](diffusion_testcase/ref2va-pilot/README.md) |

## H3 eval-58 at a glance

- 58 cases, one prompt sheet per case: `core/{t2va,fl2va,ref2va}/` + `hard/`
- Machine-readable index: `cases.csv` (Excel-friendly) and `cases.jsonl` (full fields)
- 92 reference-asset URLs across 36 cases in `assets/assets.csv`, fetched on demand by
  `assets/fetch_assets.py`; third-party media is not redistributed here
- Generated from a single source workbook (`source/H3评测数据集_58条.xlsx`) by
  `tools/build_from_xlsx.py`, so the workbook stays the source of truth

Start here: [pack README](diffusion_testcase/h3-eval-58/README.md) ·
[case index](diffusion_testcase/h3-eval-58/docs/index.md) ·
[how to run](diffusion_testcase/h3-eval-58/docs/how-to-run.md) ·
[coverage](diffusion_testcase/h3-eval-58/docs/coverage.md) ·
[sources and rights](diffusion_testcase/h3-eval-58/docs/sources-and-rights.md)

## Ref2VA pilot

Five MiniMax H3 Ref2VA cases covering image identity, subject/scene separation,
image-plus-video motion, image-plus-audio, and multimodal reference composition,
with prompts, assets, attribution and license details. See the
[Ref2VA pilot README](diffusion_testcase/ref2va-pilot/README.md).

## Notes

- Rights: public accessibility is not redistribution permission. Several entries
  reference third-party media or real trademarks; see
  [sources and rights](diffusion_testcase/h3-eval-58/docs/sources-and-rights.md)
  before publishing any result.
- The two packs are independent: `ref2va-pilot` is frozen, `h3-eval-58` is the
  maintained benchmark.
