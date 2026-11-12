---
case_id: "REF2VA-06"
package: "核心包"
modality: "REF2VA"
input_modality: "文本＋参考图×6＋参考视频×1"
subtask: "多参考组合／剪辑节奏迁移"
business_scenario: "品牌电影混剪"
difficulty: "5"
difficulty_category: "-"
duration_seconds: "15"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Multi-Asset Cinematic Remix"
reuse_type: "public_multimodal_example_adapted"
---

# REF2VA-06 · 多参考组合／剪辑节奏迁移

核心包 / REF2VA / 文本＋参考图×6＋参考视频×1 · 15 秒 · 16:9 · 难度 5/5

## 提示词（中文执行版）

```text
Image 1–6 均为内容资产，保持每张图中的主体身份、商品或场景特征，不相互融合；Video 1 只作为镜头节奏、转场语言和音乐结构参考。将六张图片中的内容重组为 15 秒电影感混剪，按 Video 1 的剪切密度和情绪起伏安排出现顺序，每次转场都保留主体辨识度，不直接复制 Video 1 中的人物或商品。
```

## 音频要求

参考 Video 1 的音乐结构与重音位置，重新生成无侵权旋律的原创配乐；动作转场点配置简洁音效；无对白。

## 参考资产

Image 1–6＝内容资产；Video 1＝剪辑节奏、转场和音乐结构

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44050/MyXMNUIzKsoWVCGGrOvRN_3-2-1-1_ref1.webp> |
| 2 | Image 2 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/xUAGrwemSsdcxx_s5kz9i_3-2-1-1_ref2.webp> |
| 3 | Image 3 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/YFGVkzhPRCFE5g-zyoKp-_3-2-1-1_ref3.webp> |
| 4 | Image 4 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44050/qnEWKeTFEN_2RVFPdpl3z_3-2-1-1_ref4.webp> |
| 5 | Image 5 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/n3MxAdI6T6ym0HjytKt64_3-2-1-1_ref5.webp> |
| 6 | Image 6 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/tqaWhAlodUZxjSG-syKvH_3-2-1-1_ref6.webp> |
| 7 | Video 1 | 模型输入·视频 | video | <https://v3b.fal.media/files/b/0aa44040/y8LRcPncOXeXsDLbw_sqF_3-2-1-1_in1.mp4> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

生成结果正确使用全部指定参考，目标动作、编辑与声音符合提示，未指定部分保持稳定。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：六图覆盖与互不串扰；视频节奏迁移；转场重音；主体身份与商品保真

## 硬失败规则

- 遗漏任一 Image 资产
- 两张图主体融合
- 复制 Video 1 新主体
- 剪辑节奏与参考明显无关

## 资产准备

按条目链接下载原始输入媒体；保持 Image／Video／Audio 编号与上传顺序一致；不上传示例输出视频。

## 改编说明

原网页说明多数提示词为摘录；中文版本依据可见资产补齐音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Multi-Asset Cinematic Remix
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Use Images 1–6 as assets. Match Reference Video 1 closely for shot rhythm, transition language, and music.
```
