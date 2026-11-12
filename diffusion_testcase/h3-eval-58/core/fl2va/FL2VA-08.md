---
case_id: "FL2VA-08"
package: "核心包"
modality: "FL2VA"
input_modality: "文本＋首帧图＋尾帧图"
subtask: "状态变化／双人身份连续"
business_scenario: "舞台魔术短剧"
difficulty: "5"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Precision Costume Swap"
reuse_type: "derived_frames_from_public_output"
---

# FL2VA-08 · 状态变化／双人身份连续

核心包 / FL2VA / 文本＋首帧图＋尾帧图 · 10 秒 · 16:9 · 难度 5/5

## 提示词（中文执行版）

```text
两位魔术师面向观众站在舞台上，同时挥杖并释放烟雾。烟雾散去时，左侧魔术师改穿白色西装，右侧改穿黑色西装；两人的脸、手套颜色和相对位置不变。随后两人鞠躬，红幕合拢并逐渐变为深蓝，最后匹配派生尾帧。
```

## 音频要求

挥杖破风声、烟雾低鸣、观众短促惊叹和鞠躬后的掌声；幕布变化时一次柔和低音；无对白。

## 参考资产

Image 1＝首帧；公开输出视频最后一张解码帧＝派生尾帧

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·首帧 | image | <https://v3b.fal.media/files/b/0aa44041/jfwzo1TKVVkBwF4lcVdGH_3-3-4-3_ref1.webp> |
| 2 | - | 派生尾帧的来源输出（不直接输入） | video | <https://v3b.fal.media/files/b/0aa44040/_nJgGSvJXSs74YAza9vVr_out42_3-3-4.mp4> |

尾帧需从上方第 2 条官方输出视频提取最后一帧得到（该视频本身不作为模型输入）；取帧命令见 [`../../docs/how-to-run.md`](../../docs/how-to-run.md)。

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

从规定首帧自然过渡到规定尾帧，端点保真且中间动作、声音满足提示。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：双人身份与左右绑定；服装颜色交换；手套不变；幕布颜色过渡

## 硬失败规则

- 两人身份互换或脸部改变
- 服装未交换
- 手套颜色改变
- 左侧穿黑／右侧穿白

## 资产准备

保留现成首帧；下载公开输出视频并提取最后一张解码帧作为尾帧；记录源 URL 与帧号，两图统一尺寸和纵横比。

## 改编说明

原网页说明多数提示词为摘录；中文版本补充音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Precision Costume Swap
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`derived_frames_from_public_output`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Two magicians stand onstage facing the audience and perform a “swap” illusion. They wave their wands simultaneously and smoke rises. When it clears, their suit colors have exchanged: the magician on the left now wears white, and the one on the right now wears black. Their glove colors do not change. They bow; the red curtain closes behind them and gradually shifts from deep red to dark blue.
```
