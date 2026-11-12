---
case_id: "HARD-MP-01"
package: "困难包"
modality: "T2VA"
input_modality: "文本"
subtask: "困难样本／多人·群体游戏"
business_scenario: "校园与亲子短视频"
difficulty: "5"
difficulty_category: "多人"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "T2V-CompBench — 6_interaction.txt"
reuse_type: "original_prompt_adapted_count_audio"
---

# HARD-MP-01 · 困难样本／多人·群体游戏

困难包 / T2VA / 文本 · 10 秒 · 16:9 · 难度 5/5 · 困难类别：多人

## 提示词（中文执行版）

```text
写实操场，四名儿童分组跳绳：两人摇绳、两人依次跳入，绳子呈规则圆弧摆动，跳绳者双脚起落与绳体过脚时点一致。画面中儿童数量全程固定为四人，不增加、不减少，个体服装与身份不互换，不出现第五人。
```

## 音频要求

绳子破空声、脚步落地声、儿童笑声与数数声；无配乐。

## 参考资产

无需输入资产（纯文本题）。

## 预期输出

10 秒四人跳绳，人数恒定，绳体成弧，跳跃与过绳同步。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：人数恒定（4 人）；绳体圆弧物理；跳跃与过绳同步；个体身份不互换

## 硬失败规则

- 人数变化
- 绳子断裂／穿模／不呈弧
- 跳跃与绳完全错位
- 人物融合

## 资产准备

无需资产

## 改编说明

保留原题群体游戏语义，明确四人数量锚点以检验人群计数与身份保持。

## 来源与权利

- 来源：T2V-CompBench — 6_interaction.txt
- 来源页面：<https://github.com/KaiyueSun98/T2V-CompBench/blob/V2/prompts/6_interaction.txt>
- 复用方式：`original_prompt_adapted_count_audio`
- 权利状态：未发现仓库级 LICENSE（本次检索返回 404）；仅链接原题，正式再分发前需确认授权

## 原文（source_prompt_original，仅供对照）

```text
A group of children engage in a lively game of jump rope
```
