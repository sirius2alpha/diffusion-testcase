---
case_id: "FL2VA-06"
package: "核心包"
modality: "FL2VA"
input_modality: "文本＋首帧图＋尾帧图"
subtask: "第一人称运镜／动作音效"
business_scenario: "游戏过场与玩法演示"
difficulty: "5"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — First-Person Tactical Gameplay"
reuse_type: "derived_frames_from_public_output"
---

# FL2VA-06 · 第一人称运镜／动作音效

核心包 / FL2VA / 文本＋首帧图＋尾帧图 · 10 秒 · 16:9 · 难度 5/5

## 提示词（中文执行版）

```text
第一人称、眼平视角、手持现代战争 FPS 画面。玩家持枪沿基地道路缓慢推进，先左右检查通道，再短暂停步向远处目标射击数发，随后继续前进并到达尾帧。只有真实玩家式轻晃与射击后坐力，枪械结构、手部与基地透视稳定。
```

## 音频要求

脚步、装备摩擦、数发枪声及远处回声；枪声与每发枪口焰、后坐力同步；无背景音乐。

## 参考资产

Image 1＝首帧；公开输出视频最后一张解码帧＝派生尾帧

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·首帧 | image | <https://v3b.fal.media/files/b/0aa44041/FNR0bvaxq9bXDHMA_2U1i_3-1-6-4_ref1.webp> |
| 2 | - | 派生尾帧的来源输出（不直接输入） | video | <https://v3b.fal.media/files/b/0aa44040/WOJY_3DBYBZg86BpOEpf1_out23_3-1-6.mp4> |

尾帧需从上方第 2 条官方输出视频提取最后一帧得到（该视频本身不作为模型输入）；取帧命令见 [`../../docs/how-to-run.md`](../../docs/how-to-run.md)。

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

从规定首帧自然过渡到规定尾帧，端点保真且中间动作、声音满足提示。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：第一人称视角；枪械与手部；移动—停顿—射击—移动顺序；枪声同步

## 硬失败规则

- 变成第三人称
- 枪械或手部严重畸形
- 枪口焰／后坐力与枪声错位
- 未到尾帧位置

## 资产准备

保留现成首帧；下载公开输出视频并提取最后一张解码帧作为尾帧；记录源 URL 与帧号，两图统一尺寸和纵横比。

## 改编说明

原网页说明多数提示词为摘录；中文版本补充音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — First-Person Tactical Gameplay
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`derived_frames_from_public_output`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Camera: first-person, eye level, handheld gameplay. Simulate a player operating a modern-warfare FPS, holding an assault rifle and advancing slowly around the perimeter of a military base. Move forward along a road beside cover, sweep the reticle across the passage ahead, pause to fire several rounds at a distant target, then continue pushing forward like authentic player-controlled footage.
Lighting: cool natural light across a modern military base, mixed with smoke and firelight. Keep the image photoreal and crisp, with AAA-quality weapons, materials, dust, and battlefield haze.
Camera movement: subtle player-driven sway while moving; begin with a slow advance, make small checks left and right, add light recoil when firing, then continue forward steadily.
```
