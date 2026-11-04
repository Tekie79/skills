# Routing and Extending the Agent Skills Collection

The repository is a multi-project skill library, not one monolithic agent. Skills are self-contained bundles and no skill assumes another skill is installed.

## Which skill should handle the request?

| User intent | Preferred skill |
| --- | --- |
| Meher Flow engineering quality, functional/API/browser/regression/security review | meher-flow-qa |
| Meher Flow director/producer/crew/customer acceptance | meher-flow-uat |
| Unrelated software project's technical QA | quality-engineering |
| Unrelated product's business UAT | uat-facilitation |
| Immutable release candidate, mandatory gates and publish recommendation | release-evidence-review |
| Existing legacy automation explicitly names SlateDog combined skill | slatedog-qa-uat |

If a request combines concerns, perform only the requested scope and distinguish **technical QA** from **actual human UAT** and **release authority** in the output. A high confidence automated test does not become a signed human acceptance. Installation and activation depend on the target agent's documented skill discovery, not this repo.

## Template for another project

1. Create a product-named skill using scripts/skills.py new and a concrete trigger description.
2. Make the SKILL.md self-contained, with a source SHA/date, current-snapshot warning and project safety policy.
3. Add references/module-charters.md for delivered functionality, assets/report.md and references/evaluations.md with synthetic positive, negative and unsafe/missing-tool prompts.
4. Prefer linked concise reference files over a SKILL.md longer than 500 lines. Never link to resources outside its directory to perform the task.
5. Keep generic skills portable; put exact project commands, release policy and module-specific identity rules in the named product skill.
6. Run structural validation, repository tooling tests and target-agent behavioral evaluations; record results honestly. See docs/authoring.md.

## Evidence and regression rules

Every check has a candidate SHA, role/tenant where relevant, test method, expected observable behavior, actual outcome, evidence, timestamp and PASS/FAIL/BLOCKED/NOT_RUN/NOT_APPLICABLE. Report initial failed runs and retries. Avoid claiming coverage from an old commit or a different environment.

Test selection is risk-based: changed behavior plus affected data/contracts/permission boundaries and protected critical workflows. Candidate release policy remains mandatory and can require broader execution. Report excluded legacy suites and why; never silently count them as passing.

## Safe distribution

Agent Skills are instructions, not credentials or security permission grants. Do not copy production data into fixtures, embed tokens, turn off release gates, run destructive database tests, send real messages, or approve UAT on another person's behalf. Test in an explicitly verified isolated environment and require the user or authorized owner to perform high-impact actions.
