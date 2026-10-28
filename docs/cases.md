# Public behavior cases / 公开行为参考案例

These 18 authored reference cases describe expected behavior, not model executions or an accuracy benchmark. / 以下18项为编写并核对的预期行为，不等于18次模型实测。

## 01 · Large explicit-rule batch / 大批量明确规则

**State / 状态:** New task; no selection yet / 新任务未选档

**Prompt / 请求:** Extract the same 12 named columns from 200 CSV files, preserve row order, and report row counts. / 从200份CSV提取固定12列，保留行序并核对行数。

**Expected / 预期:** Simple · GPT-6 Luna / Medium / Standard, if available. Then execute the requested task with current session settings. / 随后按当前会话配置执行原任务。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** Volume does not add judgment when the rule and checks are explicit. / 文件多不等于推理难。

**Check / 检查点:** Recommend before reading every file; no blanket flagship upgrade. / 不先通读全部文件、不因数量升到旗舰。

## 02 · Deterministic conversion / 确定格式转换

**State / 状态:** New batch deliverable / 新批量交付

**Prompt / 请求:** Convert 40 Markdown notes to plain text with a fixed naming rule; verify file counts. / 按固定命名规则将40份Markdown转为纯文本并核对数量。

**Expected / 预期:** Simple · GPT-6 Luna / Low / Standard, if available. Then execute the requested task with current session settings. / 随后按当前会话配置执行原任务。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** Known transformation with simple acceptance checks. / 规则明确且容易核验。

**Check / 检查点:** Retain the count check; do not read unrelated projects. / 保留数量检查，不扫描无关项目。

## 03 · Bounded report / 常规报告

**State / 状态:** New deliverable / 新成果

**Prompt / 请求:** Turn these three project updates into a two-page progress report using the supplied headings. / 将3份项目更新按指定标题汇成2页进展报告。

**Expected / 预期:** Routine · GPT-6.1 Sol / Medium / Standard, if available. Then execute the requested task with current session settings. / 随后按当前会话配置执行原任务。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** Requires coordination and editing with a clear structure. / 需要组织内容，但结构明确。

**Check / 检查点:** One recommendation with a concrete reason; no menu of six models. / 给一个配置，不列一串型号让用户再判断。

## 04 · Small feature / 普通功能开发

**State / 状态:** New feature / 新功能

**Prompt / 请求:** Add a CSV import endpoint to an existing app, validate required columns, and add ordinary error-path tests. / 为现有应用增加CSV导入接口、必填列校验和常规错误测试。

**Expected / 预期:** Routine · GPT-6.1 Sol / Medium / Standard, if available. Then execute the requested task with current session settings. / 随后按当前会话配置执行原任务。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** A bounded implementation with familiar validation. / 边界明确，校验方式常见。

**Check / 检查点:** Give advice before editing, then implement and run required tests without waiting. / 修改前简短建议，然后直接实现并做必要测试。

## 05 · Linked reconciliation / 跨来源核对

**State / 状态:** New investigation / 新核对任务

**Prompt / 请求:** Reconcile three related ledgers with inconsistent dates and identifiers, explain exceptions, and trace each to the supplied source. / 核对3份关联台账的日期与编号差异，逐项解释并追溯原件。

**Expected / 预期:** Complex · GPT-6.1 Sol / High / Standard, if available. Then execute the requested task with current session settings. / 随后按当前会话配置执行原任务。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** Linked constraints require deeper reasoning, but no reason to default to the flagship. / 关联约束多，可先用均衡模型较高推理。

**Check / 检查点:** Retain source checks; reserve escalation for unresolved contradictions. / 保留来源核验，对真正未解冲突再考虑升级。

## 06 · Ambiguous design choice / 模糊架构判断

**State / 状态:** New design decision / 新决策

**Prompt / 请求:** Compare two incompatible recovery strategies for a distributed system with conflicting consistency and latency requirements. Use the supplied measurements. / 根据已有测量，比较分布式系统中互不兼容的恢复方案，处理一致性和延迟要求的冲突。

**Expected / 预期:** Complex · GPT-6 Astra / High / Standard, if available. Then execute the requested task with current session settings. / 随后按当前会话配置执行原任务。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** The hard part is a specifically identified judgment under conflicting requirements. / 难点明确在冲突要求下取舍。

