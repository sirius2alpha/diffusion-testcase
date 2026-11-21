---
case_id: "FL2VA-05"
package: "核心包"
modality: "FL2VA"
input_modality: "文本＋首帧图＋尾帧图"
subtask: "动作补全／动态运镜"
business_scenario: "黏土动画电影"
difficulty: "5"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Claymation Lava Canyon Leap"
reuse_type: "derived_frames_from_public_output"
---

# FL2VA-05 · 动作补全／动态运镜

核心包 / FL2VA / 文本＋首帧图＋尾帧图 · 10 秒 · 16:9 · 难度 5/5

## 提示词（中文执行版）

```text
黏土动画风格。狐狸从首帧姿态加速冲向悬崖并起跳，以慢动作跨越熔岩峡谷；空中镜头从狐狸腹部下方向前穿过，展示峡谷深度和完全伸展的黏土身体，最后落到派生尾帧位置。狐狸造型、体积和材质全程一致。
```

## 音频要求

奔跑脚步、起跳风声、熔岩低鸣与热浪噼啪；空中音乐仅保留低音持续音，无对白。

## 参考资产

Image 1＝首帧；公开输出视频最后一张解码帧＝派生尾帧

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·首帧 | image | <https://v3b.fal.media/files/b/0aa44041/aEXwD7DJ5_a0_T6zvbx-R_3-1-6-1_ref1.webp> |
| 2 | - | 派生尾帧的来源输出（不直接输入） | video | <https://v3b.fal.media/files/b/0aa44040/yZZhju7Tf9BtoB-MGrQeo_out20_3-1-6.mp4> |

尾帧需从上方第 2 条官方输出视频提取最后一帧得到（该视频本身不作为模型输入）；取帧命令见 [`../../docs/how-to-run.md`](../../docs/how-to-run.md)。

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

从规定首帧自然过渡到规定尾帧，端点保真且中间动作、声音满足提示。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：首尾姿态；跑—跳—落动作链；镜头穿越；黏土体积与身份

## 硬失败规则

- 狐狸中途变形／消失
- 没有起跳或落地
- 镜头穿模导致主体不可见
- 熔岩音效完全缺失

## 资产准备

保留现成首帧；下载公开输出视频并提取最后一张解码帧作为尾帧；记录源 URL 与帧号，两图统一尺寸和纵横比。

## 改编说明

原网页说明多数提示词为摘录；中文版本补充音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Claymation Lava Canyon Leap
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`derived_frames_from_public_output`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Claymation. A fox sprints to the edge of a cliff and launches without hesitation, making a dramatic heroic leap in slow motion over an immense lava canyon. Midair, the camera races beneath the fox’s belly in a bold dynamic move, revealing the terrifying depth of the chasm and the fully extended motion of its clay body.
```
