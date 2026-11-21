---
case_id: "FL2VA-04"
package: "核心包"
modality: "FL2VA"
input_modality: "文本＋首帧图＋尾帧图"
subtask: "产品展示／UI 动效"
business_scenario: "电商产品落地页"
difficulty: "3"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Rotating Product Page Reveal"
reuse_type: "derived_frames_from_public_output"
---

# FL2VA-04 · 产品展示／UI 动效

核心包 / FL2VA / 文本＋首帧图＋尾帧图 · 10 秒 · 16:9 · 难度 3/5

## 提示词（中文执行版）

```text
网页布局从上到下揭示，上方和中部文字向下滑入，下方文字向上滑入；中央产品出现后做小幅水平旋转，展示真实材质与结构，最后稳定到派生尾帧。除指定文字和产品外，其余 UI 不动。
```

## 音频要求

轻微产品旋转气流声与界面滑入声；无对白，简洁单次提示音结尾。

## 参考资产

Image 1＝首帧；公开输出视频最后一张解码帧＝派生尾帧

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·首帧 | image | <https://v3b.fal.media/files/b/0aa44041/RippnCb7kSS4Z2HdmcNIe_3-1-5-4_ref1.webp> |
| 2 | - | 派生尾帧的来源输出（不直接输入） | video | <https://v3b.fal.media/files/b/0aa44040/apUxRz30Q5zTJ47HJArTt_out19_3-1-5.mp4> |

尾帧需从上方第 2 条官方输出视频提取最后一帧得到（该视频本身不作为模型输入）；取帧命令见 [`../../docs/how-to-run.md`](../../docs/how-to-run.md)。

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

从规定首帧自然过渡到规定尾帧，端点保真且中间动作、声音满足提示。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：产品几何与材质；双向文字动效；端点构图；背景 UI 稳定

## 硬失败规则

- 产品旋转时结构崩坏
- 文字乱码
- 中央产品被替换
- 末帧未停止旋转

## 资产准备

保留现成首帧；下载公开输出视频并提取最后一张解码帧作为尾帧；记录源 URL 与帧号，两图统一尺寸和纵横比。

## 改编说明

原网页说明多数提示词为摘录；中文版本补充音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Rotating Product Page Reveal
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`derived_frames_from_public_output`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Reveal the layout from top to bottom. Upper and center typography slides down; lower typography slides up. Once the central product appears, let it rotate subtly.
```
