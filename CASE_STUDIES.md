# AI Engineering Case-Study Specifications

**All cases below are PROPOSED as of 2026-11-04.** This document is a delivery backlog, not proof that code exists.

## P1 — Enterprise Knowledge API (RAG)

**Business need:** Search internal documents and answer questions without hallucinating unsupported facts.

**Proposed stack:** Python, FastAPI, PostgreSQL/pgvector (or Qdrant when justified), embeddings, hybrid retrieval, structured LLM outputs; Docker and CI.

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

## Required status labels

Use one of: `proposed`, `in-progress`, `locally-tested`, `CI-verified`, `deployed-verified`, `portfolio-ready`. Never imply client implementation, paid contracts or customer results without documentation and authorization.
