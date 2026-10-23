# Behavior contract / 使用约定

| Situation / 情况 | Expected behavior / 预期 |
| --- | --- |
| New substantial task, no setting selected / 新大任务，未选档 | Three-line advice, one selection pause before substantive work / 三行建议，执行前暂停一次 |
| Settings already accepted for this task / 本任务已选定 | Continue; no repeated gate / 继续，不再拦截 |
| “Continue” / “继续” | Accept execution; never assert a verified switch / 接受执行，不声称切换已验证 |
| “Continue with current settings” / “按当前设置继续” | Respect the choice, even if advice differed / 尊重选择 |
| “Don't pause” / “不要暂停，直接做” | Brief advice and proceed; retain within this conversation / 简短提示后执行，本对话沿用 |
| Minor revision, question, status check / 小改、追问、查进度 | Skip preflight / 不重新分档 |
| Explicit advice-only question / 单独问选型 | Answer the question, no request to continue / 回答建议，不要求继续 |
| New distinct deliverable or genuinely harder problem / 新成果或实质难点 | May reassess the changed scope / 可针对变化重评 |
| Unknown or unavailable model / 型号未知或不可用 | Suggest capability tier and effort; do not invent availability / 推荐能力等级，不编造可用型号 |
| Missing source or tool failure / 缺资料、工具故障 | Fix the input/tool problem; no automatic escalation / 先处理输入或工具问题 |

An initial recommendation should name a single usable starting point, not list every model. A large deterministic batch can be Simple; a short contradictory question can be Complex. Error consequences affect verification and may affect judgment needs, but do not automatically imply the highest model.

This is an instruction policy, not a deterministic UI hook. No native popup, active-setting inspection API, automatic switch, or background monitoring is provided. The AGENTS snippet improves instruction visibility but is not a guarantee. Explicit user preferences and higher-priority host instructions still apply.

“继续”只表示允许按已有任务继续，不证明用户切换了模型。不要把分档暂停与工作授权混为一谈。模型升级也不能替代领域技能、来源核验与必要测试。
