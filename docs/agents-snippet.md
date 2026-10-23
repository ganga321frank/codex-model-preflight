# Optional project trigger / 可选项目触发规则

Merge **one** language version below into the target project's existing `AGENTS.md`; do not replace the rest of the file. Install the skill first. This is an instruction, not a guaranteed event hook. Users who prefer explicit invocation can skip it.

## English

```markdown
<!-- codex-model-preflight:start -->
Before a new substantial task, use $codex-model-preflight to recommend a model, reasoning effort, and speed. Pause once before substantive work unless settings are already chosen/accepted or I ask not to pause. Skip minor follow-ups and accepted continuations; “continue” accepts execution without proving a model switch.
<!-- codex-model-preflight:end -->
```

## 简体中文

```markdown
<!-- codex-model-preflight:start -->
独立大任务开始前调用 $codex-model-preflight，推荐模型、推理档位与速度，并在实质执行前暂停一次；本任务已选定或接受设置、或我要求不要暂停时直接继续。普通追问和已接受的继续执行不重复分档；“继续”不代表模型切换已验证。
<!-- codex-model-preflight:end -->
```

If another model-selection skill or rule already applies, choose one policy for the target project and remove or adapt overlapping instructions yourself. The public package does not overwrite existing personal rules. To remove this behavior later, delete only your added marked block.
