---
case_id: "HARD-HS-02"
package: "困难包"
modality: "T2VA"
input_modality: "文本"
subtask: "困难样本／高速动作·极限运动"
business_scenario: "运动品牌短视频"
difficulty: "4"
difficulty_category: "高速动作"
duration_seconds: "8"
aspect_ratio: "16:9"
source: "T2V-CompBench — 6_interaction.txt"
reuse_type: "original_prompt_adapted_audio_camera"
---

# HARD-HS-02 · 困难样本／高速动作·极限运动

困难包 / T2VA / 文本 · 8 秒 · 16:9 · 难度 4/5 · 困难类别：高速动作

## 提示词（中文执行版）

```text
写实滑板公园，一名滑板者加速后做腾空动作：双脚带板起跳、滑板在空中保持水平、随后双脚落回板上并屈膝缓冲着地，继续向前滑行。低机位侧面跟拍，人物与滑板全程不分离、不穿模，肢体结构正常，滑板轮在落地后重新转动。
```

## 音频要求

轮子滚动声、起跳瞬间板面敲击声、落地闷响；无配乐、无对白。

## 参考资产

无需输入资产（纯文本题）。

## 预期输出

8 秒跟拍滑板腾空—滞空—落地完整过程，人板不分离，落地后恢复滑行。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：人—板接触关系；腾空—滞空—落地时序；肢体结构；动作音时点

## 硬失败规则

- 滑板消失或与脚融合
- 落地穿模
- 肢体多指／断肢
- 板在空中翻转失控

## 资产准备

无需资产

## 改编说明

保留原题动作，补充人板关系与落地续滑的可观察检查点。

## 来源与权利

- 来源：T2V-CompBench — 6_interaction.txt
- 来源页面：<https://github.com/KaiyueSun98/T2V-CompBench/blob/V2/prompts/6_interaction.txt>
- 复用方式：`original_prompt_adapted_audio_camera`
- 权利状态：未发现仓库级 LICENSE（本次检索返回 404）；仅链接原题，正式再分发前需确认授权

## 原文（source_prompt_original，仅供对照）

```text
A skateboarder performing a trick, launching their board into the air before landing back on the pavement.
```
