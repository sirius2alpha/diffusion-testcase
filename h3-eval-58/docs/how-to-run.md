# 使用说明

## 目录

| 路径 | 内容 |
| --- | --- |
| `cases.csv` | 58 条索引（UTF-8 BOM，Excel 可直接打开）：元数据 + 文档路径 + 输入资产 URL |
| `cases.jsonl` | 每条用例的完整字段，含解析后的资产清单，供脚本直接消费 |
| `core/t2va/`、`core/fl2va/`、`core/ref2va/` | 核心包 36 条，一条一个 Markdown 提示单 |
| `hard/` | 困难包 22 条，文件名前缀带困难类别 |
| `assets/assets.csv` | 参考资产清单：编号（Image 1／Video 1／Audio 1…）、用途、URL、落地文件名 |
| `assets/fetch_assets.py` | 按清单抓取模型输入资产到 `assets/files/`（不入库） |
| `docs/coverage.md` | 覆盖统计与目标值核对，由脚本生成 |
| `docs/sources-and-rights.md` | 来源与权利说明 |
| `docs/how-to-run.md` | 本文件，跑测约定与评分口径 |
| `source/H3评测数据集_58条.xlsx` | 源工作簿（唯一数据源，含使用说明／覆盖统计／来源与权利三张附表） |
| `tools/build_from_xlsx.py` | 由源工作簿重新生成本包全部 Markdown／CSV／JSONL |

## 修改用例的正确姿势

1. 改 `source/H3评测数据集_58条.xlsx` 的「全部测试用例」表（不要直接改生成的 Markdown）。
2. 在包根目录运行：

   ```bash
   python tools/build_from_xlsx.py
   ```

3. 提交时把工作簿与重新生成的 Markdown／CSV／JSONL 一起提交，保证两者始终一致。

脚本只依赖 Python 标准库（办公机没有 openpyxl，因此直接解析 xlsx 的 XML）。

## 跑测约定

- **同参数对比**：同一组对比（不同 PR、不同量化、不同后端）必须使用同一
  `duration_seconds`、`aspect_ratio`、模型／checkpoint、采样步数与 seed。
- **资产编号即上传顺序**：`Image 1`／`Video 1`／`Audio 1` 的编号必须与
  `assets/assets.csv` 的顺序一致；顺序错位会把「参考角色绑定」类用例变成无效样本。
- **总时长上限**：H3 单次生成有时长上限，包内用例最长 15 秒，超出时按条目的
  改编说明压缩时间轴，不要拼接多段再评分。
- **硬失败优先**：先按每条的「硬失败规则」判定 `hard fail`，通过后再打分；
  硬失败样本不参与均值统计，但要单独列出。
- **多次采样**：质量比较建议每条 ≥3 个 seed，报告均值与最差样本。

## 评分口径

| 层级 | 维度 | 说明 |
| --- | --- | --- |
| 公共维度 | 语义一致性、主体与背景时序一致性、运动自然度、画面质量、音画同步、音频清晰度、指令遵循 | 每条用例都评 |
| 专项维度 | 见每条用例的「评测维度」 | 该条用例的核心考点，例如替换完整度、唇形同步、UI 文字逐字 |
| 音轨 | 见每条用例的「音频要求」 | 单独打分，不并入画面分 |

文字类用例（`HARD-TX-*`、含 UI 文案的 `REF2VA-*`）必须先人工转录目标文字清单，
再逐字对照生成结果；错拼、漏字、多字、乱码一律 `hard fail`。

## 参考资产抓取

```bash
cd diffusion_testcase/h3-eval-58
python assets/fetch_assets.py --dry-run          # 先看计划
python assets/fetch_assets.py                     # 抓模型输入资产
python assets/fetch_assets.py --case REF2VA-01    # 只抓某条
python assets/fetch_assets.py --include-derived   # 需要派生尾帧时，额外抓官方输出视频
```

FL2VA 里 `derived_tail_frame_source` 类资产是**官方输出视频**，只用来提取尾帧，
不能作为模型输入；用 `ffmpeg` 取最后一帧：

```bash
ffmpeg -sseof -0.1 -i assets/files/FL2VA-01_asset2_xxxxxxxx.mp4 -frames:v 1 tail.png
```
