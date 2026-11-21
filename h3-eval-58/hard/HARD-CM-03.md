---
case_id: "HARD-CM-03"
package: "困难包"
modality: "T2VA"
input_modality: "文本"
subtask: "困难样本／多种运镜·分镜时间轴"
business_scenario: "影视分镜预演"
difficulty: "5"
difficulty_category: "多种运镜"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "自设计压力题（运镜术语参考 fal H3 Prompting Guide）"
reuse_type: "guide_technique_self_designed"
---

# HARD-CM-03 · 困难样本／多种运镜·分镜时间轴

困难包 / T2VA / 文本 · 10 秒 · 16:9 · 难度 5/5 · 困难类别：多种运镜

## 提示词（中文执行版）

```text
10 秒多运镜短片，严格按时间轴执行：0–2 秒缓慢推近（push in）雨夜便利店门口的女孩；2–4 秒硬切至环绕（orbit）她半周；4–6 秒硬切至升降镜头（crane）从地面升至俯拍展现街道；6–8 秒硬切至侧面跟拍（tracking）她走入街道；8–10 秒推近至面部特写定格。四类运镜各自明确可辨，镜头切换全部为硬切，主体身份跨镜头一致。
```

## 音频要求

雨声、脚步、远处车流；每次硬切伴随轻微音效；无对白、无配乐。

## 参考资产

无需输入资产（纯文本题）。

## 预期输出

10 秒内四类运镜（推近／环绕／升降／跟拍）依次可辨，硬切切换，主体一致。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：四类运镜可辨识度；硬切时点；主体跨镜头身份一致

## 硬失败规则

- 任一类运镜缺失或无法区分
- 出现淡入淡出
- 主体换脸
- 时间轴事件缺失

## 资产准备

无需资产

## 改编说明

基于 H3 Prompting Guide 的镜头语言技巧自设计，用于把运镜能力拆成可逐项打分的压力题。

## 来源与权利

- 来源：自设计压力题（运镜术语参考 fal H3 Prompting Guide）
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`guide_technique_self_designed`
- 权利状态：本条目为自设计压力题，无外部媒体权利

## 原文（source_prompt_original，仅供对照）

```text
（无外部原题）运镜术语体系参考 fal H3 Prompting Guide 的镜头语言技巧，本条目为自设计压力题。
```
