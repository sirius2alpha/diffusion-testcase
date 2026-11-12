---
case_id: "REF2VA-12"
package: "核心包"
modality: "REF2VA"
input_modality: "文本＋参考图×1＋参考视频×1"
subtask: "参考图风格＋视频局部特效"
business_scenario: "爱情短剧／后期特效"
difficulty: "4"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Hand-Drawn Romance VFX"
reuse_type: "public_multimodal_example_adapted"
---

# REF2VA-12 · 参考图风格＋视频局部特效

核心包 / REF2VA / 文本＋参考图×1＋参考视频×1 · 10 秒 · 16:9 · 难度 4/5

## 提示词（中文执行版）

```text
Image 1 只提供橙黄色手绘标记的笔触、颜色与发光质感；Video 1 提供两人表演和原始镜头。随着两人靠近，在他们周围增加相同风格的手绘标记，从零星小火花逐渐变密并变亮；亲吻瞬间加入粉色笔触。特效跟随人物运动，保留两人面部、背景、镜头和原始表演，不做全局滤镜。
```

## 音频要求

保留原对白与环境声；火花增加时叠加轻柔手绘沙沙声和细微电子音，亲吻时一次柔和上扬音；无新增配乐。

## 参考资产

Image 1＝手绘笔触与颜色；Video 1＝人物表演和原始镜头

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/kGEokRD-_IEApK5F3pt3H_3-3-4-4_ref1.webp> |
| 2 | Video 1 | 模型输入·视频 | video | <https://v3b.fal.media/files/b/0aa44041/tONqOAIX9BQBbcdMWgdjg_3-3-4-4_in1.mp4> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

生成结果正确使用全部指定参考，目标动作、编辑与声音符合提示，未指定部分保持稳定。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：参考笔触风格；特效随动作增长；亲吻时点；非目标画面与声音保持

## 硬失败规则

- 全画面被手绘化
- 人物或背景明显改变
- 亲吻时没有粉色笔触
- 特效遮挡面部导致表演不可见

## 资产准备

按条目链接下载原始输入媒体；保持 Image／Video／Audio 编号与上传顺序一致；不上传示例输出视频。

## 改编说明

原网页说明多数提示词为摘录；中文版本依据可见资产补齐音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Hand-Drawn Romance VFX
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Creative interpretation + animated graphic effects
Add orange-yellow hand-drawn marks like Image 1 around the two people in Video 1. As they move closer, the marks multiply and build from tiny sparks into bright radiance. When they kiss, introduce pink brushstrokes.
```
