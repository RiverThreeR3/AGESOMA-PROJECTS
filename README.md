# AGESOMA — AI Engineering

**Engineering reliable AI-enabled systems with testable contracts, safety boundaries and reproducible evidence.**

AGESOMA-PROJECTS is the company's **public engineering work and service-scope repository**. It distinguishes implemented components from proposals, CI verification from deployment, and technical demonstrations from paid client delivery. No commercial projects, customers, revenue or production systems are claimed without independently verified evidence.

## Current engineering work

### [Knowledge API — Extractive Retrieval Baseline](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2)

A FastAPI service that searches a fixed corpus of five **fictional** Markdown policy documents and returns source-backed text passages or abstains when the system cannot find sufficient lexical evidence.

**Implemented in the open PR:** typed input/output contracts, deterministic retrieval, document and line citations, synthetic evaluation, regression tests, Docker support and CI. No generative language model, vector database, real-document ingestion or customer data is involved.

| Evidence | Observed result | What it does **not** establish |
| --- | --- | --- |
| [Implementation PR #2](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2) | Open, not merged or deployed | A production-ready or client-approved service |
| [Baseline CI, SHA `62ccc7e`](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/actions/runs/42366822290) | Successful automated test/lint/evaluation and Docker checks | Live reliability or real-model answer accuracy |
| [Evidence-guard PR #7](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/7) | Separate reviewed change with stricter lexical abstention, numeric consistency checks and input validation; **not merged into PR #2** | That the baseline feature branch already contains these improvements |
| [Evidence-guard CI, SHA `895c32f`](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/actions/runs/42372898957) | **62 passing tests**; authored retrieval cases: 9 known-source, 3 basic unknown and 8 near-domain unsupported cases; Docker smoke and lint passed | Independent holdout accuracy, semantic correctness, security certification or production use |

The latest tested evidence guards remain under review. The five-document corpus and evaluation cases are synthetic and deliberately small. The [project quality gates](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/blob/895c32fd3d3100dc6c4015df38b0e046f9823e15/projects/knowledge-api/QUALITY_GATES.md) explain what is still missing.

## Engineering status by area

| Area | Publicly demonstrable today | Current boundary |
| --- | --- | --- |
| Document search and citation | Deterministic Knowledge API in open PR | Fictional Markdown, no user authentication or independent holdout |
| AI workflow integrations | [Proposed service design](SERVICES.md) | No completed AGESOMA implementation claimed |
| Permissioned AI agents | [Proposed acceptance specification](CASE_STUDIES.md) | No production agent or authorized external action |
| Multi-tenant AI copilots | [Proposed acceptance specification](CASE_STUDIES.md) | No verified tenant-isolated service |
| LLM gateway and evaluation | [Proposed acceptance specification](CASE_STUDIES.md) | No implemented provider gateway or real-model evaluation |
| Voice AI | Research backlog | No released voice agent claimed |

## How we engineer

**Define scope and acceptance criteria → implement the smallest deterministic baseline → test negative cases and permissions → measure quality and failure modes → review independently → deploy only with explicit authorization.**

For each implementation, reviewers should be able to inspect the original source, a reproducible test command, CI at its exact commit SHA, synthetic vs real evaluation boundaries, known limitations and the next release gate. An open PR is **in review**, not delivered or deployed.

## Technical documentation

- [Implementation plans and acceptance requirements](CASE_STUDIES.md)
- [Proposed AI Engineering services and deliverables](SERVICES.md)
- [Delivery controls and handoff process](SALES_DELIVERY_PLAYBOOK.md)
- [Publication and customer-data safety rules](PUBLICATION_POLICY.md)
- [Open-source dependencies and licensing review](OPEN_SOURCE_AUDIT.md)
- [Project-to-website evidence alignment](WEBSITE_PROJECT_SYNC.md)

## Company and personal portfolio

- **AGESOMA**: business problem, solution design, implementation and verification evidence.
- **[Raphael Ribeiro — AI Engineering portfolio](https://github.com/RiverThreeR3/AIEngineer)**: independently attributable individual technical contributions and engineering decisions.

The same implementation is linked rather than duplicated across these public repositories. Personal learning records, interview performance and private CV data are not public evidence.

## Website and release status

[AGESOMA's existing Vercel site](https://agesoma.vercel.app) is **separate from this repository**. Its past deployment status does not establish anonymous accessibility, current content synchronization or a published customer offer. Follow the [existing-site integration plan](SITE_INTEGRATION_PLAN.md); do not create another site or deploy production changes without source ownership, preview checks and approval.

**Current publication status:** engineering work in review, service scopes proposed, no independently verified customer deployment or commercial outcome. No unverified contact link, guarantee, pricing or performance claim is provided.
