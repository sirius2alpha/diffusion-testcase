---
case_id: "HARD-TX-01"
package: "困难包"
modality: "T2VA"
input_modality: "文本"
subtask: "困难样本／文字保真·拼音教学"
business_scenario: "儿童教育内容"
difficulty: "5"
difficulty_category: "文字生成与指定文字保真"
duration_seconds: "15"
aspect_ratio: "16:9"
source: "EvoLink — MiniMax H3 Prompts（A-B-C-D Learning Animation）"
reuse_type: "third_party_prompt_rewritten"
---

# HARD-TX-01 · 困难样本／文字保真·拼音教学

困难包 / T2VA / 文本 · 15 秒 · 16:9 · 难度 5/5 · 困难类别：文字生成与指定文字保真

## 提示词（中文执行版）

```text
15 秒儿童拼音动画，教学闭环“字母→发音→物体→趣味动作→单词”重复四次：A（苹果）、B（球）、C（猫）、D（鸭）。每个字母先完整显示再 morph 成物体。屏幕文字逐字显示：Let's learn!、APPLE、BALL、CAT、DUCK、A B C D、Great job!；旁白按原 Prompt 逐句朗读。圆润 3D 角色、柔和 pastel 配色、干净排版。
```

## 音频要求

英文旁白逐句清晰，pop／crunch／meow／quack 音效与动作同步；无背景音乐。

## 参考资产

无需输入资产（纯文本题）。

## 预期输出

15 秒拼音动画，8 处目标文字全部逐字正确，旁白与文字同步，字母 morph 可理解。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：目标文字逐字（Let's learn!／APPLE／BALL／CAT／DUCK／A B C D／Great job!）；字母 morph 几何解释；旁白与文字同步

## 硬失败规则

- 任一目标词错拼／漏字／多字／乱码／文字融化
- 旁白与文字明显不同步
- 字母未完整显示即变形

## 资产准备

无需资产

## 改编说明

第三方公开 Prompt 的摘录＋中文执行版；完整原文见来源页面，评测前建议以原页面逐字核对目标文字清单。

## 来源与权利

- 来源：EvoLink — MiniMax H3 Prompts（A-B-C-D Learning Animation）
- 来源页面：<https://evolink.ai/minimax-h3-prompts>
- 复用方式：`third_party_prompt_rewritten`
- 权利状态：第三方博客公开 Prompt，未见许可声明；仅复用文本并改写为中文执行版，对外发布前需取得作者授权

## 原文（source_prompt_original，仅供对照）

```text
Create a 15-second animated educational video that teaches young children the letters A, B, C, and D. The learning pattern for every letter must be: LETTER → SOUND → OBJECT → PLAYFUL ACTION → OBJECT NAME. …（中略：A is for Apple / B is for Ball / C is for Cat / D is for Duck 四段逐秒脚本，含旁白 “A. A says ah. A is for Apple.” 等逐句引文与 recap 段）… Animation requirements: Keep each letter fully visible for a moment before it transforms. Show uppercase and lowercase versions clearly. … Maintain stable spelling, clean letterforms, accurate object shapes, and consistent character design.
```
