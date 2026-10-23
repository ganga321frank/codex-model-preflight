# v0.1.0 — Early preview / 试用预览版

**Codex Model Preflight gives a brief model, reasoning-effort, and speed recommendation before substantial work.**

**大任务开工前，给你一次简短、有依据的模型与推理档位建议。**

## Included / 这版有什么

- Three task classes: Simple, Routine, Complex. One starting configuration, a reason, and an escalation condition.
- One selection pause per unassessed substantial task; accepted settings, continuations, minor follow-ups, and an explicit no-pause preference are respected.
- A dated model guide with official sources; capability-tier advice when exact models are unavailable.
- English and Chinese documentation, 12 public reference cases, MIT license, install/remove instructions, and two labeled 30-second illustrative walkthroughs.
- A friend trial ZIP: open a ready-made project in Codex, try a fictional CSV task, and return optional feedback. No global model configuration change is required.

## What was checked / 已核查

Local manual and Skills CLI installation, installed-file hashes, native Codex skill discovery, named-skill removal, internal documentation links, archive contents, and all demo frames. The Chinese guides were rendered in WPS and visually reviewed.

Public installation from `ganga321frank/codex-model-preflight` was verified on 2026-10-23 using Skills CLI 1.7.4 in an isolated Windows project. All four installed files match source after line-ending normalization. This machine needed its existing system proxy for Git access; no global settings were changed.

The removal guide includes an observed Skills CLI 1.7.4 shared-directory edge case. Exact evidence and limits are in [validation.md](validation.md).

## Known limits / 已知边界

This is an instruction-only advisor. It does not switch the active model or open a native popup. Automatic matching and pause behavior depend on the client and model. Fresh-chat behavioral reliability and real allowance savings have not been established. The 12 cases are reference judgments, not 12 executed model tests or an accuracy score.

技能只给方向，不保证最优或固定额度节省。先用低风险示例观察是否提示、继续后是否反复暂停、建议是否易懂。无需发送完整业务资料。

## Feedback / 希望你帮忙看

1. Could you install or open the trial project without help?
2. Did it offer useful advice before the work, then stay quiet on ordinary follow-ups?
3. If you stopped using it, what made it unhelpful?

首轮目标为 10 位自愿试用者；尚未取得外部留存结果。请用 Issue 模板或试用包中的反馈表提交脱敏例子。
