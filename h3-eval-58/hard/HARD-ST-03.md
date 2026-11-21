---
case_id: "HARD-ST-03"
package: "困难包"
modality: "REF2VA"
input_modality: "文本＋参考图＋参考视频"
subtask: "困难样本／伪影·局部替换稳定"
business_scenario: "影视后期场景替换"
difficulty: "4"
difficulty_category: "伪影／闪烁／细节稳定"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Window View Replacement"
reuse_type: "public_multimodal_example_adapted"
---

# HARD-ST-03 · 困难样本／伪影·局部替换稳定

困难包 / REF2VA / 文本＋参考图＋参考视频 · 10 秒 · 16:9 · 难度 4/5 · 困难类别：伪影／闪烁／细节稳定

## 提示词（中文执行版）

```text
将 Input Video 1 中窗外的景色替换为 Image 1 的景观：窗框、窗台、室内人物、镜头运动与光线完全保持，仅窗外区域改变；窗玻璃反射与新景观一致，人物经过窗前时遮挡关系正确，边缘融合自然。
```

## 音频要求

保留原视频音频。

## 参考资产

Image 1＝窗外新景观；Input Video 1＝待替换原视频

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/2e6Tu9nHoWzSZzalT5WH4_3-3-2-3_ref1.webp> |
| 2 | Input Video 1 | 模型输入·视频 | video | <https://v3b.fal.media/files/b/0aa44050/YWz6UnJNrZYj5ZNPyjXBo_3-3-2-3_in1.mp4> |
| 3 | - | 官方示例输出（仅参考，不输入） | video | <https://v3b.fal.media/files/b/0aa44040/xMBtlDo5z5YVGVHrdw3pk_out38_3-3-2.mp4> |

本地文件名见 [`../assets/assets.csv`](../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

仅窗外区域替换为新景观，窗框与室内区域逐帧保持稳定，遮挡关系正确。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：局部替换精度；非目标区域稳定；遮挡关系；反射一致性

## 硬失败规则

- 窗框或室内区域被改动
- 新景观与窗框透视不符
- 人物被错误遮挡或穿透
- 边缘融合穿帮

## 资产准备

下载 Image 1 与 Input Video 1，核对编号与上传顺序；不上传示例输出视频。

## 改编说明

复用 fal 官方示例输入资产与原提示（一句话原题），中文执行版补全非目标区域保持的验收口径。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Window View Replacement
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Replace the view outside the window in Video 1 with Image 1.
```
