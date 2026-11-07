# AGESOMA — Reproducible Business Simulations

**Evidence date:** 2026-11-07. **Execution origin:** standalone **Knowledge API Python simulator**, **NOT InstantWork**. This is retained as earlier public engineering evidence; new AGESOMA work samples must use the private InstantWork operating platform and only publish sanitized verification artifacts here. **Status:** Synthetic evaluation in open engineering [PR #8](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/8); **not merged, deployed, client-delivered or production-verified**.

The objective is to show the *behavior of running code on transparent fictional workloads*, then distinguish that behavior from purely assumed time or revenue effects. No simulated result is presented as a real customer, contract, ROI or historical business performance.

## Two implemented simulations (one Knowledge API codebase)

The [Knowledge API at commit `1c25782`](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/tree/1c25782a8d1cc9ba591480bf3228026979f24446/projects/knowledge-api) executes a deterministic lexical retrieval baseline over five fictional policy files. The [simulation script](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/blob/1c25782a8d1cc9ba591480bf3228026979f24446/projects/knowledge-api/simulate_workload.py) processes 30 authored, fictional queries: 15 customer-support and 15 internal-operations tickets.

| Simulation | Unique fictional tickets | Expected passage AND expected source matched | Handoff drafts | Unsafe/mismatched candidates on authored cases | Hypothetical manual handling (min) | Hypothetical human-reviewed handling (min) | **Modeled** minutes saved |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Customer support knowledge desk | 15 | 10 | 5 | 0 | 90 | 40 | **50** |
| Internal operations policy desk | 15 | 10 | 5 | 0 | 120 | 60 | **60** |
| **Combined** | **30** | **20** | **10** | **0** | **210** | **100** | **110** |

**Source of observed code behavior:** [GitHub Actions run 42375020327](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/actions/runs/42375020327), success for exact PR head `1c25782a8d1cc9ba591480bf3228026979f24446`. Job: `verify-api`. The job logs and job summary contain the computed simulation table. **71 pytest tests passed**, Ruff lint, synthetic retrieval evaluation, Docker build and container health smoke succeeded (one dependency deprecation warning).

### What is observed versus modeled

**Observed by executing code:** document/passage labels, handoff draft classification and counts. A valid *source-and-excerpt match* is a **fixture check** and is not an independent semantic correctness judgment. The evaluator can see the fixture's expected answer and uses it to detect mismatches; a real agent cannot know an unknown answer's label.

**Invented assumptions used only for arithmetic:**
- Customer support: manual handling **6 min/ticket**; human review of a source-matched draft **1 min/ticket**.
- Internal operations: manual handling **8 min/ticket**; human review of a source-matched draft **2 min/ticket**.
- Unsupported or mismatched cases receive **no modeled time saving**; they retain the full manual handling time.

The calculations give **55.56%** modeled reduction for support, **50.00%** for internal operations and **52.38%** across this synthetic 30-ticket mix. These are **not** measured clock times, customer resolution rates, SLA results, wages, cost savings, revenues or investment returns. There is no monthly extrapolation. All 30 cases were authored for development; none is a blind holdout or real traffic sample.

### Reproduce

From the branch in [PR #8](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/8), inside `projects/knowledge-api`:

```bash
python -m pip install -r requirements-dev.txt
python simulate_workload.py --format markdown
python simulate_workload.py --format json
python -m pytest -q
```

[Read the full simulation methodology and case fixture](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/tree/1c25782a8d1cc9ba591480bf3228026979f24446/projects/knowledge-api/simulations). No paid API accounts, cloud services, n8n, WhatsApp, CRM or customer records are used. A `human_handoff_draft` is a simulated disposition, not an actual ticket created in a vendor system.

## Related technical demonstration (separate personal repository)

The [InstantCloser policy lab](https://github.com/RiverThreeR3/AIEngineer/tree/main/projects/instantcloser) independently demonstrates **11 hand-authored deterministic decision-policy cases** involving consent, opt-out, objections and approval requirements. [CI run 42370624923](https://github.com/RiverThreeR3/AIEngineer/actions/runs/42370624923) passed **six unit tests and all 11 synthetic scenarios**. It is **not** a connected CRM, live lead-qualification agent, messaging service, verified client engagement or AGESOMA-owned production implementation. It is linked for related engineering context only; no source code is duplicated.

## What still prevents a credible enterprise pilot

- **True validation:** independently labeled unseen support queries, false abstention/unsupported-answer rates and expert review.
- **Data/identity:** consented document ingestion, tenant authentication, authorization, retention and deletion.
- **Integration:** mocked CRM/webhook adapters followed by sandbox integration, deduplication/idempotency, retry/error handling and human approval.
- **Operations:** measured real time-on-task and review effort, latency/load checks, privacy-preserving telemetry, threat modeling, deployment, rollback and customer signoff.
- **Commercial proof:** genuine client pilots and measured outcomes only when documented and authorized.

The engineering work remains on **one original Knowledge API flagship**. These are scenario harnesses and links, **not** multiple claimed client solutions.
