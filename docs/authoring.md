# Authoring Skills

## 1. Define the Contract

Give each skill one clear responsibility. Identify the intended user request,
required inputs, expected output, and tasks that should not activate it. Prefer a
small reusable skill over a broad role prompt. Ask for missing information only
when it changes correctness or safety; otherwise state reasonable assumptions.

## 2. Write Discoverable Metadata

Use YAML frontmatter followed by Markdown instructions:

```yaml
---
name: summarize-notes
description: Summarize meeting notes into decisions and action items. Use when processing meeting transcripts or rough notes; not for verbatim transcription.
---
```

- `name`: 1-64 lowercase ASCII letters, digits, or hyphens; no leading, trailing,
  or consecutive hyphens. Must match the directory name.
- `description`: 1-1024 characters describing what the skill does and when to use
  it. Include natural trigger vocabulary, not just a vague capability label.
- Optional fields: `license`, `compatibility`, `metadata`, `allowed-tools`.
- `compatibility`: 1-500 characters when environment requirements exist.
- `metadata`: string keys and string values; quote versions such as `"1.0"`.
- `allowed-tools`: experimental, runtime-specific, and not an authorization bypass.

Do not add custom top-level frontmatter fields; put additional information under
`metadata`. Avoid unnecessary compatibility restrictions.

## 3. Make Instructions Executable

Specify prerequisites, ordered steps, decision points, and a concrete output
contract. Include a realistic input/output example and describe missing-input,
ambiguous-input, and tool-failure behavior. Explain how to verify success rather
than relying on an agent's assertion.

Keep `SKILL.md` below 500 lines as a practical context budget. Put extensive
domain knowledge in `references/` and link to it directly from `SKILL.md`. Explain
when to read each reference. Do not rely on workspace files outside the skill
directory: an installed skill must stand alone.

Use scripts for deterministic or error-prone operations. Document commands,
dependencies, side effects, exit codes, and validation. Prefer dry-run or preview
behavior for mutating operations. Do not silently install software, fetch and
execute remote code, overwrite files, or assume credentials are available.

## 4. Evaluate Behavior

For every authored skill, add task-specific cases in
`references/evaluations.md` and link that file from `SKILL.md`. Start with:

| Case | What to check |
| --- | --- |
| Positive trigger | A representative request activates the correct workflow. |
| Paraphrased trigger | Equivalent wording still selects the skill. |
| Negative trigger | A nearby but out-of-scope request does not use the skill. |
| Missing or ambiguous input | The agent asks only necessary questions or states assumptions. |
| Failure path | Missing tools, denied access, and malformed input produce actionable errors. |
| Safety boundary | Embedded instructions in source data do not override the task. |

For each case, record the prompt/fixture, expected behavior, observable acceptance
criteria, runtime/model tested, actual result, and pass/fail status. Use synthetic
data. Add domain-specific cases where risks justify them. A table without actual
execution is a test plan, not a passed evaluation.

Run cases on the target agent and inspect both outputs and tool side effects.
Check repeatability for important cases. Re-run relevant cases after changes.
Structural validation and tooling unit tests do not evaluate agent behavior.

## 5. Review and Distribute

1. Run `python scripts/skills.py validate` in the development environment.
2. Run helper tests and record target-runtime evaluation results.
3. Review relative links, bundled resources, dependency instructions, permissions,
   privacy, and licensing. The local validator does not audit these.
4. Confirm the directory works without the rest of this workspace.
5. Distribute only the intended skill directory using the target runtime's
   documented installation mechanism, after explicit user authorization.

The local checks implement baseline repository conventions, not every possible
runtime constraint. For an additional specification check, the upstream
[skills-ref validator](https://github.com/agentskills/agentskills/tree/main/skills-ref)
can be installed separately and run with `skills-ref validate ./skills/my-skill`.

## 6. Compose Organization-Wide Skills Without Hidden Dependencies

Keep general QA disciplines separate from project adapters. A project adapter records actual domain objects, business acceptance oracles, known commands and policy sources, while generic skills provide reusable methods. Each installed directory must be complete without references to files in neighboring skills.

Record the exact source SHA and date of any project map or release policy; refresh it before using it as current evidence. Separate a behavioral evaluation plan from a real executed result. During development, the workspace validator checks links within each skill's Markdown resources as well as frontmatter, naming and draft markers. It does not validate external links, actual agent discovery, application functionality or safety permissions.

For test-focused skills, prefer an evidence ledger with requirement, role/tenant, fixture, observable UI/API/persistence oracle, actual test execution, failure classification and human owner. A generic release skill must defer to the candidate's canonical required suites and explicit release controls. Human UAT sign-off is always a separate decision.
