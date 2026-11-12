---
case_id: "FL2VA-02"
package: "核心包"
modality: "FL2VA"
input_modality: "文本＋首帧图＋尾帧图"
subtask: "风格转场／版式保持"
business_scenario: "展览海报动态化"
difficulty: "3"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "3:4"
source: "fal MiniMax H3 Prompting Guide — Animated Gallery Poster"
reuse_type: "derived_frames_from_public_output"
---

# FL2VA-02 · 风格转场／版式保持

核心包 / FL2VA / 文本＋首帧图＋尾帧图 · 10 秒 · 3:4 · 难度 3/5

## 提示词（中文执行版）

```text
将 Image 1 的艺术海报动化为一个连续运动海报，保留白色画廊边框、内框、红白黑配色、3D 收藏玩具质感和原始排版。仅让人物与装饰元素轻微动作，文字逐字出现，最终准确收束到派生尾帧，不改变边框尺寸和文字布局。
```

## 音频要求

每次文字出现都有轻巧打字音；细微纸面摩擦声；无对白、无背景音乐。

## 参考资产

Image 1＝首帧；公开输出视频最后一张解码帧＝派生尾帧

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·首帧 | image | <https://v3b.fal.media/files/b/0aa44050/2YmEFl1sdPM3TaBDW8rvP_3-1-2-6_ref1.webp> |
| 2 | - | 派生尾帧的来源输出（不直接输入） | video | <https://v3b.fal.media/files/b/0aa44040/Wp9YVJ44sbUaDHP4yqeEM_out10_3-1-2.mp4> |

尾帧需从上方第 2 条官方输出视频提取最后一帧得到（该视频本身不作为模型输入）；取帧命令见 [`../../docs/how-to-run.md`](../../docs/how-to-run.md)。

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

从规定首帧自然过渡到规定尾帧，端点保真且中间动作、声音满足提示。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：端点版式一致；文字与边框稳定；3D 材质；打字音与文字出现同步

## 硬失败规则

- 白框或内框消失
- 文字乱码／位置漂移
- 海报被改成实拍场景
- 末帧版式不一致

## 资产准备

保留现成首帧；下载公开输出视频并提取最后一张解码帧作为尾帧；记录源 URL 与帧号，两图统一尺寸和纵横比。

## 改编说明

原网页说明多数提示词为摘录；中文版本补充音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Animated Gallery Poster
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`derived_frames_from_public_output`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Animate the source artwork as a motion poster while preserving its white gallery border, inner frame, red/white/black palette, 3D collectible-figure look, and original layout. Add a light, playful type-on sound whenever text appears.
```
