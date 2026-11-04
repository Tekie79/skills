---
name: qa-performance
description: "Analyze algorithmic efficiency, time and space complexity, real-world latency, UI rendering and backend scalability. Use for profiling, benchmark design, regressions and capacity reviews; not for invented performance claims or unapproved load tests."
---

# Performance and Complexity Review

## Goal
Prove or bound resource behavior on representative workloads, preserving correctness, security and traceability. A theoretical Big-O estimate is a model, not a measurement.

## Inputs
Exact SHA/build, function/operation, input-size variables, workload and dataset shape, critical correctness invariants, baseline, instrumentation, platform limits, approved service objectives and target authorization.

## Workflow
1. Identify actual hot path and boundaries: browser rendering, API, DB joins/indexes, queue/worker, storage, native and external provider. Read code and relevant queries before asserting cost.
2. Define n/m/k/p/b variables and expected/worst time, auxiliary/retained memory, I/O round trips, network payload, memory allocation and queue behavior. State assumptions such as indexed access, hash distribution and pagination.
3. Establish a golden correctness oracle, including tenant scoping, stable IDs, no duplicate canonical writes and UI stability, before recommending caching or algorithm changes.
4. Propose measurable workloads: cold/warm, representative and adversarial sizes, multi-tenant skew, long screenplay, large asset catalog, rapid canvas edits, duplicate names, concurrent writes and failed retries as relevant.
5. With explicit approval run bounded experiments; capture hardware, software, dataset seed, concurrency/offered load, duration, samples, warmup, p50/p95/p99 when statistically meaningful, throughput, errors, CPU, heap/RSS, query plan, lock waits and queue lag.
6. Compare reproducibly with baseline. Attribute gains/regressions to specific evidence, explain tradeoffs and prioritize the simplest fix with correctness-preserving targeted regression.
7. Use project-approved budgets; absent objectives means propose thresholds for review, not retroactively declare PASS. Abort load on saturation, data leakage, unexpected external messaging or spend.

## Output contract
A hotspot table with source path, variables, time/space/I/O hypothesis, actual profile, workloads, sample counts, before/after confidence, actionable change and verification. Explicitly mark NOT_RUN/BLOCKED for missing measurements.

## Example
Input: Drawing 1,200 set objects slows selection.
Output: Instrument render and hit-testing time vs object count, profile retained DOM/canvas work, confirm exact selected identity and undo semantics, compare viewport and hardware; do not claim a speedup without before/after data.

## Safety
No production stress/load, unbounded export, expensive provider call, destructive query profiling or automatic dependency installation. An explain-analyze operation can execute writes; verify target and query. See [behavioral evaluations](references/evaluations.md).
