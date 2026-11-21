---
case_id: "REF2VA-01"
package: "核心包"
modality: "REF2VA"
input_modality: "文本＋参考图×4"
subtask: "多图绑定／人物与商品"
business_scenario: "时尚品牌广告"
difficulty: "5"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Desert Fashion Campaign"
reuse_type: "public_multimodal_example_adapted"
---

# REF2VA-01 · 多图绑定／人物与商品

核心包 / REF2VA / 文本＋参考图×4 · 10 秒 · 16:9 · 难度 5/5

## 提示词（中文执行版）

```text
制作 10 秒 16:9 高级时尚片。Image 1 只用于荒漠公路、老爷车、整体氛围和胶片质感；Image 2 锁定女主角面部、发型和服装；Image 3 锁定黑色手袋外形；Image 4 只用于结尾品牌标识。0–4 秒女主走到车尾并打开后备箱，4–7 秒取出 Image 3 的手袋，与车旁男士短暂对视，7–10 秒拎包离开并切入 Image 4 品牌结束帧。服装与手袋自然参与动作，不变形、不串用其他参考。
```

## 音频要求

荒漠风声、脚步、后备箱开合与皮革摩擦声；极简原创氛围配乐；无对白。

## 参考资产

Image 1＝场景与胶片质感；Image 2＝女主身份与服装；Image 3＝手袋；Image 4＝结束品牌标识

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/1UxNnVdjUikZvA2cfcM77_3-1-1-4_ref1.webp> |
| 2 | Image 2 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/pZC5MfA6RlAe4aOqyD9ht_3-1-1-4_ref2.webp> |
| 3 | Image 3 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/k4zkM9sNrFFVk0IwGHUQQ_3-1-1-4_ref3.webp> |
| 4 | Image 4 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/F0LWFW4E1LQYg_zRE4DqR_3-1-1-4_ref4.webp> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

生成结果正确使用全部指定参考，目标动作、编辑与声音符合提示，未指定部分保持稳定。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：四参考角色绑定；女主身份；手袋与服装保真；动作顺序；结束品牌帧

## 硬失败规则

- 手袋变成其他款式
- Image 1 的人物替换 Image 2
- 漏开后备箱
- 品牌标识乱码或张冠李戴

## 资产准备

按条目链接下载原始输入媒体；保持 Image／Video／Audio 编号与上传顺序一致；不上传示例输出视频。

## 改编说明

原网页说明多数提示词为摘录；中文版本依据可见资产补齐音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Desert Fashion Campaign
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Create a premium 16:9 landscape fashion film. Use Image 1 for the overall mood, location, and film texture; Image 2 for the talent; Image 3 for the bag; and Image 4 for the closing brand mark. This is a fashion campaign for the clothing and bag. The tone is elevated, cool, and restrained, but the edit should still feel lively and fashion-forward—not like a conventional narrative film or an e-commerce ad.
Keep the story simple: beside a vintage car on a desert highway, a woman walks to the rear of the car, opens the trunk, takes out a black bag, shares a quiet beat with the man standing nearby, then leaves carrying the bag. Integrate the clothing and bag naturally into the performance so they feel like part of the characters’ identity.
```
