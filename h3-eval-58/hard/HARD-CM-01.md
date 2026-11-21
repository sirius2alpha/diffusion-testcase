---
case_id: "HARD-CM-01"
package: "困难包"
modality: "REF2VA"
input_modality: "文本＋参考图"
subtask: "困难样本／多种运镜·望远镜扫镜"
business_scenario: "品牌概念片"
difficulty: "5"
difficulty_category: "多种运镜"
duration_seconds: "15"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Vintage Binocular Brand Film"
reuse_type: "public_multimodal_example_adapted"
---

# HARD-CM-01 · 困难样本／多种运镜·望远镜扫镜

困难包 / REF2VA / 文本＋参考图 · 15 秒 · 16:9 · 难度 5/5 · 困难类别：多种运镜

## 提示词（中文执行版）

```text
按原示例：Image 1–4 作为顺序关键帧，透过复古双筒望远镜取景器寻找 MINIMAX 装置。开场失焦并带手持轻晃，随后快速推近并对焦 Image 1；关键帧之间用快速望远镜扫镜（甩动、运动模糊、光学拖影、短暂曝光闪烁），在模糊峰值处硬切再迅速回焦。双圆镜头遮罩全程固定（位置、大小、羽化黑边不变形、不漂移），只有遮罩内画面运动。红色字体随对焦从模糊低透明度逐渐清晰（0.3–0.5 秒），随后淡出。Wes Anderson 式 35mm 胶片质感。
```

## 音频要求

胶片运转声、手持轻晃衣料声、对焦时轻微机械声；无对白、无配乐。

## 参考资产

Image 1–4＝顺序关键帧（望远镜遮罩内画面）

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/V3Q7hGYOXcAfDAXQlY7Jp_3-1-1-1_ref1.webp> |
| 2 | Image 2 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44050/PQ8WMlRX8qXrhltqlfQjJ_3-1-1-1_ref2.webp> |
| 3 | Image 3 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/mewPYqpZk_dPc1bghf0Br_3-1-1-1_ref3.webp> |
| 4 | Image 4 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/N0RL2HgqSGxNDMteJUYQW_3-1-1-1_ref4.webp> |
| 5 | - | 官方示例输出（仅参考，不输入） | video | <https://v3b.fal.media/files/b/0aa44040/X3-b2BWEyEaZr4luiu83G_out00_3-1-1.mp4> |

本地文件名见 [`../assets/assets.csv`](../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

15 秒望远镜视角品牌片，推近、甩镜、硬切、回焦依次可辨，遮罩固定，MINIMAX 字样清晰。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：多运镜执行（推近／甩镜／硬切）；遮罩稳定性；关键帧顺序；文字与对焦同步

## 硬失败规则

- 遮罩漂移或变形
- 关键帧顺序错乱
- MINIMAX 字样乱码
- 镜头运动与指令不符（变成静止画面）

## 资产准备

下载四张参考图，核对编号与上传顺序；不上传示例输出视频。

## 改编说明

复用 fal 官方示例完整 Prompt；本条同时检验多参考绑定、多运镜与文字保真。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Vintage Binocular Brand Film
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Use Images 1–4 as sequential keyframes, seen through a vintage binocular viewfinder searching for the MINIMAX installation. Open out of focus with subtle handheld shake, then push in quickly and rack focus onto Image 1. Between keyframes, use fast binocular-scan transitions with whip movement, motion blur, optical smearing, and brief exposure flicker. Cut at peak blur, then settle and snap back into focus. Keep the twin circular lens mask absolutely fixed throughout: identical position, scale, feathered black vignette, and edge softness, with no warping or drift. Only the image inside the mask may move.
In Image 2, let the fabric move gently in the wind while the MINIMAX lettering follows the folds and remains legible. In Image 3, the subject should feel like a stylish passerby caught by chance, walking, turning, and swinging their arms naturally. In Image 4, the subject adjusts their glasses or lifts their chin slightly with a cool, effortless fashion-campaign attitude.
Red typography should resolve with the focus: begin slightly blurred and at low opacity, then fade into clarity over 0.3–0.5 seconds. A subtle vertical slide or slight tracking expansion is allowed. Fade it out before the next transition or let motion blur carry it away. No spins, bounces, or large fly-ins/outs.
Visual language: a voyeuristic, Wes Anderson-inspired 35 mm film look with fine grain, soft highlight halation, restrained color, and red typographic accents. Minimal, premium, lightly playful. Do not add people, vehicles, buildings, or logos. Preserve the core composition and the MINIMAX installation exactly.
```
