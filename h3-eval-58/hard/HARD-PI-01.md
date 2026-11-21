---
case_id: "HARD-PI-01"
package: "困难包"
modality: "REF2VA"
input_modality: "文本＋参考图"
subtask: "困难样本／人＋商品·座椅演示"
business_scenario: "电商产品视频"
difficulty: "5"
difficulty_category: "人＋商品互动"
duration_seconds: "15"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Ergonomic Chair Product Film"
reuse_type: "public_multimodal_example_adapted"
---

# HARD-PI-01 · 困难样本／人＋商品·座椅演示

困难包 / REF2VA / 文本＋参考图 · 15 秒 · 16:9 · 难度 5/5 · 困难类别：人＋商品互动

## 提示词（中文执行版）

```text
以 Image 2 的椅子为精确商品、Image 1 为功能细节参考，生成 15 秒 16:9 产品片：0–4 秒 360 度环绕展示黑色人体工学椅；4–8 秒真人演示——一位设计师坐上去，双手调节扶手高度与座椅升降，后仰展示腰托贴合；8–12 秒宏观特写网布透气结构与腰托曲线；12–15 秒该设计师舒适办公并定格文字“WHERE INSPIRATION MEETS COMFORT.”。人物与椅子有真实坐、调、靠互动，椅子结构全程不变形、不换款。
```

## 音频要求

座椅调节机械声、网布摩擦声、办公室环境声；无对白、无配乐。

## 参考资产

Image 1＝功能细节（网布、腰托、扶手）；Image 2＝商品主体（椅子）

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/odbQKz3gGNeCvoiXJ6_a__3-1-4-2_ref1.webp> |
| 2 | Image 2 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44050/8EI5Tk2n5OQz4x9EjYIyL_3-1-4-2_ref2.webp> |
| 3 | - | 官方示例输出（仅参考，不输入） | video | <https://v3b.fal.media/files/b/0aa4404f/4Ux9W7hLE1vWD5E6dSKN9_out15_3-1-4.mp4> |

本地文件名见 [`../assets/assets.csv`](../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

15 秒产品片，真人完成坐—调—靠互动，椅子保真，结尾文字逐字正确。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：商品保真；人—椅互动（坐／调／靠）；目标文字逐字；360 展示结构稳定

## 硬失败规则

- 椅子变形／换款
- 人物仅同框无互动
- 结尾文字错拼、漏字或乱码
- 360 展示中结构漂移

## 资产准备

下载两张参考图，核对编号与上传顺序；不上传示例输出视频。

## 改编说明

复用 fal 官方示例与原提示（含结尾文字）；中文执行版把“展示专业人士”落为可验收的坐—调—靠动作。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Ergonomic Chair Product Film
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Present a black Herman Miller ergonomic chair in a premium office with a full 360-degree product reveal. Cut to macro views of the breathable mesh back with airflow visualization, an engineering animation of the lumbar support and ergonomic curve, and demonstrations of multidirectional armrest and seat-height adjustment. Show designers, developers, and creative professionals working comfortably over long sessions. Include a 3D skeletal-support visualization that communicates all-day comfort, plus refined interior styling. End with the line: “WHERE INSPIRATION MEETS COMFORT.” Keep the direction minimal, cool-toned, professional, futuristic, and slow-paced. Use Image 1 for feature details and Image 2 for the product.
```
