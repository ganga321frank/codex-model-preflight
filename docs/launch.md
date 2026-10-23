# Launch kit / 发布与试用材料

## Positioning

**English:** A brief, grounded model recommendation before a substantial Codex task.

**中文：** 大任务开始前，给你一次简短、有依据的模型与推理档位建议。

Ready-made rules, a dated guide, public cases, and clear install/remove steps save setup and review work. Users can build an equivalent skill themselves. We have not established a recommendation-quality advantage or percentage savings.

## 中文发布文案

标题：Codex 总开最高档？我做了一个开工前帮你选档的简约 Skill

我常常习惯性使用高档模型，所以做了 Codex Model Preflight：在独立大任务开始前，用三行文字给出模型、推理档位和速度建议，再等我选择。普通追问不重复打断，回复“继续”就继续，也可以明确要求不要暂停。

功能很小：不给“最优选型”的承诺，也不自动切换模型。仓库附了带日期的模型依据、12个公开行为案例和中英文安装说明。你可以自己让AI写一个；这份现成包希望帮你省去整理规则、处理反复确认和检查型号建议的麻烦。

现在想找10位Codex重度用户试用：是否容易装好？建议有没有用？暂停是否烦人？一周后还愿不愿意留下？欢迎用脱敏例子反馈。

项目：https://github.com/ganga321frank/codex-model-preflight

安装：`npx skills add ganga321frank/codex-model-preflight --skill codex-model-preflight -a codex --copy`

演示：https://github.com/ganga321frank/codex-model-preflight/blob/main/assets/demo-zh.gif

## 朋友转发短文案

我做了一个很小的 Codex 技能：大任务开始前，先给你一句模型和推理档位建议，选好后继续，普通追问尽量不打断。

你不用装依赖或改全局设置，下载朋友试用包，解压后用 Codex 打开其中的“Codex试用项目”就能尝试。里面有虚构数据和中文说明。帮我看看能不能顺利开始、建议看不看得懂、会不会重复暂停就好。

目前是试用预览版，只提供起步方向，不自动切换模型，也没有验证过固定的省额度比例。用完直接告诉我一处好用或不好用的地方即可。

朋友试用包：https://github.com/ganga321frank/codex-model-preflight/raw/refs/heads/main/downloads/codex-model-preflight-v0.1.0-friends.zip

## English launch copy

Title: A small Codex skill for choosing settings before the work starts

I built Codex Model Preflight after repeatedly defaulting to high-end settings. Before a substantial task, it suggests one model, reasoning effort, and speed, with a short reason and an escalation condition. It pauses once for a choice; accepted continuations and small follow-ups stay quiet. You can ask it not to pause.

It is an instruction-only skill, with a dated model guide and 12 public behavior cases. You can generate an equivalent yourself; this package aims to save the setup and review work. It does not switch models, promise an optimal choice, or claim a measured percentage saving.

I'm looking for 10 Codex users to try it and report setup friction, useful or poor recommendations, annoying pauses, and whether they keep it after a week.

Repository: https://github.com/ganga321frank/codex-model-preflight

Install: `npx skills add ganga321frank/codex-model-preflight --skill codex-model-preflight -a codex --copy`

Walkthrough: https://github.com/ganga321frank/codex-model-preflight/blob/main/assets/demo-en.gif

## 30-second storyboard / 30秒演示脚本

The GIF is an illustrative text workflow, not a live recording or executed feature demo. Both languages follow the same sequence:

| Time | Scene |
| --- | --- |
| 0–4.5s | User asks for a bounded CSV import feature. |
| 4.5–11s | Skill offers Routine / balanced Medium / Standard, a reason and one pause. |
| 11–15.5s | User manually chooses the suggested settings in the client. |
| 15.5–20s | User says “continue”. No claim of a verified switch. |
| 20–25s | Expected behavior: proceed with the original work without another selection question. |
| 25–30s | Small follow-up: no fresh preflight. |

## First ten testers / 首轮10人

Invite users through the posts you choose to publish; no outreach has been sent by this package. Record only voluntary feedback in your own notes; the skill has no feedback uploader. Try to include both desktop and CLI users, and people doing coding and file work.

Ask at setup: Could you install without help? Did explicit invocation work? Did a substantial task trigger with the snippet? Did continuing produce another gate?

Ask after one week: Still enabled? One useful recommendation? One poor one? Too many pauses? If removed, why?

Track stars, installation signals, and retention separately. Skills directory installation counts are not active-user or retention counts. Do not infer quota savings from raw token totals. If later comparing cost, include the preflight overhead, use matched tasks and quality checks, and distinguish input/cache/output and actual allowance changes.

The [Skills directory FAQ](https://skills.sh/docs/faq) says public skills appear through real installations reported by the CLI. This is not a separate manual submission or a guarantee of ranking. Verify one real remote install after publication, then let genuine user installs provide the signal; do not repeat installs to inflate counts.

## Maintainer release checklist / 维护者发布清单

- Choose the actual GitHub owner/repository; create the repository only when ready to publish.
- Upload repository contents, keep English and Chinese README links working, and use the MIT license included.
- Confirm the documented public install command and prepared posts use `ganga321frank/codex-model-preflight`.
- Add a short repository description and relevant topics such as codex, agent-skills, model-selection and developer-tools.
- Verify installation from the actual public GitHub URL; local install success does not prove a remote install.
- Tag v0.1.0 and attach the skill-only ZIP after that remote check. Do not label an unverified build as universally tested.
- Review validation status, disclose limits, and attach the clearly labeled walkthrough. Do not publish private project files or usage logs.
- Share a useful demonstration in relevant communities with their posting rules. Answer concrete installation and behavior issues first.
- Check official model/control changes when reported, update the guide and affected cases, then record the release. No real-time maintenance promise is made.
