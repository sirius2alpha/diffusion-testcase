---
case_id: "HARD-FH-01"
package: "困难包"
modality: "REF2VA"
input_modality: "文本＋参考图"
subtask: "困难样本／人脸身份·微表情"
business_scenario: "影视角色一致性与数字人"
difficulty: "5"
difficulty_category: "人脸与手部细节"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "ConsisID 官方仓库 README 示例"
reuse_type: "public_example_identity_reference"
---

# HARD-FH-01 · 困难样本／人脸身份·微表情

困难包 / REF2VA / 文本＋参考图 · 10 秒 · 16:9 · 难度 5/5 · 困难类别：人脸与手部细节

## 提示词（中文执行版）

```text
以 Image 1 的男孩面部身份为锚点，生成 10 秒黑白 35mm 胶片风格视频：男孩沿城市街道行走，眉头微蹙、若有所思，随后露出短暂微笑。背景为复古建筑、鹅卵石人行道与柔和街灯光影，路人虚化成模糊轮廓。面部身份与参考图一致，微表情自然，胶片颗粒均匀稳定，无彩色画面。
```

## 音频要求

35mm 胶片机运转低鸣、脚步声与远处城市环境声；无对白、无配乐。

## 参考资产

Image 1＝男孩面部身份锚点（ConsisID 官方示例输入图）

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/consisid/consisid_input.png?download=true> |

本地文件名见 [`../assets/assets.csv`](../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

10 秒黑白胶片街拍，面部身份与参考图一致，微表情与颗粒稳定。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：面部身份保持（与参考图逐帧对比）；微表情自然度；黑白胶片颗粒一致性

## 硬失败规则

- 面部身份明显漂移（换脸感）
- 五官扭曲
- 颗粒闪烁
- 出现彩色画面

## 资产准备

下载 ConsisID 官方示例输入图，评测前确认人脸清晰可辨（半身或全身更佳）。本机网络无法直连 huggingface.co 时，可用镜像 https://hf-mirror.com/datasets/huggingface/documentation-images/resolve/main/diffusers/consisid/consisid_input.png 获取同一文件。

## 改编说明

复用 ConsisID 官方 README 的原图与英文 Prompt，中文执行版补充音轨与验收口径。

## 来源与权利

- 来源：ConsisID 官方仓库 README 示例
- 来源页面：<https://github.com/PKU-YuanGroup/ConsisID>
- 复用方式：`public_example_identity_reference`
- 权利状态：ConsisID 仓库 Apache-2.0；示例图来自 HuggingFace documentation-images 数据集，权利随该数据集条款；人物肖像仅作内部评测候选

## 原文（source_prompt_original，仅供对照）

```text
The video captures a boy walking along a city street, filmed in black and white on a classic 35mm camera. His expression is thoughtful, his brow slightly furrowed as if he's lost in contemplation. The film grain adds a textured, timeless quality to the image, evoking a sense of nostalgia. Around him, the cityscape is filled with vintage buildings, cobblestone sidewalks, and softly blurred figures passing by, their outlines faint and indistinct. Streetlights cast a gentle glow, while shadows play across the boy's path, adding depth to the scene. The lighting highlights the boy's subtle smile, hinting at a fleeting moment of curiosity. The overall cinematic atmosphere, complete with classic film still aesthetics and dramatic contrasts, gives the scene an evocative and introspective feel.
```
