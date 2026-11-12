---
case_id: "FL2VA-01"
package: "核心包"
modality: "FL2VA"
input_modality: "文本＋首帧图＋尾帧图"
subtask: "场景转换／多镜头叙事"
business_scenario: "科幻预告片"
difficulty: "5"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Epic Space Opera Teaser"
reuse_type: "derived_frames_from_public_output"
---

# FL2VA-01 · 场景转换／多镜头叙事

核心包 / FL2VA / 文本＋首帧图＋尾帧图 · 10 秒 · 16:9 · 难度 5/5

## 提示词（中文执行版）

```text
以 Image 1 为精确首帧，以派生尾帧为结束画面，制作史诗太空歌剧预告。指挥舱震动、白炽闪光和跃迁冲击依次增强；标题从深空阴影中浮现，字距逐渐展开，最后定格到尾帧构图。允许快速硬切，但首尾主体、色调与标题风格保持统一。
```

## 音频要求

低频引擎轰鸣、舱体金属震动、短促警报与跃迁重音；标题锁定时一次克制低音冲击；无对白。

## 参考资产

Image 1＝首帧；公开输出视频最后一张解码帧＝派生尾帧

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·首帧 | image | <https://v3b.fal.media/files/b/0aa44041/67cRsNFSSXnWYh3A2WUEP_3-1-1-2_ref1.webp> |
| 2 | - | 派生尾帧的来源输出（不直接输入） | video | <https://v3b.fal.media/files/b/0aa44040/oOe4kafjDQ3eYqK-TRwyE_out01_3-1-1.mp4> |

尾帧需从上方第 2 条官方输出视频提取最后一帧得到（该视频本身不作为模型输入）；取帧命令见 [`../../docs/how-to-run.md`](../../docs/how-to-run.md)。

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

从规定首帧自然过渡到规定尾帧，端点保真且中间动作、声音满足提示。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：首尾帧保真；多镜头节奏；标题可读性；跃迁视觉与重音同步

## 硬失败规则

- 首帧主体被替换
- 末帧未到达
- 标题乱码
- 跃迁画面与重音明显错位

## 资产准备

保留现成首帧；下载公开输出视频并提取最后一张解码帧作为尾帧；记录源 URL 与帧号，两图统一尺寸和纵横比。

## 改编说明

原网页说明多数提示词为摘录；中文版本补充音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Epic Space Opera Teaser
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`derived_frames_from_public_output`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Epic theatrical space-opera teaser
Keep the pace fast and the scale enormous without letting the edit drag. Use sharp hard cuts, a shaking command deck, white-hot flashes, split-second black frames, and a violent jump-to-warp impact. Title cards should use wide-tracked cinematic typography—not pure white—with restrained material texture, subtle illumination, and a faint edge glow. Animate the titles by emerging from deep-space shadow, catching a sweep of starlight, opening their letter spacing, leaving a slight afterimage, and flashing briefly against black.
```
