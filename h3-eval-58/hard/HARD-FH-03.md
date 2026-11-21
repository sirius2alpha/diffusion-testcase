---
case_id: "HARD-FH-03"
package: "困难包"
modality: "T2VA"
input_modality: "文本"
subtask: "困难样本／手部细节·描眉特写"
business_scenario: "美妆自媒体"
difficulty: "4"
difficulty_category: "人脸与手部细节"
duration_seconds: "8"
aspect_ratio: "16:9"
source: "VBench — human_action.txt"
reuse_type: "original_prompt_adapted_detail_camera"
---

# HARD-FH-03 · 困难样本／手部细节·描眉特写

困难包 / T2VA / 文本 · 8 秒 · 16:9 · 难度 4/5 · 困难类别：人脸与手部细节

## 提示词（中文执行版）

```text
特写镜头，一位女性手持眉笔对着镜子描眉：一手轻抬固定眉部皮肤，另一手用眉笔沿眉形短促填色，左右眉交替，最后用眉刷轻扫定型。面部（尤其眉眼区域）与双手细节清晰稳定，眉笔始终接触眉部，不悬空、不漂移。
```

## 音频要求

极轻室内环境声、眉刷刷过皮肤的细微声；无对白、无配乐。

## 参考资产

无需输入资产（纯文本题）。

## 预期输出

8 秒描眉特写，眉眼细节稳定，眉笔—眉部接触连续，眉形渐变自然。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：眉眼细节稳定；手—眉笔—眉部三点接触；微表情；工具不漂移

## 硬失败规则

- 面部细节糊化或漂移
- 眉笔穿过脸部或悬空描画
- 眉毛颜色／形状骤变
- 手部结构异常

## 资产准备

无需资产

## 改编说明

VBench 原题仅一句动作描述；中文执行版补全工具接触与细节稳定检查点。

## 来源与权利

- 来源：VBench — human_action.txt
- 来源页面：<https://github.com/Vchitect/VBench/blob/master/prompts/prompts_per_dimension/human_action.txt>
- 复用方式：`original_prompt_adapted_detail_camera`
- 权利状态：Apache-2.0（VBench 仓库）；保留出处、许可与修改说明

## 原文（source_prompt_original，仅供对照）

```text
A person is filling eyebrows
```
