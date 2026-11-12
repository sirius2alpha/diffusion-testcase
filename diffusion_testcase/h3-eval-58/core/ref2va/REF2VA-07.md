---
case_id: "REF2VA-07"
package: "核心包"
modality: "REF2VA"
input_modality: "文本＋参考图×2＋参考视频×1"
subtask: "参考视频动作迁移／双人身份"
business_scenario: "舞蹈短视频／虚拟角色"
difficulty: "5"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Street Dance Motion Transfer"
reuse_type: "public_multimodal_example_adapted"
---

# REF2VA-07 · 参考视频动作迁移／双人身份

核心包 / REF2VA / 文本＋参考图×2＋参考视频×1 · 10 秒 · 16:9 · 难度 5/5

## 提示词（中文执行版）

```text
Video 1 只作为街舞动作、重心、节奏与表演时点参考；Image 1 和 Image 2 分别锁定两位舞者身份、服装与外观。让两位角色在完整身体可见的街舞场景中复现主要动作序列，左右关系清晰，脚步、手臂和转身时点贴近参考，保持各自身份，不交换服装，不改变 Video 1 的背景为输入条件。
```

## 音频要求

生成原创街舞鼓点，脚步落地与低音鼓同步；保留鞋底摩擦和喘息；不使用可识别现成歌曲、无对白。

## 参考资产

Image 1–2＝两位舞者身份；Video 1＝动作、重心与节奏

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/-4dp5kbzdRqinGhtzgS9Q_3-2-2-2_ref1.webp> |
| 2 | Image 2 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/Gas53M7Tuo0s1PYYOQRkE_3-2-2-2_ref2.webp> |
| 3 | Video 1 | 模型输入·视频 | video | <https://v3b.fal.media/files/b/0aa44040/ByMddW2HA-LxjZ8f1X-f3_3-2-2-2_in1.mp4> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

生成结果正确使用全部指定参考，目标动作、编辑与声音符合提示，未指定部分保持稳定。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：双角色身份绑定；动作序列与节奏；脚步重心；音乐与落地时点

## 硬失败规则

- 两人身份／服装交换
- 动作变成无关舞蹈
- 脚部严重滑步或穿地
- 鼓点与主要落地动作明显错位

## 资产准备

按条目链接下载原始输入媒体；保持 Image／Video／Audio 编号与上传顺序一致；不上传示例输出视频。

## 改编说明

原网页说明多数提示词为摘录；中文版本依据可见资产补齐音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Street Dance Motion Transfer
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Use Video 1 as the motion reference for a street-dance performance. Use Images 1 and 2 as the character references.
```
