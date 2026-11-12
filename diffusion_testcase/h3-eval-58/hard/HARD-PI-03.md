---
case_id: "HARD-PI-03"
package: "困难包"
modality: "REF2VA"
input_modality: "文本＋参考图"
subtask: "困难样本／人＋商品·服装穿着"
business_scenario: "时尚品牌广告"
difficulty: "4"
difficulty_category: "人＋商品互动"
duration_seconds: "15"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Cyber-Grunge Fashion Film"
reuse_type: "public_multimodal_example_adapted"
---

# HARD-PI-03 · 困难样本／人＋商品·服装穿着

困难包 / REF2VA / 文本＋参考图 · 15 秒 · 16:9 · 难度 4/5 · 困难类别：人＋商品互动

## 提示词（中文执行版）

```text
以 Image 2 锁定人物身份（白金长发、黑色窄墨镜、亮面黑色漆皮风衣），Image 1 提供质感与氛围，生成 15 秒 16:9 时尚短片：人物在夜间火堆前走动、转身、抬手整理衣领并倚靠栏杆，风衣随动作摆动、火光在漆面反射流动。允许快速剪辑与 VHS 故障、扫描线效果，但每镜内人物与服装一致，特效不破坏面部与服装主体。
```

## 音频要求

火焰噼啪、布料摩擦、低频氛围电子乐；无对白。

## 参考资产

Image 1＝质感与氛围参考；Image 2＝人物身份与服装

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/9Eemto-aYNtyAGtfrHCdj_3-1-1-5_ref1.webp> |
| 2 | Image 2 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/SpdaBOaq8baQmmcrIXoE1_3-1-1-5_ref2.webp> |
| 3 | - | 官方示例输出（仅参考，不输入） | video | <https://v3b.fal.media/files/b/0aa44040/yVqUCcogilhzfQTiJ5t02_out04_3-1-1.mp4> |

本地文件名见 [`../assets/assets.csv`](../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

15 秒时尚短片，人物穿着并展示风衣（走动、整理、摆动），身份与服装在特效下保持稳定。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：人—服装互动（穿着／整理／摆动）；身份保持；特效下细节稳定

## 硬失败规则

- 服装款式／颜色改变
- 面部漂移
- 人物静立展示无互动
- 故障效果导致主体不可辨

## 资产准备

下载两张参考图，核对编号与上传顺序；不上传示例输出视频。

## 改编说明

复用 fal 官方示例与原提示；中文执行版把互动动作与特效边界写成可验收条款。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Cyber-Grunge Fashion Film
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Use Image 1 as the reference for texture and mood, and Image 2 for the subject’s appearance. Generate a 15-second, 16:9 fashion short. Preserve the subject’s identity: long platinum-blonde hair, narrow black vintage sunglasses, a glossy black patent-leather trench coat, a cool, self-assured expression, and orange firelight reflected across the coat.
Style: fast-cut fashion film on analog stock, set against a nighttime blaze with black smoke and orange-red flames. Layer in VHS glitches, CCTV signal interruptions, 1990s film grain, scanlines, chromatic aberration, light leaks, flash-to-white transitions, and subtle frame jitter.
```
