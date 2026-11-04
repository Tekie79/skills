# Code Efficiency, Complexity, and Performance

## Review Before Optimizing

Choose measured hot paths: screenplay parsing/reconciliation, Breakdown occurrence
search, Library lists/search/preview, Scene/shot graph reads, large screenplay
editing, worker backlog recovery, and export. Include web rendering, API, database,
worker, and native resource costs separately. A broad architectural rewrite is
not an optimization recommendation without evidence of the bottleneck.

Check cohesion, duplication of canonical state, unnecessary abstractions, coupling,
dead code, resource ownership, exception paths, and maintainability. Prefer small
correct changes; do not trade tenant isolation, ordering, audit, or immutable
history for a faster benchmark. Provide a regression oracle before recommending
an algorithm replacement.

## Complexity Worksheet

For each material hotspot record:

| Field | Required analysis |
| --- | --- |
| Path | File/line, function/query, caller and user operation |
| Inputs | Define variables: e.g. `n` incoming scenes, `m` previous scenes, `k` candidate matches, `p` page size, `b` file bytes |
| Current cost | Worst/expected time, auxiliary and retained memory, I/O round trips and bytes; assumptions and bounds |
| Evidence | Loop/query structure, profile, allocation/heap sample, trace, query plan |
| Alternative | Candidate cost and tradeoffs: indexing, batching, streaming, bounded concurrency, caching |
| Verification | Equivalent outcomes, adversarial input, tenant correctness, before/after measurements |

Example hypothesis, not a verified SlateDog bug: comparing each new Scene against
each old Scene is `O(n*m)` comparisons; indexing stable signatures can approach
`O(n+m+k)` expected work with `O(m)` additional storage, but ambiguous-candidate
explosion can retain quadratic worst-case behavior. Preserve ambiguous review and
Scene IDs. Benchmark repeated headings and near-duplicates, not just unique scenes.

State average vs worst-case explicitly, including hash/index assumptions. SQL
complexity cannot be inferred from ORM syntax alone. A bounded page response does
not prove a bounded scan, join, count, sort, or deserialization. Consider repeated
calls, total pagination traversal, recursion depth, graph cycles, and regex/parser
pathological inputs. Separate input storage from auxiliary memory and output size.

## Database and Backend

- Detect N+1 patterns with query counts as `p` grows; measure connection-pool
  occupancy, transaction duration, lock waits, query latency, and rows examined.
- Inspect composite indexes for tenant filters, sort/cursor predicates, search
  vectors, and outbox claims. Test realistic tenant skew, high cardinality, missing
  selectivity, deep pagination, duplicate sort keys, and delete/change between pages.
- Use `EXPLAIN` first; `EXPLAIN ANALYZE` executes the query, including writes. Run
  it only against explicitly authorized disposable/safe data with timeouts. A
  rollback is not protection from every trigger, sequence, or external side effect.
- Check overfetching, unbounded arrays/joins/exports, redundant serialization,
  sync CPU work on request/event loops, repeated blob reads, and accidental copies.
- Evaluate tenant/user-aware cache keys, TTL, stampedes, mutation invalidation,
  memory limits, and permission revocation. Do not cache private data globally.
- Profile worker batch size/concurrency, bounded memory per file/job, stale-lease
  recovery, dead-letter growth and retry storms. Throughput improvements must retain
  canonical idempotency and avoid overwhelming PostgreSQL or provider quotas.

## Web and Native

- Measure initial navigation and in-app transitions separately, production builds
  rather than dev mode. Inspect server/client component boundaries, hydration,
  bundle/route payload, duplicate packages, waterfall requests, and font/image cost.
- Use a profiler to find excessive renders, large lists, synchronous parsing,
  expensive derived data and canvas/Designer redraw loops. Recommend memoization,
  virtualization or deferral only when evidence supports it and semantics survive.
- Check image sizing/lazy loading, responsive formats, cached assets, layout shifts,
  event-listener/observer/timer cleanup, object URLs, abortable requests, and growing
  caches. Sample heap after repeated route/open/close cycles for retained growth.
- Test lower-end devices, throttled CPU/network, long scripts, large selections,
  high-DPI drawing, print/export and native file operations. Frame drops and memory
  leaks need profiles, not subjective labels.

## Measurement Protocol

Define workload, synthetic seed, dataset scales, concurrency/arrival model,
hardware/container limits, network, build, candidate SHA, warmup, duration,
repetitions, and baseline. Track cold and warm cache separately. Report p50/p95/p99
latency, throughput, failure/timeouts, CPU, RSS/heap, database/worker saturation,
queue lag and recovery time. Include sample counts; a p99 from a tiny sample is
not trustworthy. Avoid coordinated omission: record offered load, completed load,
and dropped/time-out requests, not only successful-response latency.

Use geometric dataset growth (for example 100/1,000/10,000 synthetic records) within
approved capacity to test scaling. Empirical scaling can support a hypothesis,
not prove asymptotic bounds. Record variance and comparable before/after runs;
never report an invented speedup or compare unlike environments.

## Budgets and Load Profiles

Use established project SLOs/SLIs and performance budgets. If absent, propose them
for owner approval before a release decision. Do not invent current product SLAs.
For public web experience, common Core Web Vitals targets are LCP <=2.5 s,
INP <=200 ms and CLS <=0.1 at the 75th percentile of relevant field visits.
These are proposed targets unless adopted by the project; lab TBT is not INP,
and a Lighthouse score is neither field evidence nor a universal release gate.

Execute only authorized profiles: baseline, expected steady load, spike, stress
to an agreed ceiling, endurance/soak, and recovery. Set target allowlist, maximum
users/RPS, duration, spend, abort thresholds, monitoring, and cleanup before starting.
Use isolated staging and synthetic tenants. Stop on abnormal saturation, data
integrity issues, unexpected real messages/provider charges, or target mismatch.

Report capacity at the agreed latency/error budget, bottleneck, headroom, and
recovery behavior. Without approved budgets or representative execution evidence,
performance readiness is `BLOCKED`/`NOT_RUN`, not a guessed pass.
