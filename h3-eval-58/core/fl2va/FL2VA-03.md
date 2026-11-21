---
case_id: "FL2VA-03"
package: "核心包"
modality: "FL2VA"
input_modality: "文本＋首帧图＋尾帧图"
subtask: "UI 状态变化／文字保持"
business_scenario: "汽车官网动效"
difficulty: "3"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Automotive Website UI Animation"
reuse_type: "derived_frames_from_public_output"
---

# FL2VA-03 · UI 状态变化／文字保持

核心包 / FL2VA / 文本＋首帧图＋尾帧图 · 10 秒 · 16:9 · 难度 3/5

## 提示词（中文执行版）

```text
首帧和尾帧均为同一汽车网页界面。顶部标题向下滑入到位，下方文案面板向上滑入，汽车车灯由暗变红，其他导航、车身和背景保持不动。运动路径简洁，最终精确到达尾帧 UI 状态，不新增页面元素。
```

## 音频要求

轻微界面滑动声与一次车灯点亮电子音；无配乐、无对白。

## 参考资产

Image 1＝首帧；公开输出视频最后一张解码帧＝派生尾帧

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·首帧 | image | <https://v3b.fal.media/files/b/0aa44050/6h9GMfzActy_L4IyAiMZA_3-1-5-3_ref1.webp> |
| 2 | - | 派生尾帧的来源输出（不直接输入） | video | <https://v3b.fal.media/files/b/0aa44040/Fu_Rn7NeWKY9_B7aZVyK7_out18_3-1-5.mp4> |

尾帧需从上方第 2 条官方输出视频提取最后一帧得到（该视频本身不作为模型输入）；取帧命令见 [`../../docs/how-to-run.md`](../../docs/how-to-run.md)。

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

从规定首帧自然过渡到规定尾帧，端点保真且中间动作、声音满足提示。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：UI 元素轨迹；文字逐字保持；非目标区域稳定；车灯状态与音效

## 硬失败规则

- 标题或文案出现错字
- 汽车整体变形
- 车灯未变红
- 新增导航／按钮导致末帧不一致

## 资产准备

保留现成首帧；下载公开输出视频并提取最后一张解码帧作为尾帧；记录源 URL 与帧号，两图统一尺寸和纵横比。

## 改编说明

原网页说明多数提示词为摘录；中文版本补充音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Automotive Website UI Animation
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`derived_frames_from_public_output`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Animate the website UI: the top headline slides down into place, the copy panel below slides up, and the car’s lights shift from dark to red.
```
