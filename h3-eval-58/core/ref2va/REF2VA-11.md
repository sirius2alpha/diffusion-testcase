---
case_id: "REF2VA-11"
package: "核心包"
modality: "REF2VA"
input_modality: "参考视频×1"
subtask: "多目标局部编辑／文字与台词"
business_scenario: "广告后期／多元素改稿"
difficulty: "5"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Product, Sign & Dialogue Replacement"
reuse_type: "public_multimodal_example_adapted"
---

# REF2VA-11 · 多目标局部编辑／文字与台词

核心包 / REF2VA / 参考视频×1 · 10 秒 · 16:9 · 难度 5/5

## 提示词（中文执行版）

```text
对 Video 1 做四处且仅四处编辑：开头的罐装饮料替换为 Coca-Cola；背景发光招牌‘FamilyMart’改为‘HUHUI’；结尾塑料袋中的所有零食替换为 Coca-Cola 罐；最后一句改为‘I bought a whole bunch of Coke.’ 其余人物、街道、镜头、光线和动作保持。所有招牌与包装文字清晰可读。
```

## 音频要求

最后英文台词逐字替换，其他对话和环境音保持；罐体碰撞声与动作一致；无新增配乐。

## 参考资产

Video 1＝待多目标局部编辑原视频

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Video 1 | 模型输入·视频 | video | <https://v3b.fal.media/files/b/0aa44040/hqcytT4Y13i26QE011efd_3-3-4-2_in1.mp4> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

生成结果正确使用全部指定参考，目标动作、编辑与声音符合提示，未指定部分保持稳定。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：四目标逐项完成；包装与招牌文字；非目标区域保持；新台词与口型

## 硬失败规则

- 任一目标漏改
- 招牌不是‘HUHUI’
- 袋中仍有零食
- 旧结尾台词残留
- 无关场景被重做

## 资产准备

按条目链接下载原始输入媒体；保持 Image／Video／Audio 编号与上传顺序一致；不上传示例输出视频。

## 改编说明

原网页说明多数提示词为摘录；中文版本依据可见资产补齐音轨和验收约束。 含真实商标，仅建议内部技术评测；公开发布前需另做商标与素材权利审核。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Product, Sign & Dialogue Replacement
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
In the reference video, replace the canned drink shown at the beginning with Coca-Cola. Change the illuminated “FamilyMart” convenience-store sign in the background to “HUHUI.” At the end, replace every snack in the plastic bag with cans of Coca-Cola, and change the final line from “I bought a few snacks” to “I bought a whole bunch of Coke.”
```
