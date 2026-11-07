# AI Engineering Services — Scoping, Delivery and Retention

This is an internal-methodology-style **public description of proposed delivery standards**, not evidence of past client engagements.

## Opportunity qualification

1. **Buyer pain:** what manual step, information failure or customer outcome requires improvement? Identify current owner.
2. **Data and integrations:** exact source systems, API availability, consent, privacy, data residency and the human fallback path.
3. **Baseline:** current time/step count, failure frequency, quality/accuracy and cost measured or explicitly unknown.
4. **Acceptance:** task success, source-grounding, authorization, latency, operating cost and rollback checks agreed before the build.
5. **Delivery constraints:** access rights, credentials managed by client, hosting, client-owned subscriptions, budget, deadline and approval process.
6. **Commercial gate:** request written approval for production access or outbound actions. Stop when requirements are unsafe or cannot be verified.

## Standard offer ladder (quotes are custom)

| Engagement | Meaning | Output | Exclusions |
| --- | --- | --- | --- |
| Discovery / AI Workflow Audit | Map the work and technical risks | Process map, architecture options, measurement plan, staged scope | Not a deployed agent |
| Integration or Reliability Sprint | Fix a bounded existing pipeline or integrate one workflow | Reproduced baseline, tested change, runbook, risk report | No indefinite support or guaranteed business outcomes |
| Build + Controlled Pilot | Deliver one bounded AI-enabled workflow or knowledge service | Original code, tests, evaluation report, sandbox/human approval, handoff | No unapproved real messaging, purchases, access elevation or claims of flawless AI |
| Post-release Quality & Support | Explicitly agreed follow-up | Regression checks, incident triage, monitoring/quality/cost review | No assumed SLA without a signed service agreement |

Do not force a production-scale system into a low fixed budget merely because a listing advertises one. An underpriced posting can be a discovery lead, not an economically viable delivery contract.

## Technical project checklist

- Confirm client requirements and sanitized architecture.
- Favor a deterministic manual/rule-only baseline; add a model only where it proves value.
- Typed inputs/outputs, idempotent webhook handlers, timeouts, bounded retries and budget caps.
- Real permission checks; customer identities must originate from authenticated systems.
- Synthetic or licensed test data; no publishing customer content or client credentials.
- Evaluations using unseen cases and negative/security tests; separate mocks and real model calls.
- Observability with token/cost/latency/failure reports where measured, versioned evidence at exact SHA.
- Deployment only with explicit customer authorization; verify rollback and handoff.
- Traceable changes, license and dependency review, truthful completion and demo claims.

## Proposal outline (English)

**Problem understood:** customer process and outcome sought.

**Proposed scope:** bounded workflow, API integrations and first acceptance milestone.

**Milestones:** discovery/baseline, original implementation, security/eval, approved handoff.

**Evidence:** portfolio case-study link to the closest *independently verified* capability, with limitations.

**Assumptions/exclusions:** data access, model-provider charges, privacy requirements, licenses and maintenance.

**Next step:** a scoped discovery conversation. No price or delivery promise before confirming scope.

## Public portfolio and private career boundary

AGESOMA-PROJECTS publishes authorized business cases. Raphael's [personal AI Engineer portfolio](https://github.com/RiverThreeR3/AIEngineer) contains his independently demonstrated personal technical experience. Cross-link verified proof instead of duplicating implementations. Do not link the private lesson tracker, private master CV or private client data.

## Weekly commercial review

On the existing Monday AI Engineer+AGESOMA-PROJECTS routine: use **LinkedIn only** for actual career/contract opportunity scouting; separately sample public **Upwork and Workana briefs** strictly to identify recurring **technical requirements for synthetic work samples**, never as application or contact leads. Choose one bounded milestone for the Knowledge API flagship, implement a verifiable simulation only where it fits that scope, and report actual execution vs invented time/ROI assumptions separately in [SIMULATIONS.md](SIMULATIONS.md). During BUILD/AUDIT use small, reviewable PRs. On Sunday reconcile project evidence, recruiter guide, private resume and client-facing claims. **Do not start a second flagship or imply a client project was delivered.**
