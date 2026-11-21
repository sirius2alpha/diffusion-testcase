---
case_id: "REF2VA-04"
package: "核心包"
modality: "REF2VA"
input_modality: "文本＋参考图×3"
subtask: "商品保真／多人时尚表演"
business_scenario: "眼镜电商与品牌广告"
difficulty: "4"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "9:16"
source: "fal MiniMax H3 Prompting Guide — Futuristic Eyewear Campaign"
reuse_type: "public_multimodal_example_adapted"
---

# REF2VA-04 · 商品保真／多人时尚表演

核心包 / REF2VA / 文本＋参考图×3 · 10 秒 · 9:16 · 难度 4/5

## 提示词（中文执行版）

```text
制作 10 秒 9:16 高级眼镜广告。Image 1 锁定两位全身模特、服装、白色无缝摄影棚和肢体关系；Image 2 补充面部细节；Image 3 锁定两位模特佩戴的未来感眼镜，包括包裹式曲面镜片、猫眼与护目镜混合轮廓、镜面反射和流线镜腿。两位模特依次转头、并肩向前走一步并停下，镜头从全身缓慢推至眼镜近景，商品不变形。
```

## 音频要求

原创冷感电子节拍、脚步和轻微镜架触碰声；无对白，不出现歌词。

## 参考资产

Image 1＝双模特与棚拍；Image 2＝面部细节；Image 3＝眼镜商品

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/A7EDo_J65S-WX62RdaQvS_3-1-4-1_ref1.webp> |
| 2 | Image 2 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/0qwssBfAaHIucktJHpXeC_3-1-4-1_ref2.webp> |
| 3 | Image 3 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/bF3Ouc7OGu4h7NWOEG61G_3-1-4-1_ref3.webp> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

生成结果正确使用全部指定参考，目标动作、编辑与声音符合提示，未指定部分保持稳定。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：商品轮廓与材质；双人身份；眼镜佩戴稳定；推镜后商品可读性

## 硬失败规则

- 眼镜变成普通墨镜／两侧款式不同
- 镜片或镜腿消失
- 模特换脸
- 近景商品严重变形

## 资产准备

按条目链接下载原始输入媒体；保持 Image／Video／Audio 编号与上传顺序一致；不上传示例输出视频。

## 改编说明

原网页说明多数提示词为摘录；中文版本依据可见资产补齐音轨和验收约束。 原摘录提到参考视频，但页面未公开对应输入视频；本条删除该不可获得条件，仅使用三张可见图片。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Futuristic Eyewear Campaign
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Create a premium 9:16 fashion-eyewear commercial. Match the reference video’s shot rhythm, edit speed, white-cyclorama look, and severe fashion attitude. Use a seamless minimal white studio with clean, bold, avant-garde art direction worthy of a global luxury campaign.
Use Image 1 for the key visual: two full-body female models, one Black and one white, preserving their elevated wardrobe, body language, studio lighting, runway presence, and cool attitude. Use Image 2 for facial details. Both models wear futuristic luxury eyewear based on Image 3: wraparound curved lenses, a sharp cat-eye/goggle hybrid silhouette, mirrored reflections, streamlined temples, and the finish of a premium fashion accessory.
```
