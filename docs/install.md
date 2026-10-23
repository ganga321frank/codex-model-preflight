# Install and remove / 安装与卸载

The skill is instruction-only. Install only `skills/codex-model-preflight/`, not the repository's docs or assets. Keep an existing personal model-selection skill unchanged; avoid enabling overlapping policies in the same project.

## Skills CLI

Download or clone this repository, open a terminal at its root, and run:

```sh
npx skills add . --skill codex-model-preflight -a codex --copy
```

The `.` is the local repository you just downloaded; no unpublished GitHub URL is needed. The installer may prompt or auto-detect Codex, so inspect its output. Start with project scope. `--copy` avoids requiring symbolic-link privileges on Windows. For intentional user-wide installation, add `-g`.

To install from the public repository, open a terminal in your target project and run:

```sh
npx skills add ganga321frank/codex-model-preflight --skill codex-model-preflight -a codex --copy
```

The third-party [Skills CLI](https://github.com/vercel-labs/skills) documents its own Node.js requirement and telemetry controls. The skill itself has no telemetry. Inspect the files and installer output before accepting changes.

## Manual install

OpenAI currently documents `.agents/skills` for project discovery and `~/.agents/skills` for user-wide discovery. See [Build skills](https://learn.chatgpt.com/docs/build-skills). Some clients also use or support legacy locations; inspect your client's discovered skill path rather than assuming every version shares one path.

For a project trial, copy the entire `skills/codex-model-preflight` folder into the target project's `.agents/skills/` directory:

```text
your-project/
  .agents/skills/codex-model-preflight/
    SKILL.md
    agents/openai.yaml
    references/model-guide.md
    LICENSE
```

Windows PowerShell, from the downloaded repository root; replace the target path with your project:

```powershell
$projectTarget = 'C:\path\to\your-project'
$skillTarget = Join-Path $projectTarget '.agents\skills\codex-model-preflight'
if (Test-Path -LiteralPath $skillTarget) { throw 'Skill already exists; inspect it before updating.' }
New-Item -ItemType Directory -Path $skillTarget -Force | Out-Null
Copy-Item -LiteralPath '.\skills\codex-model-preflight\SKILL.md' -Destination $skillTarget
Copy-Item -LiteralPath '.\skills\codex-model-preflight\LICENSE' -Destination $skillTarget
Copy-Item -LiteralPath '.\skills\codex-model-preflight\agents' -Destination $skillTarget -Recurse
Copy-Item -LiteralPath '.\skills\codex-model-preflight\references' -Destination $skillTarget -Recurse
```

No global settings need changing. For a more consistent project-level instruction, merge one [AGENTS snippet](agents-snippet.md) into the existing project `AGENTS.md`. Installation alone does not enforce a pre-task pause.

## Check the installation

1. Open a new Codex chat in the target project; restart Codex if the skill does not appear.
2. Find `codex-model-preflight` in the skill selector or mention `$codex-model-preflight`.
3. Ask it to build a small CSV import feature with validation and tests. Expect Routine / balanced Medium / Standard, a reason, and one pause before work.
4. Reply “continue with current settings”. Expect execution without another selection gate or a claim that the model was switched.
5. Say “rename this one heading”. Expect no new preflight. For implicit invocation, repeat step 3 with a different substantial task in a fresh chat without explicitly mentioning the skill, with the project snippet installed.

If this fails, check the actual discovered path, duplicate policies, scope, and restart behavior. Report the client version and a sanitized example. Do not change global model defaults as a workaround.

## Remove or update

For a CLI-managed install, use:

```sh
npx skills remove codex-model-preflight
```

This removes this **one named skill across project agent targets**, including its shared canonical directory; it does not remove other skill names. In the tested Skills CLI 1.7.4, Codex-only removal (`-a codex`) reported success but retained the shared `.agents/skills/codex-model-preflight` files. Check the directory and the skill selector after removal rather than relying on the success message.

If you still need this shared skill in another client, do not use the all-agent command; inspect that client's and Codex's per-skill disable controls instead. If installed globally, add `-g` only when you intend to remove the global copy. Review the installer's targets and prompts. For a manual install, locate the installed folder and remove only that folder in your file manager. Remove only the marked snippet you added to AGENTS.md. Leave other instructions and unrelated skills intact.

Before an update, inspect the new release and back up any local customization. Do not install a second copy under another scope with the same skill name.
