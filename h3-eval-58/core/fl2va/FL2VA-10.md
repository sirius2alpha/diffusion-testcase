---
case_id: "FL2VA-10"
package: "核心包"
modality: "FL2VA"
input_modality: "文本＋首帧图＋尾帧图"
subtask: "动作补全／跟随运镜"
business_scenario: "CG 动画短片"
difficulty: "4"
difficulty_category: "-"
duration_seconds: "8"
aspect_ratio: "16:9"
source: "Wan2.1 官方 FLF2V 示例"
reuse_type: "original_frame_pair_and_prompt_audio_added"
---

# FL2VA-10 · 动作补全／跟随运镜

核心包 / FL2VA / 文本＋首帧图＋尾帧图 · 8 秒 · 16:9 · 难度 4/5

## 提示词（中文执行版）

```text
CG 动画，一只胸口有独特斑纹的蓝色小鸟从首帧地面振翅起飞，羽毛细节清晰。镜头从近景低角度跟随小鸟向上，蓝天、白云和阳光保持不变，最后到达尾帧飞行姿态。飞行动作有准备、振翅、升空三个阶段，不添加其他鸟类。
```

## 音频要求

振翅声由近到远、上升风声与明亮短促鸟鸣；无配乐、无对白。

## 参考资产

首帧＝地面小鸟；尾帧＝空中小鸟

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·首帧 | image | <https://raw.githubusercontent.com/Wan-Video/Wan2.1/main/examples/flf2v_input_first_frame.png> |
| 2 | Image 2 | 模型输入·尾帧 | image | <https://raw.githubusercontent.com/Wan-Video/Wan2.1/main/examples/flf2v_input_last_frame.png> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

蓝色小鸟从地面起飞至尾帧，跟随镜头与振翅声自然。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：首尾帧保真；振翅与升空；低角度跟随；鸟体结构

## 硬失败规则

- 小鸟颜色／胸口斑纹改变
- 没有升空
- 出现第二只鸟
- 镜头未跟随向上

## 资产准备

直接下载两张官方示例图并核对纵横比。

## 改编说明

保留官方英文原 Prompt，中文执行版补充音频与阶段约束。

## 来源与权利

- 来源：Wan2.1 官方 FLF2V 示例
- 来源页面：<https://github.com/Wan-Video/Wan2.1#run-first-last-frame-to-video-generation>
- 复用方式：`original_frame_pair_and_prompt_audio_added`
- 权利状态：Wan2.1 仓库 Apache-2.0；示例媒体保留来源，公开再分发前核对资产声明

## 原文（source_prompt_original，仅供对照）

```text
CG animation style, a small blue bird takes off from the ground, flapping its wings. The bird’s feathers are delicate, with a unique pattern on its chest. The background shows a blue sky with white clouds under bright sunshine. The camera follows the bird upward, capturing its flight and the vastness of the sky from a close-up, low-angle perspective.
```
