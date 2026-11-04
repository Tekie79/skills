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

## 6. Multiple Products and Quality Skills

Use focused, independently installable skills rather than one workspace-wide giant prompt. Name the target product in the skill name only for project-specific workflows. A generic quality-engineering skill must not assume another product's stack, CI gates, severity policy, test URLs, role names, or credentials.

For QA skills, explicitly distinguish plans from source audit and independently executed runtime tests. Define a change-impact and regression-selection process including critical security/data boundaries. For UAT, use human-facing business tasks and keep real acceptance decisions separate from agent outputs. For release skills, verify immutable source/artifact binding and current project-specific release controls.

A project map must state the inspected repository, SHA, date and known freshness limits. Roadmap features cannot be treated as implemented. Prefer proportionate regression, with protected invariants and mandatory gates, to replaying an unbounded historical suite for each change.

Validate all relative links from SKILL.md and test that a skill directory operates without this workspace. Evaluation case tables remain a plan until actual target-runtime execution is recorded. See [skill routing](skill-routing.md).
