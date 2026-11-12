---
case_id: "HARD-ST-02"
package: "困难包"
modality: "REF2VA"
input_modality: "文本＋参考视频"
subtask: "困难样本／细节稳定·光照迁移"
business_scenario: "影视后期重新布光"
difficulty: "5"
difficulty_category: "伪影／闪烁／细节稳定"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Day-to-Night Relighting"
reuse_type: "public_multimodal_example_adapted"
---

# HARD-ST-02 · 困难样本／细节稳定·光照迁移

困难包 / REF2VA / 文本＋参考视频 · 10 秒 · 16:9 · 难度 5/5 · 困难类别：伪影／闪烁／细节稳定

## 提示词（中文执行版）

```text
将 Input Video 1 的光照从白天改为夜晚：保持人物身份、动作、场景布局与镜头完全一致，仅改变光照——加入暖色室内灯光与窗外冷蓝夜色，人物受光方向与新光源一致，阴影随光改变。除光照外所有细节保持稳定，边缘无抠像光晕。
```

## 音频要求

保留原视频音频，可轻微叠加夜晚环境声（虫鸣／灯电流声）；无配乐。

## 参考资产

Input Video 1＝待重新布光的原视频

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Input Video 1 | 模型输入·视频 | video | <https://v3b.fal.media/files/b/0aa44040/emXiHyqHBI1Go4GG7gKxc_3-3-2-2_in1.mp4> |
| 2 | - | 官方示例输出（仅参考，不输入） | video | <https://v3b.fal.media/files/b/0aa44040/BXGIUDLgWrr4qZ5ZmbaMW_out37_3-3-2.mp4> |

本地文件名见 [`../assets/assets.csv`](../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

白天转夜晚的重打光版本，身份、动作、布局不变，仅光照与阴影改变。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：光照转换自然度；身份与动作稳定；非光照区域保持；阴影一致性

## 硬失败规则

- 人物身份漂移
- 动作改变
- 除光照外场景布局变化
- 边缘抠像光晕穿帮

## 资产准备

下载 Input Video 1；不上传示例输出视频。

## 改编说明

复用 fal 官方示例输入视频与原提示（一句话原题），中文执行版补全稳定性验收口径。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Day-to-Night Relighting
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Change the lighting in the reference video from daytime to night.
```
