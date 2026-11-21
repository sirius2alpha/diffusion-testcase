# 来源与权利

本包所有条目均来自公开可访问页面或公开代码仓，但**公开可访问不等于可自由再分发**。
下表是逐条溯源的结果；`cases/<id>.md` 与 `cases.csv` 中每条用例也各自记录了
`source_name` / `reuse_type` / `rights_status`。

| 来源 | URL | 用于条目 | 权利说明 |
| --- | --- | --- | --- |
| VBench | https://github.com/Vchitect/VBench | 核心 T2VA-01～04；困难 HARD-FH-02～03、HARD-ST-01 | Apache-2.0（VBench 仓库）；保留出处、许可与修改说明 |
| T2V-CompBench | https://github.com/KaiyueSun98/T2V-CompBench | 核心 T2VA-04～08；困难 HARD-HS-01～02、HARD-MP-01 | 未发现仓库级 LICENSE；仅链接原题，正式再分发前需确认授权 |
| TAVGBench | https://huggingface.co/datasets/OpenNLPLab/TAVGBench | 核心 T2VA-09～10 | 数据集卡 Apache-2.0，仅复用文本；原 YouTube 音视频权利不随文本许可转移 |
| fal MiniMax H3 Prompting Guide | https://fal.ai/learn/devs/minimax-h3-prompting-guide | 核心 T2VA-11～12、FL2VA-01～09、REF2VA-01～12；困难 HARD-HS-03、MP-02～03、PI-01～03、CM-01～02、ST-02～03、TX-03 | 公开示例但未见单独媒体许可；仅作候选评测输入，公开再分发或商用前需取得权利确认 |
| Wan2.1 | https://github.com/Wan-Video/Wan2.1 | 核心 FL2VA-10 | 仓库 Apache-2.0；保留来源 |
| ComfyUI workflow_templates | https://github.com/Comfy-Org/workflow_templates | 核心 FL2VA-11～12 | 仓库 MIT；保留来源 |
| ConsisID | https://github.com/PKU-YuanGroup/ConsisID | 困难 HARD-FH-01 | 仓库 Apache-2.0；示例图权利随 HuggingFace documentation-images 数据集条款；人物肖像仅作内部评测候选 |
| EvoLink H3 Prompt 博客 | https://evolink.ai/minimax-h3-prompts | 困难 HARD-TX-01～02 | 第三方公开 Prompt，未见许可声明；仅复用文本并改写，发布前需取得作者授权 |
| 自设计 | — | 困难 HARD-HS-04、HARD-CM-03 | 自设计压力题，无外部媒体权利 |

## 使用边界

1. **仅内部技术评测**：含真实商标（REF2VA-11 的 Coca-Cola / FamilyMart、HARD-TX-03 的
   Nike 数字语言）与可识别人物肖像（HARD-FH-01、REF2VA-03）的条目，对外发布结果前需另做
   商标与肖像审核。
2. **媒体不随包分发**：仓库只保存 URL 与角色说明，不保存第三方图片／视频／音频文件，
   避免把不确定授权的媒体二次分发。需要离线资产时用 `assets/fetch_assets.py` 自行抓取。
3. **文本许可不覆盖媒体**：TAVGBench 等条目只复用文本标注，原 YouTube 媒体的权利不随之转移，
   因此这些条目不得引用原视频画面作为交付物。
4. **改写不等于原题**：`source_prompt_original` 是原题或摘录，中文执行版是统一改写版；
   对外引用时必须标注区分，不能把改写版称为官方原文。
