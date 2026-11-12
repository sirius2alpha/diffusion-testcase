---
case_id: "HARD-TX-03"
package: "困难包"
modality: "REF2VA"
input_modality: "文本＋参考图"
subtask: "困难样本／文字保真·参考图文字迁移"
business_scenario: "电商落地页与商品 UI"
difficulty: "5"
difficulty_category: "文字生成与指定文字保真"
duration_seconds: "12"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Nike-Style Product Landing Page"
reuse_type: "public_multimodal_example_adapted"
---

# HARD-TX-03 · 困难样本／文字保真·参考图文字迁移

困难包 / REF2VA / 文本＋参考图 · 12 秒 · 16:9 · 难度 5/5 · 困难类别：文字生成与指定文字保真

## 提示词（中文执行版）

```text
以 Image 1 的鞋款商品为基准，制作 12 秒产品落地页 UI 演示：快速有力的纵向滚动经过 hero 区、特性区与购买区，hover 交互时按钮放大并反色。Image 1 商品上的品牌文字与型号必须逐字保真出现在 hero 区；大号斜体无衬线标题清晰可读，不错拼、不乱码、不多字。
```

## 音频要求

滚动 whoosh、hover 点击音、低频节奏；无对白。

## 参考资产

Image 1＝商品与商品上文字（品牌／型号）的保真基准

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/Nf-ehb4Tv_oykkFMlL_Xn_3-1-5-2_ref1.webp> |
| 2 | - | 官方示例输出（仅参考，不输入） | video | <https://v3b.fal.media/files/b/0aa4404f/-BQ2kcZsnQ60QBeZbQD1g_out17_3-1-5.mp4> |

本地文件名见 [`../assets/assets.csv`](../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

12 秒落地页滚动演示，商品与 hero 区文字逐字保真，交互节奏清晰。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：参考图文字保真（逐字对照 Image 1）；UI 排版；滚动与交互节奏

## 硬失败规则

- 商品上文字错拼／乱码／缺失
- 商品变形
- 标题文字不可读
- 出现无关文字或水印

## 资产准备

下载 Image 1，评测前先人工转录商品上的目标文字并记入评分表，再与生成结果逐字对照。

## 改编说明

复用 fal 官方示例输入图与原提示；中文执行版新增参考图文字保真验收，需先转录目标文字再评测。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Nike-Style Product Landing Page
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Create a dynamic product-landing-page UI/UX demo inspired by Nike’s digital language, built around the product in Image 1. Use oversized, bold, italicized sans-serif typography and backgrounds that combine speed-driven light streaks with dark carbon fiber or breathable performance-mesh textures. Show a smooth, fast, powerful scroll through the page, plus high-impact hover interactions with scale-ups and color inversion.
```
