---
case_id: "HARD-FH-02"
package: "困难包"
modality: "T2VA"
input_modality: "文本"
subtask: "困难样本／手部细节·打领带"
business_scenario: "职场穿搭自媒体"
difficulty: "4"
difficulty_category: "人脸与手部细节"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "VBench — human_action.txt"
reuse_type: "original_prompt_adapted_detail_camera"
---

# HARD-FH-02 · 困难样本／手部细节·打领带

困难包 / T2VA / 文本 · 10 秒 · 16:9 · 难度 4/5 · 困难类别：人脸与手部细节

## 提示词（中文执行版）

```text
固定近景，一位穿白衬衫的男士在镜前打领带：双手交叉宽端与窄端、绕圈、穿过领口环、拉紧并整理结形。手指与领带布料接触清晰，布料褶皱随拉动变化，最终领结居中对称。全程不切镜，人物上半身与双手完整可见。
```

## 音频要求

布料摩擦声、轻微呼吸与室内环境声；无配乐、无对白。

## 参考资产

无需输入资产（纯文本题）。

## 预期输出

10 秒一镜到底打领带过程，手指结构正常，步骤完整，结形居中。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：手指数量与结构；手—领带接触；打结步骤顺序；布料物理

## 硬失败规则

- 多指／少指／手指融合
- 领带步骤缺失或顺序错误
- 领带穿过手或身体
- 结形完全不对称

## 资产准备

无需资产

## 改编说明

VBench 原题仅一句动作描述；中文执行版补全可验收的打结步骤。

## 来源与权利

- 来源：VBench — human_action.txt
- 来源页面：<https://github.com/Vchitect/VBench/blob/master/prompts/prompts_per_dimension/human_action.txt>
- 复用方式：`original_prompt_adapted_detail_camera`
- 权利状态：Apache-2.0（VBench 仓库）；保留出处、许可与修改说明

## 原文（source_prompt_original，仅供对照）

```text
A person is tying tie
```