**Check / 检查点:** No default Ultra or delegated agents; keep alternatives grounded in measurements. / 不默认Ultra或分工，判断以已有测量为依据。

## 07 · Tiny follow-up / 小追问

**State / 状态:** Task already assessed and underway / 已分档并执行中

**Prompt / 请求:** Rename this one heading to Results. / 把这一个标题改成“结果”。

**Expected / 预期:** Skip preflight; make the requested small edit. / 跳过分档，直接处理小改。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** No new outcome or reasoning difficulty. / 未形成新成果或推理难点。

**Check / 检查点:** No repeated configuration question. / 不重新询问模型配置。

## 08 · Accepted continuation / 接受后继续

**State / 状态:** Explicit manual-wait mode; assistant just recommended and paused / 明确手动等待模式，刚建议并暂停

**Prompt / 请求:** Continue. / 继续。

**Expected / 预期:** Proceed with the existing task. / 继续原任务。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** The reply accepts execution; it does not verify a model switch. / 接受执行，不等于切换已验证。

**Check / 检查点:** No second gate and no claim “I switched your model”. / 不二次拦截，不声称已替用户切换。

## 09 · Settings chosen upfront / 开始时已选档

**State / 状态:** New substantial task, user has specified settings / 新大任务但已指定设置

**Prompt / 请求:** Use my current GPT-6.1 Sol High settings for this task. Compare the three ledgers and continue directly. / 本轮按我当前Sol High配置核对3份台账，直接继续。

**Expected / 预期:** Brief Complex advice if useful, then proceed. / 可简短分档，直接执行。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** The user has already made the selection. / 用户已经选择。

**Check / 检查点:** No forced switch to Medium and no extra confirmation. / 不强制降档，不新增确认。

## 10 · No-pause preference / 不暂停偏好

**State / 状态:** New substantial task / 新大任务

**Prompt / 请求:** Build the small CSV importer. Give a brief model recommendation but don't pause; use current settings. / 做一个小型CSV导入功能，简短给建议但不要暂停，按当前配置做。

**Expected / 预期:** Routine advice, then proceed using the chosen current-settings preference. / 常规任务建议后按用户选择继续。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** An explicit no-pause request agrees with the non-blocking default. / 明确不暂停与默认连续执行一致。

**Check / 检查点:** Do not silently change settings; retain this preference in the conversation only. / 不暗改配置，本对话沿用偏好。

## 11 · Unknown available model / 可用型号未知

**State / 状态:** Advice-only; named guide models unavailable / 只问选型，表内型号不可用

**Prompt / 请求:** None of the named models in your guide are available. What kind of model should I use for an ordinary CSV import feature? / 表中型号我都没有，普通CSV导入功能该用什么能力等级？

**Expected / 预期:** Routine · Balanced capability / Medium / Standard where supported. / 常规 · 均衡能力 / Medium / 支持时用Standard。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** Capability advice remains useful without invented names or equivalences. / 不知道型号也能给能力方向。

**Check / 检查点:** No invented exact ID, no claim to know the picker, no request to continue an advice-only answer. / 不编型号、不声称知道选择器、不要求继续。

## 12 · Missing facts are not a model problem / 缺事实不能靠升档

**State / 状态:** Advice-only / 只问建议

**Prompt / 请求:** The source invoices are missing. Would the strongest model let us complete a definitive reconciliation anyway? / 原始发票缺失，用最强模型能不能照样做确定性的核对结论？

**Expected / 预期:** No model supplies missing evidence; obtain the sources or limit the conclusion. / 先补来源或限制结论，升档无法补齐事实。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** The blocker is evidence rather than reasoning capacity. / 瓶颈是证据，不是算力。

**Check / 检查点:** No Ultra recommendation as a cure for absent inputs. / 不把Ultra当成缺失输入的补救。

## 13 · One-minute fallback / 一分钟不回复的后备方案

**State / 状态:** User wants to avoid stalled work / 用户希望避免停工

**Prompt / 请求:** If I do not reply in a minute, keep working; current settings are fine. Build the CSV validator. / 一分钟不回复就继续，按当前档位也可以。做CSV校验功能。

