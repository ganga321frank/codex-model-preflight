# Behavior contract / 使用约定

Since v0.2.0, model advice does not require a reply by default. / 自 v0.2.0 起，选档建议默认不再要求回复。

| Situation / 情况 | Expected behavior / 预期 |
| --- | --- |
| New substantial task, no setting selected / 新大任务，未选档 | Brief advice in a progress message, then do the task with current session settings in the same turn / 简短提示后，本轮直接按当前会话配置执行 |
| Active settings unknown or different from advice / 当前配置未知或与建议不同 | Continue; distinguish advice from actual settings, no invented switch / 继续，明确建议不代表实际配置，不虚构切换 |
| Settings already accepted / 本任务已选定 | Continue; no repeated gate / 继续，不再拦截 |
| “Continue” / “继续” | Resume the original task; never assert a verified switch / 继续原任务，不声称切换已验证 |
| “Don't pause” / “不要暂停，直接做” | Brief advice and proceed / 简短提示后执行 |
| “Wait for me to choose” / “先等我选档” | Pause once until the user resumes / 暂停一次，等用户明确继续 |
| “Continue after one minute if I don't reply” / “一分钟不回复就继续” | Explain that no reliable timer is supplied; continue now with current settings to avoid blocking, unless a literal/manual wait is explicitly required / 说明本包没有可靠计时，按当前配置直接继续；明确要求实际等待时尊重等待 |
| Minor revision, question, status check / 小改、追问、查进度 | Skip preflight / 不重新分档 |
| Explicit advice-only question / 单独问选型 | Answer without starting an unrequested task / 回答建议，不擅自启动执行 |
| New outcome or genuinely harder problem / 新成果或实质难点 | May reassess; advice alone does not create a pause / 可重评，不因建议自动停工 |
| Missing critical input or required permission / 缺关键资料或必要授权 | Retain the actual boundary; time or silence is not approval / 只等待真正必要的信息或授权，超时或沉默不等于同意 |

The original user request supplies the task scope. The non-blocking default does not authorize new actions or prove consent to different model settings. A large deterministic batch can be Simple; a short contradictory question can be Complex. Model upgrades never replace source checks or required tests.

**Current session is different from system default.** The client may have an override. Do not read a configuration file and claim it proves the running model, change defaults, or create another agent to imitate an automatic switch. 本技能只推荐，不修改模型、推理档位或速度。

This is an instruction policy, not a deterministic UI hook. It supplies no native popup, model-setting API, durable timer, response listener, background monitoring, or automatic wake-up after a turn ends. One-minute automatic switching requires a separate host integration; see [interaction design](interaction.md). Explicit user choices and higher-priority host instructions still apply.
