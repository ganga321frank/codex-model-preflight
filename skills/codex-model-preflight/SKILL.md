---
name: codex-model-preflight
description: Recommend a model, reasoning effort, and speed before a new substantial Codex task or an explicit model-choice request. Continue with current session settings by default; pause for selection only when explicitly requested. Skip minor follow-ups.
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

Use three short lines, normally under 80 English words or 120 Chinese characters, plus a brief execution-status sentence when needed:

> Routine · GPT-6.1 Sol / Medium / Standard, if available.
> Why: a bounded feature with clear requirements and ordinary tests.
> Escalate if: conflicting requirements or a difficult root cause emerges.

Class labels and exact wording may vary. Give a direction, not a menu or a report. Do not scan unrelated files, query account usage, research models, or launch agents just to classify. Consult current official documentation only when a specific model uncertainty actually changes the advice.

## Recommend without blocking the task

For a substantial task the user has asked you to perform, give the recommendation in a progress message and continue the original task in the same turn using the current session settings. Do not end the turn, open an answer-required question, or ask for “continue” solely to select a model. The recommendation is advisory; this default is not an inference of consent from silence. Where useful, say: “Suggested: balanced / Medium / Standard. Continuing with this session's current settings; no switch performed.”

Continue even if the active model or reasoning effort cannot be verified, or appears different from the recommendation. Do not equate the recommendation or a global configuration default with the active session. Never claim a recommended tier is in effect merely because you are following its workflow. Do not modify global defaults, create a separate agent, or switch models as a workaround. If the current model actually cannot carry out a necessary step, explain that concrete limitation and continue independent work where possible.

If the user explicitly says “wait for me to choose”, “先等我选档”, or otherwise requires selection before work, recommend and pause once. Honor a user stop or pending choice; elapsed time alone never overrides it. “Continue”, “继续”, or “按当前设置继续” resumes the original task without another selection gate or an assertion that a switch happened. An explicit no-pause preference continues to apply within the conversation. Only a new outcome or material difficulty change justifies reassessment; it does not itself require a pause.

For an advice-only question, answer the question and stop normally. Do not start an unrequested implementation merely to avoid a pause. Required permissions, genuinely necessary missing inputs, and host safety checks remain separate from model advice; do not convert silence or a timeout into their approval.

## Requests to continue after one minute

This instruction-only skill provides no durable timer, response listener, model-selection control, or wake-up after a completed turn. Do not promise “I will resume in 60 seconds”, finish the turn hoping to wake later, sleep or poll solely for selection, or create recurring automation to emulate this behavior.

When the user wants a one-minute fallback to avoid stalled work, explain the limitation briefly and use the non-blocking default: continue now with the current session settings. If they explicitly require the actual timed wait or automatic switching, state that it needs a separate host integration; respect an explicit manual-wait requirement instead of silently substituting immediate execution. A real implementation would need a persistent deadline, reply/cancel handling, turn-state checks, and a supported model-setting interface. None is supplied by this package.
