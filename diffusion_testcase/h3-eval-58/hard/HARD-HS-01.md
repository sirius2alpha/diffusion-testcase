---
case_id: "HARD-HS-01"
package: "困难包"
modality: "T2VA"
input_modality: "文本"
subtask: "困难样本／高速动作·高速驾车"
business_scenario: "汽车广告与影视追逐镜头"
difficulty: "4"
difficulty_category: "高速动作"
duration_seconds: "8"
aspect_ratio: "16:9"
source: "T2V-CompBench — 4_motion_binding.txt"
reuse_type: "original_prompt_adapted_audio_camera"
---

# HARD-HS-01 · 困难样本／高速动作·高速驾车

困难包 / T2VA / 文本 · 8 秒 · 16:9 · 难度 4/5 · 困难类别：高速动作

## 提示词（中文执行版）

```text
写实夜景街道路口，一辆深色轿车高速从画面右侧向左疾驰穿过十字路口，轮胎打滑发出尖叫声，车身带轻微侧倾与方向一致的运动模糊，背景路灯与建筑因高速产生横向模糊。固定机位不切镜，车辆从头到尾保持同一车型、同一颜色、四轮着地，不出现第二辆车。
```

## 音频要求

轮胎尖叫声由弱到强再消失，发动机轰鸣由远及近；无配乐、无对白。

## 参考资产

无需输入资产（纯文本题）。

## 预期输出

8 秒固定机位高速过弯镜头，方向为右→左，车辆结构稳定、运动模糊方向一致。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：高速运动方向（右→左）；车辆几何与结构稳定；运动模糊方向；轮胎音与画面时点

## 硬失败规则

- 车辆变形／融合
- 运动方向错误（左→右）
- 车轮不转或倒转
- 完全听不到轮胎声

## 资产准备

无需资产

## 改编说明

保留原题语义，补充固定机位、运动方向与音轨验收锚点；属于改写题。

## 来源与权利

- 来源：T2V-CompBench — 4_motion_binding.txt
- 来源页面：<https://github.com/KaiyueSun98/T2V-CompBench/blob/V2/prompts/4_motion_binding.txt>
- 复用方式：`original_prompt_adapted_audio_camera`
- 权利状态：未发现仓库级 LICENSE（本次检索返回 404）；仅链接原题，正式再分发前需确认授权

## 原文（source_prompt_original，仅供对照）

```text
A car speeds left, tires squealing as it cuts across the intersection.
```
