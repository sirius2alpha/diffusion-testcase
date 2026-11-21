---
case_id: "HARD-CM-02"
package: "困难包"
modality: "REF2VA"
input_modality: "文本＋参考图"
subtask: "困难样本／多种运镜·快切 MV"
business_scenario: "音乐 MV 与潮流广告"
difficulty: "4"
difficulty_category: "多种运镜"
duration_seconds: "15"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Cyber-Grunge Rap Music Video"
reuse_type: "public_multimodal_example_adapted"
---

# HARD-CM-02 · 困难样本／多种运镜·快切 MV

困难包 / REF2VA / 文本＋参考图 · 15 秒 · 16:9 · 难度 4/5 · 困难类别：多种运镜

## 提示词（中文执行版）

```text
以两张参考图的排版与表面质感为准，制作 15 秒暗潮／赛博垃圾风说唱 MV：全程硬切剪辑（禁止淡入淡出），镜头在表演者中近景、手部特写与快速推镜之间切换，叠加粗颗粒、门 weave、半调网点、扫描错位与 rough 印刷边缘。每次硬切卡在鼓点上，运镜节奏与音乐结构一致。
```

## 音频要求

原创暗潮电子节拍（kick／snare／bass），硬切与鼓点同步；无歌词人声。

## 参考资产

Image 1–2＝排版、表面质感与风格参考

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/1pS57kNUbNacQDAVT3wau_3-1-2-4_ref1.webp> |
| 2 | Image 2 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/K6RRNz9zu5ycrR1L29lMd_3-1-2-4_ref2.webp> |
| 3 | - | 官方示例输出（仅参考，不输入） | video | <https://v3b.fal.media/files/b/0aa44040/wDLAUm2rPN0BPRM78RasZ_out08_3-1-2.mp4> |

本地文件名见 [`../assets/assets.csv`](../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

15 秒快切 MV，硬切全部落在鼓点上，运镜多样且质感参考保持。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：硬切节奏与鼓点对齐；运镜多样性；质感参考保持

## 硬失败规则

- 出现淡入淡出
- 运镜单一近乎静止
- 参考质感完全丢失
- 切点与节拍明显错位

## 资产准备

下载两张参考图，核对编号与上传顺序；不上传示例输出视频。

## 改编说明

复用 fal 官方示例与原提示；中文执行版把硬切与鼓点对齐写成可验收条款。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Cyber-Grunge Rap Music Video
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Style: dark-pop / cyber-grunge / rap music video with photoreal high-fashion polish and the texture of a scanned film magazine—high contrast without looking cheap. Reference late-1990s to early-2000s indie magazines, photocopies, film scans, underground-music posters, and zine collage. Add coarse grain, subtle gate weave, halftone dots, rough print edges, and slight scan misregistration. Keep the edit fast and use hard cuts only—no fades or soft transitions. Match the typographic treatment and surface texture of the reference images.
```
