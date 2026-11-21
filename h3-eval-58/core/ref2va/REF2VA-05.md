---
case_id: "REF2VA-05"
package: "核心包"
modality: "REF2VA"
input_modality: "文本＋参考图×2"
subtask: "人物身份／分镜参考"
business_scenario: "仙侠动画角色宣传片"
difficulty: "5"
difficulty_category: "-"
duration_seconds: "12"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Fantasy Wuxia Character Film"
reuse_type: "public_multimodal_example_adapted"
---

# REF2VA-05 · 人物身份／分镜参考

核心包 / REF2VA / 文本＋参考图×2 · 12 秒 · 16:9 · 难度 5/5

## 提示词（中文执行版）

```text
Image 2 为唯一角色身份参考，锁定半扎黑长发、镂空银冠、靛蓝发带、浅色层叠汉服、半透蓝外袍、深蓝腰带、银花扣与长流苏；Image 1 仅用于分镜顺序与节奏。按分镜制作 12 秒 16:9 中式 3D 仙侠角色片，镜头运动自然、过渡连续而非幻灯片。面部只在近景或极近景出现；远景使用背影、后侧四分之三或空镜，不出现远景正脸。
```

## 音频要求

风声、衣袂与流苏轻响、远处一声古钟；庄重原创氛围音乐；无对白。

## 参考资产

Image 1＝分镜顺序与节奏；Image 2＝唯一角色身份与服化道

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/UyHIoFOvKqn8aO5As8Zij_3-1-6-2_ref1.webp> |
| 2 | Image 2 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/f1fFTNFZL7JbU01sRDu4I_3-1-6-2_ref2.webp> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

生成结果正确使用全部指定参考，目标动作、编辑与声音符合提示，未指定部分保持稳定。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：角色服化道保真；分镜遵循；远近景面部规则；转场非幻灯片

## 硬失败规则

- 银冠／外袍／腰带等关键特征丢失
- 远景出现正脸
- 角色换脸
- 分镜变成静态图片轮播

## 资产准备

按条目链接下载原始输入媒体；保持 Image／Video／Audio 编号与上传顺序一致；不上传示例输出视频。

## 改编说明

原网页说明多数提示词为摘录；中文版本依据可见资产补齐音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Fantasy Wuxia Character Film
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Use Image 2 as the locked character reference. Preserve the half-up long black hair, openwork silver crown, indigo ribbon, layered pale hanfu, translucent blue outer robe, deep-blue sash, silver floral fastener, and long tassels. Use Image 1 for storyboard order and pacing.
Render in high-quality 4K, 16:9 Chinese-inspired 3D with cinematic xianxia production value: intense, solemn, and shaped by destiny. Follow the storyboard beat by beat, with natural camera movement and seamless transitions—never a slideshow. Show the face only in close-up or extreme close-up. In wide shots, use back view, rear three-quarter view, or empty environment shots; never show a distant frontal face.
```
