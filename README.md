# Agent Skills Workspace

A provider-neutral workspace for developing reusable AI agent skills. Skills follow
the [Agent Skills specification](https://agentskills.io/specification), rather than
a proprietary prompt or tool format.

## Layout

```text
AGENTS.md                   Instructions for agents working in this workspace
docs/authoring.md           Authoring, safety, evaluation, and release checklist
templates/skill/SKILL.md    Starter instructions, not an installed skill
skills/                    Authored skills (created by the scaffold command)
scripts/skills.py           Scaffold and validate skills
tests/test_skills.py        Tests for the development tooling
requirements-dev.txt       Development dependencies only
```

Each published skill is a self-contained directory:

```text
skills/my-skill/
  SKILL.md                 Required metadata and instructions
  scripts/                 Optional deterministic helpers
  references/              Optional detailed guidance, including evaluations
  assets/                  Optional templates or static resources
```

Create optional directories only when they contain useful material. The workspace
tooling is not a dependency of the skills you author.

## Quick Start

Requires Python 3.10 or newer. Run commands from this workspace directory.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/skills.py new summarize-notes --description "Summarize meeting notes into decisions and action items. Use when turning meeting transcripts or rough notes into a concise team summary."
```

Edit `skills/summarize-notes/SKILL.md`, replacing every `TODO` with concrete
instructions. Then validate and test:

```sh
.venv/bin/python scripts/skills.py validate
.venv/bin/python -m unittest discover -s tests -v
```

Validate a single skill or an alternative collection:

```sh
.venv/bin/python scripts/skills.py validate skills/summarize-notes
.venv/bin/python scripts/skills.py validate --root /path/to/skill-collection
```

The validator checks metadata, naming, nonempty instructions, and unfinished draft
markers. It intentionally requires a mapping-style YAML frontmatter and the
current specification's field names. It does not prove instruction quality,
runtime compatibility, script safety, or task success. See
[the authoring guide](docs/authoring.md) for behavioral evaluation.

## Use With Agents

Install or link individual directories under `skills/` into the skill discovery
location documented by your target agent. Discovery paths, tool permissions, and
installation commands vary by runtime; this repository does not install anything
automatically. Do not install `templates/` as a skill collection.

Keep instructions portable. Document any required tools, credentials, network
access, or runtime-specific behavior in each skill. Never embed credentials.

## Available Skills

[`slatedog-qa-uat`](skills/slatedog-qa-uat/SKILL.md) provides project-specific QA,
UAT, and release-readiness workflows for SlateDog / Meher Flow. It covers
functional and advanced testing, code efficiency and complexity, performance,
design/accessibility/SEO, tenant security, data integrity, and operational recovery.

Example requests after loading the skill in your agent:

- "Build a risk-based UAT plan for Meher Flow's Library upload changes."
- "Review SlateDog reconciliation time/space complexity and propose benchmarks."
- "Assess this exact release candidate; distinguish missing evidence from failures."

The skill includes a pinned repository research baseline, not an application QA
result. Read its safety boundaries before running tests or touching an environment.

## Scope

This baseline does not choose a domain, model, runtime, deployment platform, or
license for future skills. Set licensing explicitly before distributing content.
Do not assume third-party examples or assets can be redistributed.
