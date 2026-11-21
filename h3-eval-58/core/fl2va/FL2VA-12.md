---
case_id: "FL2VA-12"
package: "核心包"
modality: "FL2VA"
input_modality: "文本＋首帧图＋尾帧图"
subtask: "空间转换／连续后拉运镜"
business_scenario: "艺术电影／梦境视觉"
difficulty: "5"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "ComfyUI 官方 MiniMax H3 Max FLF2V 工作流"
reuse_type: "original_frame_pair_prompt_time_compressed"
---

# FL2VA-12 · 空间转换／连续后拉运镜

核心包 / FL2VA / 文本＋首帧图＋尾帧图 · 10 秒 · 16:9 · 难度 5/5

## 提示词（中文执行版）

```text
以 dream_face_first 为首帧、dream_face_last 为尾帧，压缩为 10 秒连续梦境镜头。0–4 秒深蓝单色的巨大投影脸随呼吸明暗变化，镜头后拉并揭示卧室与床边人物；4–7 秒墙面如纸向内卷曲，巨脸缩成悬浮发光面具；7–10 秒空间继续收缩，面具映入瞳孔并收束到尾帧极端眼部特写。全片蓝色单色、电影质感、无切镜、无文字。
```

## 音频要求

低频 drone 与水下闷混响；空间卷曲时纸张拉伸声；接近瞳孔时心跳增强，结尾所有声音抽离，仅留轻微耳鸣。

## 参考资产

首帧＝巨脸梦境；尾帧＝极端眼部特写

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·首帧 | image | <https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/dream_face_first.png> |
| 2 | Image 2 | 模型输入·尾帧 | image | <https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/dream_face_last.png> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

10 秒连续后拉梦境变换，声音随空间收束，准确到达眼部尾帧。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：首尾端点；连续后拉；空间折叠逻辑；单色与音轨收束

## 硬失败规则

- 出现切镜／字幕
- 尾帧构图错误
- 人物脸部严重崩坏
- 结尾声音未按要求抽离

## 资产准备

直接下载 Comfy 官方两张输入图。

## 改编说明

原工作流 Prompt 含两个 8 秒段；为 H3 单段时长上限压缩为 10 秒，原文保留在 source_prompt_original。

## 来源与权利

- 来源：ComfyUI 官方 MiniMax H3 Max FLF2V 工作流
- 来源页面：<https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_max_flf2v.json>
- 复用方式：`original_frame_pair_prompt_time_compressed`
- 权利状态：Comfy workflow_templates 仓库 MIT；媒体保留来源，公开再分发前核对资产声明

## 原文（source_prompt_original，仅供对照）

```text
[Segment 1]
Style: dream physics, deep-blue monochrome with a misty diffusion in the glow, shadows keeping faint layers instead of pure black, spatial scale distortion, photoreal texture.
Action: [0s-1.5s] The projected face breathes with light shifts, dust drifting, his silhouette still; [1.5s-4s] The camera pulls back slowly and the giant face shrinks with it, revealing that this colossal face floats on the wall of a vast bedroom: a projection inside a dream-room, his silhouette standing at the bedside looking up; [4s-8s] The camera keeps pulling back past the room's boundary as the walls curl inward like paper, folding into the darkness of a second dream layer, the giant face shrinking with the curling walls into a floating glowing mask suspended in the void, the man motionless and looking up throughout, the frame ending with the mask hovering directly above him. No text. Camera: one continuous pull-back, slight warping as the space folds, no cuts. Audio: a low drone wrapped in an underwater-feeling muted reverb, paper-like stretching as the space curls, one distant bell.

[Segment 2]
Style: same dreamy haze, the blue one shade darker, a deeper dream layer.
Action: [0s-2s] The glowing mask rotates slowly above him; he raises a hand, and the instant his fingertips near it the whole space collapses in scale: the mask becomes a reflection inside a pupil, his body edge receding into silhouette; [2s-5s] The viewpoint reveals itself as his eye all along: the frame wavers slightly, we have been looking through his pupil, the blue iris texture rings into view at the frame's edge; [5s-8s] The giant face in the pupil breathes once with light, the dream begins to dissolve: the image tears slightly like a bad signal, the reflection flickers twice, locking finally on the extreme eye close-up, a deeper blue surfacing slowly in the depths of the iris. No text. Camera: an objective view snapping into pupil-POV, the switch made through a slight signal-tear, no cuts. Audio: a heartbeat approaching to become the main beat, one falling bass note as the mask shrinks, signal noise through the tear, every sound sucked away on the last beat leaving a faint ringing in the ears.

[Shared]
Dreamy haze over the blue monochrome, faint layers in the shadows, photoreal texture, spatial scale distorting with each dream layer. Negative: no water ripples, no third-person frontal face, no color shift away from the blue monochrome, no text overlays, no subtitles, no dissolve transitions, no extra light sources, no logo.
```
