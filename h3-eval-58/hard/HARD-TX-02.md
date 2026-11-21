---
case_id: "HARD-TX-02"
package: "困难包"
modality: "T2VA"
input_modality: "文本"
subtask: "困难样本／文字保真·动态字体"
business_scenario: "品牌片头与海报动画"
difficulty: "5"
difficulty_category: "文字生成与指定文字保真"
duration_seconds: "15"
aspect_ratio: "16:9"
source: "EvoLink — MiniMax H3 Prompts（Kinetic Quote Typography）"
reuse_type: "third_party_prompt_rewritten"
---

# HARD-TX-02 · 困难样本／文字保真·动态字体

困难包 / T2VA / 文本 · 15 秒 · 16:9 · 难度 5/5 · 困难类别：文字生成与指定文字保真

## 提示词（中文执行版）

```text
15 秒电影感动态字体动画，围绕 quote “Every great change begins quietly, grows through courage, and becomes impossible to ignore.” 逐短语揭示：0:00–0:03 “Every great change” 黑暗中逐词浮现；0:03–0:06 “begins quietly,” 手写感出现；0:06–0:09 “grows through courage,” 日出渐变中升起；0:09–0:12 “AND BECOMES” 编辑网格排版；0:12–0:14 “IMPOSSIBLE TO IGNORE” 冲击式定格；0:14–0:15 完整 quote 定格在米白背景，change／courage／impossible 以深红高亮。所有短语拼写完全准确。
```

## 音频要求

氛围音乐渐强、粒子与脉冲音效、结尾重音；无对白。

## 参考资产

无需输入资产（纯文本题）。

## 预期输出

15 秒动态字体动画，6 个短语按时间轴逐字出现，最终完整 quote 定格可读。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：每个短语逐字拼写；出现时序；定格帧可读性

## 硬失败规则

- 任一短语错拼／字母扭曲／重复字符
- 完整 quote 定格缺失
- 出现随机符号
- 文字随动画漂移错位

## 资产准备

无需资产

## 改编说明

第三方公开 Prompt 的摘录＋中文执行版；完整原文见来源页面。

## 来源与权利

- 来源：EvoLink — MiniMax H3 Prompts（Kinetic Quote Typography）
- 来源页面：<https://evolink.ai/minimax-h3-prompts>
- 复用方式：`third_party_prompt_rewritten`
- 权利状态：第三方博客公开 Prompt，未见许可声明；仅复用文本并改写为中文执行版，对外发布前需取得作者授权

## 原文（source_prompt_original，仅供对照）

```text
Create a 15-second cinematic text-animation video built around the quote: “Every great change begins quietly, grows through courage, and becomes impossible to ignore.” …（中略：0:00–0:03 “Every great change”、0:03–0:06 “begins quietly,”、0:06–0:09 “grows through courage,”、0:09–0:12 “AND BECOMES”、0:12–0:14 “IMPOSSIBLE TO IGNORE” 逐段动画描述）… 0:14–0:15 the complete quote appears centered on a clean off-white background … Avoid misspelled words, warped letters, duplicated characters, unreadable text, random symbols, excessive flickering, chaotic layouts, inconsistent fonts.
```
