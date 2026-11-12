---
case_id: "HARD-MP-03"
package: "困难包"
modality: "REF2VA"
input_modality: "文本＋参考视频"
subtask: "困难样本／多人·新增人物同步"
business_scenario: "团体表演与体育内容编辑"
difficulty: "5"
difficulty_category: "多人"
duration_seconds: "8"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Add a Character in Sync with the Others"
reuse_type: "public_multimodal_example_adapted"
---

# HARD-MP-03 · 困难样本／多人·新增人物同步

困难包 / REF2VA / 文本＋参考视频 · 8 秒 · 16:9 · 难度 5/5 · 困难类别：多人

## 提示词（中文执行版）

```text
在 Input Video 1 画面左侧新增一名穿相同队服的人物，与画面中其他队员做完全同步的动作（节奏、幅度、时点一致），新增人物的光照、透视与地面阴影与原画面一致，不遮挡原有人物，原视频其余内容保持不变。
```

## 音频要求

与原视频动作节拍一致的脚步与口号声；不覆盖原始音频结构。

## 参考资产

Input Video 1＝原群体表演视频（在其左侧新增同步人物）

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Input Video 1 | 模型输入·视频 | video | <https://v3b.fal.media/files/b/0aa44040/l_yC8dPdRorPJHvPdxo-l_3-3-1-2_in1.mp4> |
| 2 | - | 官方示例输出（仅参考，不输入） | video | <https://v3b.fal.media/files/b/0aa44040/LtxFezdUS47l1Nj2_DrrR_out34_3-3-1.mp4> |

本地文件名见 [`../assets/assets.csv`](../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

画面左侧新增一名同步队员，动作与其他人一致，原画面其余部分不变。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：新增人物与原队伍的同步率；队服一致性；光影透视融合；原区域保持

## 硬失败规则

- 新增人物不同步
- 队服颜色／款式不一致
- 人物悬浮或阴影错误
- 原有人物动作被改变

## 资产准备

下载 Input Video 1；不上传示例输出视频。

## 改编说明

复用 fal 官方示例输入视频与原提示（一句话原题），中文执行版补全同步率与融合验收口径。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Add a Character in Sync with the Others
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Add one person on the left side of frame wearing the same team uniform and moving in sync with the others.
```
