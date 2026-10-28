# Validation status / 验证说明

## v0.2.0 update on 2026-10-28

This update changes interaction instructions, not runtime code. The checks below do not establish automatic discovery or reliable behavior across every client.

- The public skill and project trigger were reviewed together against the old forced-selection pause. Personal rules were updated separately on the maintainer's machine; the public installer does not overwrite other users' personal instructions.
- Skill Creator frontmatter/name validation passed for the public skill. Relative Markdown links resolve locally. All 18 authored cases were reviewed as reference expectations; they are not 18 model executions.
- A manual installation into a fresh isolated project copied all four runtime files and matched the source hashes. Skill-only and friend-trial ZIP contents match those same files, and ZIP CRC checks passed.
- Skills CLI 1.7.4 installed the updated public GitHub repository into a fresh isolated Windows project using the documented skill name, Codex target, and --copy. All four runtime files match the committed source after line-ending normalization. This verifies one remote install, not implicit triggering or model decisions.
- Updated illustrative assets still say they are not a live recording. The model mapping remains dated 2026-10-22; it is not claimed to have been refreshed by this interaction change.
- No fresh-chat model execution, one-minute wake-up, automatic switch, latency benchmark, or allowance-saving benchmark is claimed for this update. The six new cases are reference scenarios, not six completed inference tests.
- Old project-level instructions or already-loaded conversations may still request a pause. Inspect overlapping rules and start a new chat to try the updated policy; restart the client if the updated skill is not detected.

## Historical v0.1.0 checks

The remainder records checks for the previously published version; it does not validate the changed v0.2.0 behavior.

Package: **0.1.0**, assembled 2026-10-22–23. Model guide checked on 2026-10-22. Windows 11; Codex CLI **0.163.0-alpha.11**; Skills CLI **1.7.4**.

## Checks actually performed

| Check | Result and meaning |
| --- | --- |
| Skill Creator frontmatter/name validation | Passed with Python UTF-8 mode. This validates structure, not advice quality. |
| Manual project installation | Copied the skill folder to an isolated project's `.agents/skills/`; file hashes match the package. |
| Native Codex discovery | The installed client's `skills/list` interface returned `codex-model-preflight`, enabled, with repository scope and the expected description. No inference request was sent. |
| Skills CLI project install/list/remove | Installed the local repository source with `--copy`, compared every installed file hash, and listed the skill for Codex. Codex-only removal reported success but retained the shared folder; removing this one named skill without an agent filter cleared it. No global install or model configuration change. |
| Public examples | All 12 cases reviewed against the authored policy for task class, pause, continuation, and capability boundaries. These are manual reference cases, not 12 model executions. |
| Local documentation and package | Relative Markdown links, public text for known private identifiers, expected skill files, and unchanged private-source hashes checked. This is a targeted publication check, not a general security audit. |
| Demo assets | Six frames per language, 30,000 ms total duration; reviewed every frame. Clearly labeled illustrative workflow, not a live recording. |
| Word companion | Exported with installed WPS Office; all three resulting pages visually reviewed. |
| Public GitHub publication | Published to `ganga321frank/codex-model-preflight` on 2026-10-23. All 30 initial remote files match the local committed Git blob hashes. |
| Public remote installation | Skills CLI 1.7.4 installed from `ganga321frank/codex-model-preflight` into an isolated project's `.agents/skills/` for Codex with `--copy`. All four installed files match source after line-ending normalization. The command used this machine's existing system proxy for network access; no global Git or model settings were changed. |
| Skills directory page | The public skills.sh detail URL returned HTTP 200 with the expected title, installation command and SKILL.md content on 2026-10-23. Its First Seen field reads Today. The install count is not yet shown; this is not evidence of ranking, adoption, or retention. |

The instruction-only runtime package contains SKILL.md, agents/openai.yaml, references/model-guide.md, and LICENSE. Promotional assets and public cases do not need to be read for each recommendation. UTF-8 is intentional; on older Windows Python installations use `python -X utf8` for text validation tools.

## What has not been established

- No fresh-chat model execution test of explicit/implicit triggering, pause-once reliability, or advice quality across clients. Native discovery is not evidence that every matching task triggers.
- No controlled model-quality, latency, token, subscription-allowance, or cost benchmark. No proof of an advantage over a well-written self-generated skill.
- The remote installation check covered one Windows project and one Skills CLI version. It does not establish compatibility across every client, platform, or network.
- No external testers recruited and no one-week retention results. The launch kit provides the invitation text and feedback questions for that next step.

## Reproduce and extend

Follow [install.md](install.md), first in a project you can discard. Use [cases.md](cases.md) to check behavior in new chats; establish the listed prior state for continuation cases. Record actual outputs and client/model settings, including cases that fail. Do not turn a checklist into an accuracy percentage.

正式对外表述可以说“本地安装、卸载、原生技能发现与公开仓库安装已验证”，不能写成“自动触发百分之百稳定”“12项模型实测全通过”或“已经验证节省额度”。真实新聊天交互仍需进一步验证。
