---
case_id: "HARD-MP-02"
package: "困难包"
modality: "REF2VA"
input_modality: "文本＋参考图＋参考视频"
subtask: "困难样本／多人·双人表演迁移"
business_scenario: "短剧与广告表演替换"
difficulty: "5"
difficulty_category: "多人"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Character Swap with Performance Reference"
reuse_type: "public_multimodal_example_adapted"
---

# HARD-MP-02 · 困难样本／多人·双人表演迁移

困难包 / REF2VA / 文本＋参考图＋参考视频 · 10 秒 · 16:9 · 难度 5/5 · 困难类别：多人

## 提示词（中文执行版）

```text
以 Image 1 的角色形象替换 Input Video 1 中的表演者，精确复刻源视频中两人的动作、表情与表演节奏：水池边男士把洗净的盘子递给女士，随即用右手弹洗洁精泡沫逗她，女士受惊后立即还击，两人笑闹躲闪、互掷泡沫。替换后角色身份稳定，动作与源视频时序一致，盘子与泡沫交互不穿模。
```

## 音频要求

保留源视频水声、盘子碰撞与两人笑声的时间结构；替换后角色声线自然；无配乐。

## 参考资产

Image 1＝替换角色身份；Input Video 1＝双人表演、动作与节奏源

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/fQJN-UhWbbouGzRae23rO_3-2-2-1_ref1.webp> |
| 2 | Input Video 1 | 模型输入·视频 | video | <https://v3b.fal.media/files/b/0aa44040/ssRXxGPYALg3edLNCZjQ5_3-2-2-1_in1.mp4> |
| 3 | - | 官方示例输出（仅参考，不输入） | video | <https://v3b.fal.media/files/b/0aa4404f/vncjZ2AM2FKDtuHO6kQsW_out29_3-2-2.mp4> |

本地文件名见 [`../assets/assets.csv`](../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

替换角色后完整复刻双人泡沫互动，身份稳定、时序一致、手物交互不穿模。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：双人动作同步；表演时序复刻；替换角色身份稳定；手—物（盘子、泡沫）交互

## 硬失败规则

- 动作与源视频明显脱节
- 替换角色面部漂移
- 盘子／泡沫穿模
- 两人融合为一人

## 资产准备

下载 Image 1 与 Input Video 1，核对编号与上传顺序；不上传示例输出视频。

## 改编说明

复用 fal 官方示例输入资产与原提示；中文执行版补全音轨与双人交互验收口径。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Character Swap with Performance Reference
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Match the character motion, expressions, and performance timing in Image 1 closely to Input Video 1.
At the sink on the right side of frame, the man hands a washed plate to the woman on the left. He turns, then suddenly flicks dish-soap foam at her with his right hand. Startled, she immediately retaliates. They laugh, dodge, and playfully throw foam back and forth.
```
