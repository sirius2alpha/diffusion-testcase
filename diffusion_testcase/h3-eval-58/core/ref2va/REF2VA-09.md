---
case_id: "REF2VA-09"
package: "核心包"
modality: "REF2VA"
input_modality: "参考视频×1"
subtask: "视频局部编辑／主体替换"
business_scenario: "后期制作／短视频改稿"
difficulty: "4"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Cat-to-Dog Replacement"
reuse_type: "public_multimodal_example_adapted"
---

# REF2VA-09 · 视频局部编辑／主体替换

核心包 / REF2VA / 参考视频×1 · 10 秒 · 16:9 · 难度 4/5

## 提示词（中文执行版）

```text
仅将 Video 1 中的猫替换为一只体型相近、健康自然的狗，狗占据相同位置并完成相近动作。保留原视频背景、镜头运动、光照、遮挡关系、时长和其他所有主体，不做全局风格化，不添加文字。
```

## 音频要求

保留原环境音与动作节奏；仅在原猫发声位置替换为自然犬声，其他声音不变；无配乐。

## 参考资产

Video 1＝待局部编辑原视频，其余内容保留

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Video 1 | 模型输入·视频 | video | <https://v3b.fal.media/files/b/0aa44040/vKUrteICQZw-0ZrY2ZYvX_3-3-1-1_in1.mp4> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

生成结果正确使用全部指定参考，目标动作、编辑与声音符合提示，未指定部分保持稳定。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：目标替换完整度；非目标区域保持；遮挡与运动连续；原声保持

## 硬失败规则

- 背景或镜头明显改变
- 猫仍残留
- 出现第二只主要动物
- 全局变成动画或重新生成另一段视频

## 资产准备

按条目链接下载原始输入媒体；保持 Image／Video／Audio 编号与上传顺序一致；不上传示例输出视频。

## 改编说明

原网页说明多数提示词为摘录；中文版本依据可见资产补齐音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Cat-to-Dog Replacement
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Replace the cat in the video with a dog.
```
