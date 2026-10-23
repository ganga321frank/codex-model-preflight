# Model guide

Last checked: **2026-10-22**. Applies to Codex clients exposing these models and controls. Availability depends on account, client, workspace, and rollout. This is a maintained starting policy, not an official task-to-model benchmark.

| Capability | Named starting point, if available | Use |
| --- | --- | --- |
| Efficient | GPT-6 Luna · Low; Medium for modest coordination | Explicit extraction, conversion, repetitive scoped work |
| Balanced | GPT-6.1 Sol · Medium | Routine multi-step work and bounded features |
| Balanced, deeper reasoning | GPT-6.1 Sol · High | Cross-source checks, difficult implementation, linked constraints |
| Flagship, targeted | GPT-6 Astra · High | A specifically identified ambiguous judgment or difficult root cause; consider Extra High only when warranted |

These effort choices are this project's heuristics. Official guidance supports starting lighter and comparing results; it does not certify these four rows as optimal. Use the controls actually available. Unknown names: recommend Efficient, Balanced, or Flagship plus an effort direction, with no invented model ID or unsupported equivalence.

Default to **Standard** speed where offered. Reasoning effort and speed are separate controls. More reasoning can add latency and usage. Fast and Ultrafast can consume more allowance. Ultra reasoning can involve subagents; it is distinct from Ultrafast speed. This advisory skill does not launch agents or change controls.

## Official basis

- [Models](https://learn.chatgpt.com/docs/models): model roles, selection controls, availability, reasoning and Ultra behavior.
- [Model selection](https://learn.chatgpt.com/docs/model-selection): compare the same task and keep settings that meet the quality requirement.
- [Pricing and usage](https://learn.chatgpt.com/docs/pricing): usage depends on model, context, reasoning, tools, retrieval, and caching; raw tokens do not establish fixed quota savings.

## Updating this guide

On an official model or control change, verify these pages, update the date and affected rows, then review the public cases. Keep stable behavior in SKILL.md. Do not add prices, account limits, or new model names from memory. Publish corrections in CHANGELOG.md; no real-time update service is included.