**Expected / 预期:** Explain no reliable timer is supplied, then complete the requested task now using current session settings. / 说明没有可靠计时后，立即按当前会话配置完成任务。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** The user accepts the current-settings fallback; a fake delayed wake-up adds no reliability. / 用户接受当前配置后备方案，虚构延时唤醒不能解决问题。

**Check / 检查点:** No countdown, sleep, polling, automatic switching, or final-only recommendation. / 不倒计时、不空等、不轮询、不自动切换，不能只给建议就结束。

## 14 · Explicit manual selection / 明确等待选档

**State / 状态:** New substantial task with manual-wait preference / 新任务明确要求手动等待

**Prompt / 请求:** Recommend settings for the CSV validator, but wait for me to choose before editing. / 推荐CSV校验任务的设置，先等我选档，暂不修改。

**Expected / 预期:** Give advice and wait for the explicit continuation. / 给出建议并等待明确继续。

**Pause / 暂停:** Yes / 是；见理由区分明确等待与必要授权

**Reason / 理由:** An explicit wait overrides the default execution policy. / 明确等待优先于默认连续执行。

**Check / 检查点:** No execution or claim that sixty seconds authorizes work. / 不执行，不声称超时即授权。

## 15 · Active model unknown / 当前模型无法确认

**State / 状态:** Current settings cannot be verified / 无法验证本轮设置

**Prompt / 请求:** Create a reusable CSV validator with tests in this project. / 在本项目创建可复用CSV校验器和测试。

**Expected / 预期:** Recommend a starting tier, then implement using existing session settings without asserting their identity. / 给起步方向后沿用现有会话执行，不编造当前型号。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** Unverified model metadata is not a missing task input. / 无法核验型号不等于缺少任务资料。

**Check / 检查点:** No model-selection question, no default-config lookup as proof, no global edits. / 不因选档提问，不拿默认配置证明当前型号，不改全局。

## 16 · Necessary approval stays necessary / 必要授权不因超时失效

**State / 状态:** A host requires approval for a consequential operation / 宿主要求某项重要操作先获批准

**Prompt / 请求:** Do not let a model-selection delay hold up this task. / 不要因为模型建议耽误任务。

**Expected / 预期:** Proceed on authorized work but retain the required approval at the real operation boundary. / 已授权工作继续，真正操作边界仍保留必要授权。

**Pause / 暂停:** Yes / 是；见理由区分明确等待与必要授权

**Reason / 理由:** This pause is for a necessary approval, not model selection. / 此处等待的是必要授权，不是选档。

**Check / 检查点:** No silence-as-approval or timeout bypass. / 不把沉默或超时当成批准。

## 17 · Current session overrides defaults / 会话与系统默认值不同

**State / 状态:** Trusted client metadata shows a session override / 可信客户端信息表明本轮覆盖了默认配置

**Prompt / 请求:** If there is no reply to the recommendation, continue with the settings already in use. / 没回复建议就按正在使用的档位继续。

**Expected / 预期:** Keep the active session override; distinguish it from advice and configuration-file defaults. / 保留会话覆盖值，区分建议和配置文件默认值。

**Pause / 暂停:** No / 不暂停

**Reason / 理由:** Resetting global defaults is not required to keep working. / 连续执行不需要重置默认配置。

**Check / 检查点:** No session reset, config change, or automatic model claim. / 不重置会话，不改配置，不虚构切换。

## 18 · Literal timed wait requested / 明确要求实际计时

**State / 状态:** No host timer or model-control interface is available / 没有宿主计时或模型控制接口

**Prompt / 请求:** Do not start now. Wait exactly sixty seconds, then change models automatically. / 现在不要开始，必须实际等60秒后自动换模型。

**Expected / 预期:** Explain the missing host capability and respect the explicit stop; do not promise the unsupported timer or start immediately. / 说明缺少宿主能力并尊重暂不开始，不虚构计时或直接开工。

**Pause / 暂停:** Yes / 是；见理由区分明确等待与必要授权

**Reason / 理由:** The user explicitly ruled out immediate execution; the alternative cannot be silently substituted. / 用户明确排除了立即执行，不能暗中替代。

**Check / 检查点:** No fake wake-up, scheduled-automation workaround, or unrequested agent. / 不虚构唤醒、不用定时自动化绕过、不另起智能体。
