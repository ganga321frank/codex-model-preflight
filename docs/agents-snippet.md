# Optional project trigger / 可选项目触发规则

Merge **one** language version below into the target project's existing `AGENTS.md`; do not replace the rest of the file. Install the skill first. This is an instruction, not a guaranteed event hook. Users who prefer explicit invocation can skip it.

## English

```markdown
<!-- codex-model-preflight:start -->
Before a new substantial task, use $codex-model-preflight to recommend a model, reasoning effort, and speed briefly, then continue the requested work in the same turn with current session settings. Do not wait for a model-selection reply unless I explicitly ask you to wait. Unknown active settings or a different recommendation alone do not block work. Skip minor follow-ups; do not claim a model switch or a one-minute automatic resume. Required permissions and critical missing inputs remain separate.
<!-- codex-model-preflight:end -->
```

## 简体中文

```markdown
<!-- codex-model-preflight:start -->
独立大任务开始前调用 $codex-model-preflight，简短推荐模型、推理档位与速度后，同一轮直接按当前会话配置执行原任务，默认不等选档回复；只有我明确要求“先等我选档”时才暂停。当前配置未知或与建议不同，本身不阻塞执行。普通追问不重复分档；不声称已切换或一分钟后自动唤醒。必要授权与关键资料缺失另按实际规则处理。
<!-- codex-model-preflight:end -->
```

If another model-selection skill or rule already applies, choose one policy for the target project and remove or adapt overlapping instructions yourself. The public package does not overwrite existing personal rules. To remove this behavior later, delete only your added marked block.
