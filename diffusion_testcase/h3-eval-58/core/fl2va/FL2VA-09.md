---
case_id: "FL2VA-09"
package: "核心包"
modality: "FL2VA"
input_modality: "文本＋首帧图＋尾帧图"
subtask: "场景转换／材质匹配转场"
business_scenario: "饮品广告／创意转场"
difficulty: "5"
difficulty_category: "-"
duration_seconds: "10"
aspect_ratio: "16:9"
source: "fal MiniMax H3 Prompting Guide — Macro Coffee-to-Fluid Transition"
reuse_type: "reference_pair_to_fl2va"
---

# FL2VA-09 · 场景转换／材质匹配转场

核心包 / FL2VA / 文本＋首帧图＋尾帧图 · 10 秒 · 16:9 · 难度 5/5

## 提示词（中文执行版）

```text
Image 1 是咖啡微距首帧，Image 2 是沙漠全景尾帧。镜头快速推向奶泡、可可颗粒和深色液面，让颗粒、气泡与涟漪充满画面；当可可纹理与沙丘脊线形状最接近时，无缝过渡为沙漠并继续前推，最后完整呈现 Image 2。保持真实微距摄影与浅景深，禁止撕裂、黑帧、硬切和明显合成缝。
```

## 音频要求

咖啡细微气泡与颗粒摩擦声逐渐转为沙漠风声；过渡点声音连续交叉变化；无配乐、无对白。

## 参考资产

Image 1＝首帧；Image 2＝尾帧；原输出视频不进入模型输入

| # | 编号 | 用途 | 类型 | URL |
| --- | --- | --- | --- | --- |
| 1 | Image 1 | 模型输入·首帧 | image | <https://v3b.fal.media/files/b/0aa44041/yY_1Z2tV6KJ2Inkaw6JgG_3-2-1-3_ref1.webp> |
| 2 | Image 2 | 模型输入·尾帧 | image | <https://v3b.fal.media/files/b/0aa44041/ED5VlEDLsGo3EG0AFZseb_3-2-1-3_ref2.webp> |
| 3 | - | 官方示例输出（仅参考，不输入） | video | <https://v3b.fal.media/files/b/0aa44040/q4z3z9AbtFRvj4I4VAMtl_out28_3-2-1.mp4> |

本地文件名见 [`../../assets/assets.csv`](../../assets/assets.csv)；在包根目录运行 `python assets/fetch_assets.py` 可一次抓取全部模型输入资产。

## 预期输出

从规定首帧自然过渡到规定尾帧，端点保真且中间动作、声音满足提示。

## 评测维度

- 公共维度：语义一致性；主体与背景时序一致性；运动自然度；画面质量；音画同步；音频清晰度；指令遵循
- 专项维度：首尾图保真；颗粒—沙丘形状匹配；单镜头连续；音轨平滑过渡

## 硬失败规则

- 出现硬切／黑帧
- 咖啡或沙漠任一端点被替换
- 过渡处明显双曝光接缝
- 声音突然断裂

## 资产准备

将原 REF2VA 的两张参考图改作首帧与尾帧；记录任务类型改变，不把原示例当成原生 FL2VA 配对。

## 改编说明

原网页说明多数提示词为摘录；中文版本补充音轨和验收约束。 本条由 REF2VA 双图示例改为 FL2VA，属于任务改造样本。

## 来源与权利

- 来源：fal MiniMax H3 Prompting Guide — Macro Coffee-to-Fluid Transition
- 来源页面：<https://fal.ai/learn/devs/minimax-h3-prompting-guide>
- 复用方式：`reference_pair_to_fl2va`
- 权利状态：公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认

## 原文（source_prompt_original，仅供对照）

```text
@Image 1: Push in rapidly toward the milk foam, cocoa particles, and dark liquid texture on the coffee until particles, bubbles, and ripples fill the frame. Keep the macro photography realistic, with extremely shallow depth of field and fine powder drifting through backlight. Let the surface feel suspended between granular sand and fluid.
At the exact moment when the cocoa particles, foam contours, and coffee swirl closely resemble the dune ridges, wind-carved textures, and airborne sand in @Image 2, transition seamlessly into the desert landscape. Continue pushing forward until the full dunes from @Image 2 are revealed.
No tearing, black frames, hard cuts, obvious VFX, or compositing seams. Keep it photoreal, quiet, and restrained—as though one granular material naturally expands from the microscopic coffee surface into a vast desert. One continuous shot with no visible edit.
```
