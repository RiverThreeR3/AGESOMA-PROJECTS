# InstantWork — Demonstrations and Evidence

**This is the public sales-proof roadmap, not a customer-results page.** The actual InstantWork application source is private, and its current status is **LABORATORY / PREPRODUCTION**.

We intend to sell a software product that **performs business work**. A buyer should be able to inspect multiple independent examples of **what was requested, what InstantWork did, what it produced and what was verified**. Technology is a means of completing the job, not the product itself.

## Demonstrations under development

| Business work that could be delegated | What a credible demo must produce | Evidence status on 2026-11-07 | Missing gate |
| --- | --- | --- | --- |
| **Keep a CRM accurate** | Approved sandbox update, independent record readback, no duplicates, action receipt | **Not verified**. Twenty CRM staging code exists in private InstantWork | Successful exact-SHA CI, tenant authorization, idempotency and real sandbox receipt |
| **Prepare and handle customer follow-ups** | Scoped work order, approved draft or send, recipient opt-in and status trail | **Not verified**. Local fictional draft harness PR exists, but CI failed | Passing tests, approved channel integration, consent and provider receipt |
| **Turn business documents into usable work** | Authorized corpus ingestion, cited answer or abstention, reviewable next action | **Not verified in InstantWork** | Actual integrated runtime, independent retrieval evaluation and permission tests |
| **Prepare a data report** | Synthetic/approved input, reproducible transformation, delivered file with quality report | **Proposed** | Source-controlled executor, reproducible tests and generated artifact |
| **Fix a digital-work problem** | Verified code or API change, test results, reviewable PR and rollback notes | **Proposed** | Genuine InstantWork coding/workspace execution and closed-loop tests |
| **Continue work across sessions** | Task state survives restart, safe autonomous progress, approval handoff, recovery evidence | **Proposed** | Durable task persistence, background runtime and failure/replay tests |

These are **six candidate demonstration families**, not six shipped features or examples of paid commissions. Even a local demo must run **actual InstantWork code**; an independently developed Python project cannot be relabeled as InstantWork output.

## What an actual proof card will contain

Each completed, publicly shareable example must provide:

| Field | Required evidence |
| --- | --- |
| **Business request** | A clear job, expected artifact and testable completion condition |
| **Execution source** | InstantWork, exact implementation revision and relevant authorized adapters |
| **Inputs** | Fictional/approved data, scale and known limitations |
| **Result** | Actual produced artifact, before/after observation and failures |
| **Verification** | Reproducible public-safe demonstration, independent acceptance check or provider receipt |
| **Safety** | Consent, scoped identity/permissions, rollback/stop and sensitive-data treatment |
| **Metrics** | Real observed quality, time, latency and cost only where measured; modeled assumptions clearly separate |
| **Status** | `SCOPED`, `LOCAL_SIMULATION`, `QA_VERIFIED`, `AWAITING_APPROVAL`, `EXTERNAL_ACTION_VERIFIED`, `CLIENT_ACCEPTED`, `FAILED` or `BLOCKED` |

**No synthetic test will be called a real customer delivery.** Do not publish raw private InstantWork code, security secrets, customer details or misleading screenshots.

## Evidence scoreboard

For every demonstration, disclose when data is actually available:

- Tasks accepted with verifiable completion receipts / eligible attempted tasks
- Independently checked correctness and negative/failure cases, with dataset and sample size
- Human approval and rejection behavior, including unauthorized-action prevention
- Real elapsed time, execution cost and recovery from failure
- Customer feedback, ROI and business effects **only if measured and publication is authorized**

### Current release barrier

The private InstantWork sample CI is failing, and an end-to-end verified business action has not been established. Until those gates pass, the portfolio may describe progress and demonstrate the planned evaluation format, **but may not market the platform as a finished autonomous execution service**.

**Next step:** verify a complete **single** work order in an isolated sandbox, capture an independently checkable artifact/receipt, and publish the first real InstantWork demonstration. Scale to additional categories with the same permission/evidence contract.

Read the [current capability ledger](CAPABILITIES.md), [publication rules](PUBLICATION_POLICY.md) and [earlier unrelated standalone experiments](LEGACY_ENGINEERING_EVIDENCE.md).
