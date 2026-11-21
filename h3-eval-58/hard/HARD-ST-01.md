---
case_id: "HARD-ST-01"
package: "困难包"
modality: "T2VA"
input_modality: "文本"
subtask: "困难样本／伪影·静态闪烁"
business_scenario: "所有场景的底座能力"
difficulty: "4"
difficulty_category: "伪影／闪烁／细节稳定"
duration_seconds: "8"
aspect_ratio: "16:9"
source: "VBench — temporal_flickering.txt"
reuse_type: "original_prompt_adapted_static"
---

# HARD-ST-01 · 困难样本／伪影·静态闪烁

困难包 / T2VA / 文本 · 8 秒 · 16:9 · 难度 4/5 · 困难类别：伪影／闪烁／细节稳定

## 提示词（中文执行版）

```text
固定机位，一间安静厨房的静态画面：料理台、水槽、厨具与窗光在 8 秒内保持完全静止，仅允许极轻微的自然光影呼吸。任何物体不得移动、变形、出现或消失，纹理与曝光保持稳定。
```

## 音频要求

极轻室内底噪（冰箱低鸣）；无对白、无配乐。

## 参考资产

无需输入资产（纯文本题）。

## 预期输出

8 秒近乎静止的厨房画面，人工逐帧检查无闪烁、无漂移、无纹理突变。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：时序闪烁；几何漂移；纹理闪烁；外观突变

## 硬失败规则

- 任何可见闪烁
- 物体移动／变形／增减
- 曝光骤变

## 资产准备

无需资产

## 改编说明

VBench temporal_flickering 维度原题即静态场景，用于以人工方式检验闪烁与细节稳定，判定比自动指标更严格。

## 来源与权利

- 来源：VBench — temporal_flickering.txt
- 来源页面：<https://github.com/Vchitect/VBench/blob/master/prompts/prompts_per_dimension/temporal_flickering.txt>
- 复用方式：`original_prompt_adapted_static`
- 权利状态：Apache-2.0（VBench 仓库）；保留出处、许可与修改说明

## 原文（source_prompt_original，仅供对照）

```text
A tranquil tableau of kitchen
```
