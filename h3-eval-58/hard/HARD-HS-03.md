---
case_id: "HARD-HS-03"
package: "困难包"
modality: "REF2VA"
input_modality: "文本＋参考图"
subtask: "困难样本／高速动作·武术对打"
business_scenario: "武侠影视与游戏 CG"
difficulty: "5"
difficulty_category: "高速动作"
duration_seconds: "15"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Snowy Bamboo Wuxia Mystery"
reuse_type: "public_multimodal_example_adapted"
---

# HARD-HS-03 · 困难样本／高速动作·武术对打

困难包 / REF2VA / 文本＋参考图 · 15 秒 · 16:9 · 难度 5/5 · 困难类别：高速动作

## 提示词（中文执行版）

```text
以 Image 1 的竹林夜雪场景与低饱和冷色调、Image 2 的角色形象为参考，生成 15 秒 16:9 写实武侠悬疑短片：两名侠客在竹林间快速交手——0–4 秒远景对峙，竹叶与雪飘落；4–9 秒快速近身对打（格挡、闪避、旋身），动作凌厉且身体结构稳定；9–13 秒切面部与手部特写，眼神与手势细节清晰；13–15 秒一人收势立于雪中。两名角色身份全程一致，不出现现代元素、字幕或动画风格。
```

## 音频要求

竹叶与风雪环境声、衣袂破空声、拳脚与格挡闷响；无对白、无配乐。

## 参考资产

Image 1＝竹林夜雪场景、调色与氛围；Image 2＝角色身份与服化道

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/9_quxJiBVqhyz-9jYZQP__3-1-3-1_ref1.webp> |
| 2 | Image 2 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/oCAoqLriHwCMRn47QVsf7_3-1-3-1_ref2.webp> |
| 3 | - | 官方示例输出（仅参考，不输入） | video | <https://v3b.fal.media/files/b/0aa44040/q_4a91RUKKAnhI2JDJ5HD_out11_3-1-3.mp4> |

本地文件名见 [`../assets/assets.csv`](../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

15 秒竹林夜雪武侠对打，快速打斗中身份、肢体结构与面部细节保持稳定。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：快速打斗动作结构；双角色身份一致；面部／手部特写细节；雪与竹叶物理

## 硬失败规则

- 角色面部漂移
- 肢体穿模或断肢
- 出现现代元素、字幕或动画化
- 对打变成缓慢摆姿势

## 资产准备

按条目链接下载两张参考图，核对编号与上传顺序一致；不上传示例输出视频。

## 改编说明

原网页说明多数提示词为摘录；中文执行版将悬疑氛围落为可验收的分段对打动作与音轨。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Snowy Bamboo Wuxia Mystery
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
A 16:9 cinematic wuxia mystery set in a bamboo forest at night. Use a low-saturation palette of cold blue, ink green, charcoal, and gray. Thin mist fills the forest and fine snow drifts through the air. The mood is austere, lethal, and controlled, with the tension of a martial-arts sect investigating a case and exchanging secret intelligence.
Deep in the forest, dense vertical bamboo fills the background while cold white mist-light glows in the distance. Soft, out-of-focus leaves partially obscure the foreground, creating the sense of watching from within the grove. A cool, soft front-side key lights the actors’ faces; backlight keeps the foreground dark and the distance luminous. Use shallow depth of field so leaves, snow, and bamboo dissolve into soft bokeh.
Prioritize facial close-ups and measured shot/reverse-shot coverage. Keep the rhythm restrained but tense. Photoreal period-drama production value, cinematic lighting, and no modern elements. No subtitles, on-screen text, watermarks, modern clothing or architecture, animation styling, over-smoothed skin, bright daylight, or comic performance.
```
