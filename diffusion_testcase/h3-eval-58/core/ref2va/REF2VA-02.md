---
case_id: "REF2VA-02"
package: "核心包"
modality: "REF2VA"
input_modality: "文本＋参考图×5"
subtask: "风格参考／动态图形与音乐"
business_scenario: "动画剧集片头"
difficulty: "5"
difficulty_category: "-"
duration_seconds: "15"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Retro Anime Crime Title Sequence"
reuse_type: "public_multimodal_example_adapted"
---

# REF2VA-02 · 风格参考／动态图形与音乐

核心包 / REF2VA / 文本＋参考图×5 · 15 秒 · 16:9 · 难度 5/5

## 提示词（中文执行版）

```text
以 Image 1–5 为人物剪影、道具、构图和色彩参考，制作 15 秒 16:9 复古日式犯罪悬疑动画片头。使用硬边剪影、漫画拼贴、非对称分屏、几何色块、英文演职员名与少量片假名。0–2 秒线稿与分屏出现，3–6 秒色块和人物剪影按节拍组接，6–10 秒唱片圆形擦除、红线切片与字母遮罩交替，10–13 秒短萨克斯／铜管段落，最后 2 秒定格。字幕仅使用清晰英文，角色与姓名各出现一次；禁止柔和溶解与流体变形。
```

## 音频要求

原创 15 秒黑色爵士片头曲，60% 悬疑＋40% 爵士；低频 drone、拨弦、冷合成器、低 kick、刷子、walking bass、短萨克斯与铜管；不得模仿现成旋律。

## 参考资产

Image 1–5＝人物、道具、构图与色彩风格参考

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/inkR-ds2tkM6eE2RarDjP_3-1-2-1_ref1.webp> |
| 2 | Image 2 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/4fBkydkxYMHR5xoyRhy4L_3-1-2-1_ref2.webp> |
| 3 | Image 3 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/mW88KCKWIujkO8k9Y4doH_3-1-2-1_ref3.webp> |
| 4 | Image 4 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/yf9YnuxGEvq21Q1smOcCp_3-1-2-1_ref4.webp> |
| 5 | Image 5 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/Ea_-Q8dhPNoJDFpEDXm0L_3-1-2-1_ref5.webp> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

生成结果正确使用全部指定参考，目标动作、编辑与声音符合提示，未指定部分保持稳定。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：多图风格吸收；转场类型；英文文字；音乐节拍与定格

## 硬失败规则

- 出现中文或乱码字幕
- 同一姓名重复
- 使用柔和溶解
- 音乐变成欢快流行曲
- 参考人物完全不可辨

## 资产准备

按条目链接下载原始输入媒体；保持 Image／Video／Audio 编号与上传顺序一致；不上传示例输出视频。

## 改编说明

原网页说明多数提示词为摘录；中文版本依据可见资产补齐音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Retro Anime Crime Title Sequence
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Create a 15-second, 16:9 opening-title sequence for a stylish crime mystery. Draw from retro Japanese animation titles, hard-edged silhouettes, comic-book collage, asymmetric split screens, bold geometric color fields, English credit typography, sparse katakana accents, and a noir-jazz sensibility. Aim for 60% suspense and 40% jazz: mysterious, cool, agile, and urban—never horror, heavy drama, or a cheerful jazz music video.
Build the sequence as motion-graphics collage: linework appears over black, split-screen boundaries snap into place, then color blocks and frames assemble piece by piece. Character silhouettes, prop close-ups, and English credits slide, pop, and reveal through masks on the beat. Keep it designed and graphic, not like conventional narrative animation.
Credits must be clean and legible. Animate thin frames drawing on, names sliding in, letters appearing one at a time, or color blocks revealing type, then hold briefly. Do not introduce Chinese text, garbled characters, or misspellings. Each role and each name appears once only; do not assign multiple roles to the same name.
Vary the transitions: circular vinyl-record wipes, vertical car-door cuts, long character shadows wiping frame, red-line slices, oversized letter masks, split-screen reconfigurations, hard color-block cuts, and tiled frames snapping into place. Keep every transition crisp, rhythmic, suspenseful, and collage-driven. No soft dissolves or fluid morphs.
BGM: an original 15-second title cue, 60% suspense and 40% jazz. Use a low drone, tense string pizzicato, cool synth pulses, low kick, sparse brushwork, fragments of walking bass, short baritone-sax phrases, and clipped brass accents. Build suspense with low frequencies and hi-hat in the first 2 seconds; bring in the low beat at 3 seconds, jazz-bass movement at 6 seconds, and a short sax/brass riff at 10 seconds. Freeze the final 2 seconds on a tense chord and drum hit. Keep it mysterious and criminally cool, never upbeat, and do not imitate an existing melody.
```
