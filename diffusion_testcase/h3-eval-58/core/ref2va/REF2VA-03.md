---
case_id: "REF2VA-03"
package: "核心包"
modality: "REF2VA"
input_modality: "文本＋参考图×2"
subtask: "双角色身份／短剧对话"
business_scenario: "竖屏家庭短剧"
difficulty: "5"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "9:16"
source: "fal MiniMax H3 Prompting Guide — Vertical Family Confrontation"
reuse_type: "public_multimodal_example_adapted"
---

# REF2VA-03 · 双角色身份／短剧对话

核心包 / REF2VA / 文本＋参考图×2 · 10 秒 · 9:16 · 难度 5/5

## 提示词（中文执行版）

```text
9:16 写实家庭争执场景，Image 1 锁定秦浩轩，Image 2 锁定年长女性，背景为中国家庭或小餐馆，暖色室内光、红色装饰与浅景深。0–3 秒女性厉声问：‘你到底还要瞒多久？’ 3–7 秒秦浩轩愤怒又受伤地回答：‘我只是不想让你再担心。’ 7–10 秒正反打加快，女性逼近一步，秦浩轩沉默。表演自然，不舞台剧化，不加字幕、水印或贴纸。
```

## 音频要求

两位中文台词逐字清晰、声线与人物绑定；室内底噪和轻微脚步；无配乐。

## 参考资产

Image 1＝秦浩轩身份；Image 2＝年长女性身份

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/7-za79fXKpM8Q5SggP_GO_3-1-3-2_ref1.webp> |
| 2 | Image 2 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/B2SgwXPNdc2TMmlgWXO12_3-1-3-2_ref2.webp> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

生成结果正确使用全部指定参考，目标动作、编辑与声音符合提示，未指定部分保持稳定。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：双人身份；说话人—声线—口型绑定；情绪递进；9:16 构图；无字幕约束

## 硬失败规则

- 两人换脸／串音
- 任一规定台词缺失或改词
- 出现自动字幕
- 表演风格变为动画或古装

## 资产准备

按条目链接下载原始输入媒体；保持 Image／Video／Audio 编号与上传顺序一致；不上传示例输出视频。

## 改编说明

原网页说明多数提示词为摘录；中文版本依据可见资产补齐音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Vertical Family Confrontation
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
A 9:16 vertical family-confrontation scene with grounded live-action performances, set in a Chinese family home or small restaurant. Use warm interior light, red decorations and calligraphy in the background, shallow depth of field, intense emotion, and tight pacing.
Performance: natural short-form drama, never theatrical. Qin Haoxuan argues back with anger, hurt, and urgency. The older woman questions him in a sharp, forceful, relentless tone. Build the confrontation steadily.
Shoot mainly in medium-close shots with frequent shot/reverse-shot cutting. Keep the setting lived-in and realistic. No sci-fi, period costume, or animation styling. Do not show subtitles, added text, platform watermarks, or stickers.
```
