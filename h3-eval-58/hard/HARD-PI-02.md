---
case_id: "HARD-PI-02"
package: "困难包"
modality: "REF2VA"
input_modality: "文本＋参考图"
subtask: "困难样本／人＋商品·装备改装"
business_scenario: "游戏买量广告"
difficulty: "5"
difficulty_category: "人＋商品互动"
duration_seconds: "15"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Interactive Game Equipment UI"
reuse_type: "public_multimodal_example_adapted"
---

# HARD-PI-02 · 困难样本／人＋商品·装备改装

困难包 / REF2VA / 文本＋参考图 · 15 秒 · 16:9 · 难度 5/5 · 困难类别：人＋商品互动

## 提示词（中文执行版）

```text
保留原示例时间轴：0–2 秒俯视，角色坐在高饱和紫色地板上抬头看向镜头，右侧游戏菜单显示 START NEW GAME / CONTINUE（高亮）/ SETTINGS / EXIT GAME，左上玩家名 MINIMAX，光标选择 CONTINUE；2–4 秒推近右臂，RIGHT ARM EQUIPMENT 面板滑入，选中 PHANTOM GRIP 后切换到 CHRONOS CLAW，机械手重组、青色 LED 变亮；4–7 秒弧形移到左侧，ARMAMENT CUSTOMIZATION 网格中左臂逐段拆解换装；7–8.5 秒拉远中景，CONFIRM CONFIG 闪烁确认，UI 收起；8.5–10 秒底部 LOADING 从 0% 走到 100%；10–15 秒角色起身，赛博朋克街景加载完成，第三人称跟随，HUD（小地图、血条弹药、任务标记）淡入。所有 UI 文字逐字正确，角色与装备面板有真实操作互动。
```

## 音频要求

UI 点击与滑入音效、机械重组声、加载完成提示音；无对白、无配乐。

## 参考资产

Image 1＝角色形象；Image 2＝UI 风格

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/by_ntirI8-pvXjlgZpYJm_3-1-5-1_ref1.webp> |
| 2 | Image 2 | 模型输入·图片 | image | <https://v3b.fal.media/files/b/0aa44041/R0fu1SE7WXXXijPApQqrA_3-1-5-1_ref2.webp> |
| 3 | - | 官方示例输出（仅参考，不输入） | video | <https://v3b.fal.media/files/b/0aa4404f/E8DY7sjVYIu5qaxWapQOn_out16_3-1-5.mp4> |

本地文件名见 [`../assets/assets.csv`](../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

15 秒装备改装演示，UI 文字全部逐字正确，机械手重组可见，时间轴事件齐全。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：人—装备交互；UI 文字逐字保真；时间轴遵循；HUD 元素齐全

## 硬失败规则

- 任一 UI 目标词（START NEW GAME、CONTINUE、SETTINGS、EXIT GAME、MINIMAX、PHANTOM GRIP、CHRONOS CLAW、CONFIRM CONFIG、LOADING）错拼／缺失／乱码
- 机械手重组缺失
- 时间轴事件顺序错误

## 资产准备

下载两张参考图，核对编号与上传顺序；不上传示例输出视频。

## 改编说明

复用 fal 官方示例完整分段时间轴；同时覆盖人＋商品互动与文字保真两个困难维度。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Interactive Game Equipment UI
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`public_multimodal_example_adapted`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
Use Image 1 for the character and Image 2 for the UI style.
[0–2 seconds] High-angle overhead shot. The character sits on a vivid, highly saturated purple floor, looks up at camera, and matches Image 1. A game menu appears on the right: START NEW GAME, CONTINUE (highlighted), SETTINGS, EXIT GAME. Player profile MINIMAX appears top left. The cursor selects CONTINUE.
[2–4 seconds] Smoothly push in to her right arm. A RIGHT ARM EQUIPMENT panel slides in from the right. PHANTOM GRIP is selected, then the selection moves to CHRONOS CLAW. Her mechanical hand reconfigures: fingers separate, new claw-like joints lock into place, and cyan LEDs flare brighter.
[4–7 seconds] Arc smoothly to her left. An ARMAMENT CUSTOMIZATION grid slides in, showing hand, forearm, elbow, and upper-arm components. The selector cycles rapidly. Her left arm disassembles section by section: the forearm plate releases, new armor slides in, the elbow joint swaps, and the hand reconfigures, with exposed wiring and pistons visible during the change.
[7–8.5 seconds] Pull back to a medium shot. CONFIRM CONFIG flashes; click it. All UI panels collapse inward and vanish. She uncrosses her legs and settles into a relaxed seated pose with one knee raised, lifting the prosthetic hand for a subtle post-configuration movement.
[8.5–10 seconds] A LOADING bar appears along the bottom and races from 0% to 100%. The saturated purple environment darkens as shadows creep inward and warm golden light begins to bleed through.
[10–15 seconds] As she stands, the full world loads around her: a dense cyberpunk slum with flickering neon, rain-wet streets, moving crowds, passing motorcycles, tangled overhead cables, and stacked buildings stretching toward futuristic towers. Settle into a third-person camera behind her. HUD elements fade in: minimap top right, health and ammo bottom left, then a mission marker. She steps into the street.
```
