---
case_id: "REF2VA-08"
package: "核心包"
modality: "REF2VA"
input_modality: "参考视频×1＋参考音频×1"
subtask: "参考音频音色／口型同步"
business_scenario: "数字人口播／角色配音"
difficulty: "5"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Voice Clone Dialogue Transfer"
reuse_type: "public_multimodal_example_adapted"
---

# REF2VA-08 · 参考音频音色／口型同步

核心包 / REF2VA / 参考视频×1＋参考音频×1 · 10 秒 · 16:9 · 难度 5/5

## 提示词（中文执行版）

```text
Video 1 提供角色外观、构图与表演视觉锚点；Audio 1 只作为目标音色和说话方式参考。让 Video 1 中角色说：‘Follow the wind, live free. Leave worries behind, enjoy the moment.’ 使用 Audio 1 的音色，保持原角色面部和身体稳定，嘴部开合、重音和停顿与英文台词一致，不添加第二个说话人。
```

## 音频要求

英文台词逐字清晰，音色接近 Audio 1；保留很轻的环境底噪；无背景音乐、无额外旁白。

## 参考资产

Video 1＝角色视觉锚点；Audio 1＝音色与说话方式

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Video 1 | 模型输入·视频 | video | <https://v3b.fal.media/files/b/0aa44040/7xUCBrPjNvvOvKNkzZ2_G_3-2-3-1_in2.mp4> |
| 2 | Audio 1 | 模型输入·音频 | audio | <https://v3b.fal.media/files/b/0aa44040/diYzSJTuTEdZH5cUmVB6u_3-2-3-1_in1.mp3> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

生成结果正确使用全部指定参考，目标动作、编辑与声音符合提示，未指定部分保持稳定。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：参考音色相似度；英文可懂度；唇形同步；角色视觉保持；无第二说话人

## 硬失败规则

- 使用完全不同音色且未参考 Audio 1
- 任一短句缺失
- 口型明显不对应
- 角色被替换或新增旁白

## 资产准备

按条目链接下载原始输入媒体；保持 Image／Video／Audio 编号与上传顺序一致；不上传示例输出视频。

## 改编说明

原网页说明多数提示词为摘录；中文版本依据可见资产补齐音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Voice Clone Dialogue Transfer
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
The character says: “Follow the wind, live free. Leave worries behind, enjoy the moment.” Match the voice in Audio 1.
```
