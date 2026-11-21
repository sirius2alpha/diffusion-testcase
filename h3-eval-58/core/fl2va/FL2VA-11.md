---
case_id: "FL2VA-11"
package: "核心包"
modality: "FL2VA"
input_modality: "文本＋首帧图＋尾帧图"
subtask: "人物表演／身份连续"
business_scenario: "奇幻游戏角色宣传片"
difficulty: "4"
difficulty_category: "-"
duration_seconds: "5"
aspect_ratio: "16:9"
source: "ComfyUI 官方 MiniMax H3 FLF2V 工作流"
reuse_type: "original_frame_pair_and_prompt_audio_added"
---

# FL2VA-11 · 人物表演／身份连续

核心包 / FL2VA / 文本＋首帧图＋尾帧图 · 5 秒 · 16:9 · 难度 4/5

## 提示词（中文执行版）

```text
Image 1 为首帧、Image 2 为尾帧。一个连续电影感奇幻镜头：天使战士在烟雾中结束与恶魔的战斗，转身并用长矛指向下方残余敌人，最终以低角度胜利英雄姿态停在尾帧。角色面部、服装、武器和画风保持一致，不切镜、不加文字。
```

## 音频要求

金属武器挥动、烟雾中的低沉嘶吼、脚步与结尾胜利姿态的一声低音重音；无对白、无歌词。

## 参考资产

Image 1＝战斗过程起点；Image 2＝低角度英雄姿态终点

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·首帧 | image | <https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/angel-warrior-demon-battle-start.png> |
| 2 | Image 2 | 模型输入·尾帧 | image | <https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/angel-warrior-demon-battle-end.png> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

5 秒单镜头战斗收尾，角色与武器稳定并到达英雄姿态。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：首尾端点；角色身份；长矛轨迹；单镜头与动作节奏

## 硬失败规则

- 换脸／换装／武器变形
- 出现切镜或文字
- 未指向下方敌人
- 尾帧姿态不符

## 资产准备

直接下载 Comfy 官方两张输入图。

## 改编说明

保留官方工作流 Prompt，中文执行版补充音轨。

## 来源与权利

- 来源：ComfyUI 官方 MiniMax H3 FLF2V 工作流
- 来源页面：<https://docs.comfy.org/tutorials/partner-nodes/minimax/minimax-h3>
- 复用方式：`original_frame_pair_and_prompt_audio_added`
- 权利状态：Comfy workflow_templates 仓库 MIT；媒体保留来源，公开再分发前核对资产声明

## 原文（source_prompt_original，仅供对照）

```text
Use Image 1 as the first frame and Image 2 as the last frame.One continuous cinematic fantasy shot. The angel warrior finishes fighting demons in the smoke, then turns and points her spear at the remaining enemies below. End in a triumphant low-angle hero pose. Same character, same style, smooth motion, no cuts, no text.
```
