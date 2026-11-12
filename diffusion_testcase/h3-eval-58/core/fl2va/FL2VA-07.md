---
case_id: "FL2VA-07"
package: "核心包"
modality: "FL2VA"
input_modality: "文本＋首帧图＋尾帧图"
subtask: "人物表演／交互界面转换"
business_scenario: "互动剧情游戏"
difficulty: "4"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Interactive Otome Game Transition"
reuse_type: "original_frame_pair"
---

# FL2VA-07 · 人物表演／交互界面转换

核心包 / FL2VA / 文本＋首帧图＋尾帧图 · 10 秒 · 16:9 · 难度 4/5

## 提示词（中文执行版）

```text
Image 1 是精确首帧，Image 2 是精确尾帧。以精致中文乙女视觉小说界面呈现演出后台：从‘选择观看他的表演’自然过渡到‘Han Xu 听到女主角后露出感兴趣的反应’。对话框、选项和文案以细腻界面动效出现，人物表情从平静转为好奇，浪漫张力克制，最终严格匹配尾帧。
```

## 音频要求

轻微界面提示音、衣料摩擦与一声感兴趣的气息；中文台词若出现须与框内文字一致；无额外配乐。

## 参考资产

Image 1＝精确首帧；Image 2＝精确尾帧

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·首帧 | image | <https://v3b.fal.media/files/b/0aa44041/4bkWZpB19fqzRjD-qXbWG_3-1-6-5_ref1.webp> |
| 2 | Image 2 | 模型输入·尾帧 | image | <https://v3b.fal.media/files/b/0aa44041/2XtxMPH_4z3_Ci3Jos18T_3-1-6-5_ref2.webp> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

从规定首帧自然过渡到规定尾帧，端点保真且中间动作、声音满足提示。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：双端 UI 与人物身份；文字可读性；表情过渡；界面动效与提示音

## 硬失败规则

- 首帧或尾帧不是对应原图
- 人物换脸
- 中文乱码
- 选项和对话框任意漂移

## 资产准备

下载两张原图，核对宽高与纵横比一致；按 Image 1→首帧、Image 2→尾帧上传。

## 改编说明

原网页说明多数提示词为摘录；中文版本补充音轨和验收约束。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Interactive Otome Game Transition
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`original_frame_pair`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Interactive Otome Game
Use the first image as the exact opening frame and the second as the exact ending frame. Create a transition within a premium Chinese otome visual-novel interface, capturing an intimate backstage moment before and after a performance. Move naturally from “Choose to watch his performance” to “Han Xu reacts with intrigued interest after hearing the heroine.” Reveal UI copy, choices, and dialogue boxes with refined otome-game motion design. Keep transitions fluid and the romantic tension suggestive but restrained.
```
