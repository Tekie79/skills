# Agent Skills Workspace

An organization-wide collection of **portable, independently installable Agent Skills**. Each directory follows the [Agent Skills specification](https://agentskills.io/specification). The collection separates general-purpose QA disciplines from Meher Flow's film-production business contracts. No skill automatically installs, deploys, approves or releases anything.

## Skill catalog

| Skill | Use when | Scope |
| --- | --- | --- |
| [meher-flow-qa](skills/meher-flow-qa/SKILL.md) | QA, regression, UI, UAT or release testing **for Meher Flow** | Project-specific entrypoint; script, Breakdown, Library, Shot Designer, Scheduling, AI, self-host and later milestones |
| [qa-test-design](skills/qa-test-design/SKILL.md) | Design risk-based cases and select regressions | Generic across projects |
| [qa-test-execution](skills/qa-test-execution/SKILL.md) | Execute authorized tests or develop test automation | Generic across projects |
| [uat-business-acceptance](skills/uat-business-acceptance/SKILL.md) | Facilitate actual stakeholder task acceptance | Generic across projects |
| [qa-security-resilience](skills/qa-security-resilience/SKILL.md) | Authorization, tenant boundaries, data integrity and recovery | Generic across projects |
| [qa-ux-accessibility](skills/qa-ux-accessibility/SKILL.md) | UI fidelity, browser/device workflows and WCAG | Generic across projects |
| [qa-performance](skills/qa-performance/SKILL.md) | Complexity, benchmarks, performance and capacity | Generic across projects |
| [qa-release-readiness](skills/qa-release-readiness/SKILL.md) | Exact-candidate release decision and mandatory gates | Generic across projects |
| [slatedog-qa-uat](skills/slatedog-qa-uat/SKILL.md) | Explicit legacy callers of the previous SlateDog QA package | Compatibility; prefer meher-flow-qa for new work |

Each skill is self-contained. **Do not assume one skill implicitly installs or imports another.** For a Meher Flow request, load its project skill; for specialized work in another repository, load the relevant generic skill. When a task spans multiple disciplines, one coordinator can apply multiple skills without conflating their test results.

## Meher Flow quality approach

The [Meher Flow skill](skills/meher-flow-qa/SKILL.md) includes feature charters and scenario IDs for organization/project boundaries, screenplay import/revisions, scene Breakdown/aliases, Project Library, Shot List/Storyboard, 2D Shot Designer (including camera coverage), Scheduling/Call Sheets, AI, and conditional production/post/delivery milestones.

- **Focused feature QA:** test the changed behavior, impacted dependencies and protected canonical/tenant invariants. Do not routinely replay all historical tests after every isolated UI fix.
- **Automation:** an actual command, immutable SHA, test discovery count, result, fixture and redacted artifact are required for a PASS. Zero discovered tests, skips and blocked environments are not successes.
- **Human UAT:** a filmmaker or other authorized owner must perform/accept the real task. An agent or green browser suite cannot sign on their behalf.
- **Public release:** current application release policy and mandatory gates are authoritative. A feature can be UAT-ready while public publication remains disabled.

Detailed adoption guidance: [QA and UAT routing](docs/quality-usage.md).

## Layout

```text
AGENTS.md                    Workspace agent instructions
docs/authoring.md            Authoring/evaluation/security rules
docs/quality-usage.md        Selecting and adopting QA skills
templates/skill/SKILL.md     Scaffold template (not an installed skill)
skills/<skill-name>/SKILL.md Independently deployable skill
skills/<skill-name>/references/   Optional self-contained detail/evaluation cases
skills/<skill-name>/assets/       Optional reports/static templates
scripts/skills.py            Scaffold and structural/reference validator
tests/test_skills.py         Tooling tests (not application tests)
.github/workflows/skills-validate.yml   Skill library CI
```

## Quick start

Python 3.10+ is required to develop/validate skills. Run from the repository root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/skills.py new summarize-notes --description "Summarize meeting notes into decisions and action items. Use when processing a rough transcript."
.venv/bin/python scripts/skills.py validate
.venv/bin/python -m unittest discover -s tests -v
```

After scaffolding, replace draft markers and add linked task-specific evaluations. Or validate one:

```sh
.venv/bin/python scripts/skills.py validate skills/meher-flow-qa
```

The validator checks frontmatter, naming, draft placeholders, nonempty instructions, and local Markdown links that exist **inside each skill**. It does not test a running agent, execute application QA, certify sandbox permissions, prove behavioral quality or validate external URLs. For optional spec checks, run the upstream [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) separately.

## Example requests

- “Prepare focused QA and regression tests for Meher Flow Shot Designer's camera coverage selector; report skipped risks.”
- “Create independent director and 1st AD UAT scripts for Meher Flow's Stripboard and Day Plan.”
- “Review this application's API tenant isolation using synthetic tenants and an authorized test environment.”
- “Compare baseline and candidate rendering performance for 1,200 layout objects; do not invent measurements.”
- “Audit an exact release candidate against its policy and human acceptance evidence; do not deploy.”

## Distribution and safety

Install or link only the intended skill directory into the target agent's documented discovery path. Do not install the template or repository root as a skill. Keep credentials out of prompts and fixtures. Real test execution, migration/seed, external messaging, load, publication, pushes and merges require appropriate explicit authorization and verified safe targets. A skill never grants privileges.

This repository is for multiple organizational projects. Product adapters must not redefine other projects' security policies or claim future capabilities already exist. Set licensing explicitly before distributing third-party content or examples.
