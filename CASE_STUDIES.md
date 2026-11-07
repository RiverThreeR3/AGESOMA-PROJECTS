# AI Engineering Case-Study Specifications

**Evidence review (2026-11-07):** one original Knowledge API implementation is in [PR #2](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2), with a separate [quality-improvement PR #7](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/7). Neither has been merged into the flagship feature branch or independently deployed. The remaining cases are **specifications, not finished builds**. No paid client delivery or measurable customer outcome is claimed.

## P1 — Knowledge API (implemented lexical baseline; RAG extension proposed)

**Current public evidence:** [Knowledge API PR #2](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2) is **open** at commit `62ccc7e` with [CI success](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/actions/runs/42366822290). The [quality-gate PR #7](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/7) separately passed [62 unit/regression tests, Ruff, synthetic evaluation and Docker smoke](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/actions/runs/42372898957) at commit `895c32f`; **this change has not been incorporated into PR #2**. The reported 9 known, 3 unknown and 8 near-domain queries are hand-authored fixtures, not independent holdout data.

**Business need:** Search internal documents and answer questions without hallucinating unsupported facts.

**Implemented stack:** Python, FastAPI, fixed synthetic Markdown corpus, deterministic lexical retrieval, exact source-line citations, pytest, Ruff and Docker CI. **Not implemented:** embeddings, vector search, generative LLM outputs, real-document ingestion, tenant authentication, independent evaluation and production deployment. PostgreSQL/pgvector and model-assisted retrieval are possible future extensions, not part of this build.

**Engineering acceptance gates:**
- Parse a synthetic, licensed dataset (PDF and Markdown), preserve document/page IDs, handle ingestion errors.
- Compare keyword, vector and hybrid retrieval on a held-out question set; report recall@k and retrieval latency.
- Cite exact source passage(s), abstain when evidence is inadequate and test prompt-injection boundaries.
- Document authorization and separation of documents between tenants; verify no cross-tenant retrieval.
- Demonstrate replayable tests, container startup, a live demo if deployed, token cost and p50/p95 latency.

## P2 — Permissioned AI Workflow Agent

**Business need:** Use LLMs to help with customer/CRM operations while enforcing deterministic business rules.

**Proposed stack:** Python/FastAPI, model tool calling, optional LangGraph/MCP where warranted, webhooks and a mock CRM integration. n8n may be used as an integration adapter, not as proof of engineering by itself.

**Engineering acceptance gates:**
- Define minimal read/write tools, authorization policy and tool argument schema.
- Build a deterministic baseline and compare it to an AI-enabled agent on a labeled task set.
- Require approval for irreversible/sensitive actions; no unsupervised real sends, purchases or CRM edits in public demo.
- Handle duplicate webhooks, idempotency, retries, rate limits, secrets and failure recovery.
- Publish exact task-completion and unsafe-action rates, traces, latency and per-run cost.

## P3 — Multi-Tenant AI Support Copilot

**Business need:** Provide a reusable SaaS assistant that can serve multiple clients safely.

**Engineering acceptance gates:**
- Per-tenant authentication/authorization, tenant-scoped retrieval, RBAC and tested isolation.
- Background document ingestion and progress reporting; audit logs and PII redaction.
- Streamed responses with source citations, escalation workflow and dashboards.
- Docker/CI, observability, rate limiting, rollback plan, load and security testing.
- Reproducible demo with synthetic organizations, measured quality and cost.

**Dependency:** reuse evidence-backed modules P1 and P2; do not develop the full SaaS first.

## P4 — LLM Gateway + Evaluation Harness

**Business need:** Compare model providers and make LLM calls safer and predictable for engineering teams.

**Engineering acceptance gates:**
- Provider adapters with typed output, schemas, timeouts, retries, fallback and usage logging.
- Deterministic mock provider for CI; real-model evaluation separated and explicitly billed.
- Evaluation harness with versioned samples, held-out cases, regression thresholds and failure taxonomy.
- Present quality, p50/p95 latency, error rates, and real provider cost under identical scenarios.

## P5 — Voice AI Agent (research backlog)

**Business need:** Answer inbound calls, qualify requests and book appointments when authorized.

**Engineering acceptance gates:** explicit consent for recording and processing, fast interruptions, safe handoff, simulated scheduling, measured cost/call, latency and transcription quality. Start only after the core AI Engineering cases have reproducible demos.

## Engineering evidence and delivery boundaries

- [SERVICES.md](SERVICES.md) lists **proposed service scopes** separately from this actual implementation.
- [SALES_DELIVERY_PLAYBOOK.md](SALES_DELIVERY_PLAYBOOK.md) defines acceptance, controlled rollout and authorization requirements. Any implemented case must link exact source, CI for the same SHA, known failures and explicit permission before public client claims.
- Keep the Knowledge API as the only active source-code flagship until its documented acceptance gates pass. Do not equate an architecture proposal, GitHub CI success or a public repository with a delivered client system.

## Required status labels

Use one of: `proposed`, `in-progress`, `locally-tested`, `CI-verified`, `deployed-verified`, `portfolio-ready`. Never imply client implementation, paid contracts or customer results without documentation and authorization.
