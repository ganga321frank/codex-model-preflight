---
name: codex-model-preflight
description: Recommend a model, reasoning effort, and speed before a new substantial Codex task or an explicit model-choice request. Pause once for selection; skip minor follow-ups and accepted continuations.
---

# Codex Model Preflight

Give a practical starting point, not an optimality or savings claim. Use the user's language. This skill advises; it cannot switch the current model.

## When to run

Run before a new multi-step deliverable, batch file job, investigation, or feature build. Do this before broad scans, research, edits, or delegation. A few essential samples are enough to establish scope. Also run when explicitly asked for model advice.

Skip short ordinary questions, tiny edits, status checks, and follow-ups within an already assessed task. A genuinely new outcome or a material increase in reasoning difficulty can justify reassessment; a wording change cannot.

## Choose a starting point

Classify the current stage, not the project's prestige or file count:

| Class | Signals | Starting capability |
| --- | --- | --- |
| Simple | Explicit rules, repeatable extraction or conversion, easy checks | Efficient model, Low or Medium effort |
| Routine | Several coordinated steps, familiar analysis or implementation, clear acceptance criteria | Balanced model, Medium effort |
| Complex | Cross-source dependencies, conflicting evidence, difficult debugging or consequential design choices | Balanced model, High effort; flagship only for the difficult judgment |

Choose one configuration. Read [model-guide.md](references/model-guide.md) for the dated model mapping; reuse it within the task. If the mapping is stale, the user rules out those models, or availability is unknown, name the capability tier instead of inventing an available model or asking for a complete model list. Briefly qualify named suggestions with “if available” when needed. No model catalog, default config, or intuition proves the active settings.

Default speed: Standard, where supported. Higher reasoning does not imply faster execution. Do not default to Max or Ultra. Do not recommend paid speed upgrades without an explicit latency need; explain the usage tradeoff if recommending one. Missing evidence, broken tools, and unclear inputs need correction, not merely a stronger model. Keep required domain skills and verification.

## Keep the recommendation short

Use three short lines, normally under 80 English words or 120 Chinese characters, plus a selection sentence when pausing:

> Routine · GPT-6.1 Sol / Medium / Standard, if available.
> Why: a bounded feature with clear requirements and ordinary tests.
> Escalate if: conflicting requirements or a difficult root cause emerges.

Class labels and exact wording may vary. Give a direction, not a menu or a report. Do not scan unrelated files, query account usage, research models, or launch agents just to classify. Consult current official documentation only when a specific model uncertainty actually changes the advice.

## Pause once, then respect the choice

For an unassessed substantial task, recommend and stop before substantive execution: “Choose the suggested settings, then reply ‘continue’, or say ‘continue with current settings’.” Do not treat silence as acceptance. This is a selection step, not a request to authorize work already requested.

If the user has already chosen or accepted settings for this task, continue without another gate. “Continue”, “继续”, or “按当前设置继续” accepts execution; it does not prove a switch happened. An explicit “don't pause”, “直接做”, or advice-only preference means give the recommendation briefly and proceed. Remember that preference within the conversation; do not modify global settings to persist it.

For a standalone model-advice question, answer without demanding a continuation. After acceptance, reassess only for a new outcome or a material difficulty change. Never claim “switched”, alter global configuration, or invoke another model as a workaround. Model selection remains with the user.
