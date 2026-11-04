# Quality Assessment: [Project / Candidate]

Scope: [feature, requirement IDs, changed files, candidate SHA/base SHA]
Mode: [plan | static | execute | retest]
Environment: [synthetic tenant, database, storage, browser, services, timestamp]
Authorization and limits: [what may run, side effects, what is prohibited]
Source/evidence freshness: [directly inspected vs supplied]

## Change-impact selection

| Change/dependency | Risk/tier | Required existing and new checks | Excluded suites + reason | Mandatory project gate |
| --- | --- | --- | --- | --- |

## Cases and execution evidence

| Case ID | Requirement | Persona/role and fixture | Steps and expected durable outcome | Test level / command | Actual / evidence / timestamp | Status |
| --- | --- | --- | --- | --- | --- | --- |

## Findings

| Defect | Severity | Expected/actual | Minimal reproduction | Evidence / candidate SHA | Fix recommendation | Retest status |
| --- | --- | --- | --- | --- | --- | --- |

## Summary

Observed passes: [named commands/cases only]
Failed: [issues]
BLOCKED/NOT_RUN/NOT_APPLICABLE: [rationale, not silently treated as PASS]
Untested critical risks: [names and owners]
Recommended next tests: [specific commands after safety verification]
Human business UAT: [not requested / pending / documented externally]
This document is QA evidence, not deployment approval.
