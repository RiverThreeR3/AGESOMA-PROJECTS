# Market Demand Watchlist — Workana, Upwork & LinkedIn

**Captured:** 2026-11-04. **Scope:** selected publicly visible advertisements and first-party market reports, not a complete scrape, representative platform sample, market-share study, contract-win history or estimate of AGESOMA revenue. Job availability and bids can change immediately. Update on the existing weekly consolidated AI Engineering routine.

## Platform roles

- **Workana:** project briefs from clients, especially SMB WhatsApp/CRM automation, RAG and professional back-office workflows.
- **Upwork:** international freelance scopes, paid-scope signals, pipeline/reliability work, n8n/agent integrations and SaaS projects. Published budgets are *buyer asks*, not market medians or economically viable AGESOMA quotes.
- **LinkedIn Jobs:** technical hiring requirements and production-readiness expectations. A full-time role is a **skills signal**, **not** a directly available freelance contract.
- **Upwork first-party research:** use independently published broad market trend reports to triangulate the selected advertisements, never confuse search volume, hired contracts, earnings or posting counts.

## Verified source samples

| Source | Listing / report date | Concrete requirement | Market signal | Link |
| --- | --- | --- | --- | --- |
| Upwork official research | 2026-02-04 | AI Integration +178%, AI Chatbot Development +71% in published 2026 annual report | Broad demand trend; growth rate is NOT frequency of current postings | [2026 In-Demand Skills](https://www.upwork.com/press/releases/upworks-in-demand-skills-2026-demand-for-top-ai-skills-more-than-doubles-as-ai-is-embedded-into-everyday-work) |
| Upwork official research | 2026-09-15 (August snapshot) | AI automation remained leading client search term; rapidly rising automation-focused searches | Search-demand signal, not confirmed buying contracts for AGESOMA | [August 2026 Hiring Insights](https://www.upwork.com/research/upwork-monthly-hiring-insights-august-2026) |
| Workana | 2026-10-22 | WhatsApp AI assistant and n8n for FAQ, leads and appointments | Automation and integration service | [WhatsApp AI + n8n](https://www.workana.com/pt/job/desenvolvimento-de-chatbot-inteligente-para-whatsapp-com-ia-e-n8n) |
| Workana | 2026-10-20 | Python/TypeScript, PostgreSQL/Supabase, approval workflows, AI agents and RAG for fiscal processes | AI workflow modernization and business-system integration | [Tax operations system](https://www.workana.com/pt/job/desenvolvedor-a-senior-python-com-ia-para-automacao-tributaria-remoto) |
| Workana | 2026-09-03 | Agentic AI + enterprise RAG, auth, privacy, telemetry, Docker/cloud | Production-grade RAG and secure agents | [Enterprise RAG & agents](https://www.workana.com/pt/job/desenvolvimento-de-plataforma-de-ia-agentica-e-rag-enterprise-com-seguranca-e-escalabilidade) |
| Upwork | 2026-11-03 | Existing n8n Cloud, OpenAI, Supabase/pgvector, Gmail/Drive/Calendar integrations; tests and documentation | Integration reliability / finish-and-handoff work | [Repair n8n workflow](https://www.upwork.com/freelance-jobs/apply/n8n-Developer-Needed-Complete-Workflow-Project-Fixed-Price_~022117741829260636765/) |
| Upwork | 2026-11-02 | RAG, citations, LangGraph, FastAPI, tenant safety, evaluation | Enterprise Knowledge API & RAG service | [RAG assistant](https://www.upwork.com/freelance-jobs/apply/Engineer-Needed-Build-Production-Ready-RAG-Assistant-with-LangGraph-FastAPI_~022117265006300703350/) |
| Upwork | 2026-11-03 | Diagnose inaccurate retrieval in an existing RAG implementation | RAG reliability audit and remediation | [RAG retrieval repair](https://www.upwork.com/freelance-jobs/apply/RAG-Pipeline-Engineer-Needed-Diagnose-Retrieval-Issues-and-Improve-Answer-Reliability_~022117578681695808118/) |
| Upwork | 2026-10-29 | Multi-tenant SaaS with retrieval, support agent, human escalation, n8n, FastAPI | Enterprise AI support copilot / security | [Multi-tenant copilot](https://www.upwork.com/freelance-jobs/apply/Build-Multi-Tenant-Support-Copilot-SaaS-RAG-Agent-Next-FastAPI-n8n_~022115739208598410375/) |
| Upwork | 2026-10-28 | Lead-qualification agent, HubSpot sync, n8n and RAG | CRM automation and revenue operations | [Lead qualification + HubSpot](https://www.upwork.com/freelance-jobs/apply/Build-Lead-Qualification-SaaS-RAG-Chat-Agent-HubSpot-Sync-n8n-Automation_~022115515900326480667/) |
| LinkedIn Jobs | Seen 2026-11-04; publish date not independently established | Python/FastAPI, LangGraph, production tool calling, structured outputs, RAG, evals, WhatsApp and LGPD | Employer skills evidence, **not freelance job volume** | [GestãoDS — Senior AI Engineer](https://br.linkedin.com/jobs/view/engenheiro-a-de-ia-s%C3%AAnior-%E2%80%94-python-e-agentes-langgraph-at-gest%C3%A3ods-4477340207) |
| LinkedIn Jobs | Seen 2026-11-04; publish date not independently established | Agentic AI & RAG, Python, MCP, reliability, retrieval evaluation, latency/cost, secure business APIs | International senior/production bar; **not a company service contract** | [Teilur — AI Engineer](https://br.linkedin.com/jobs/view/ai-engineer-agentic-ai-rag-at-teilur-talent-4487525793) |

## Qualitative shortlist, not statistically ranked platform counts

| Priority | Service offer | Why this signal matters | Current AGESOMA proof status |
| --- | --- | --- | --- |
| P1 | AI Workflow Automation & Integrations | Present across Upwork/Workana; Upwork research supports broader AI integration interest | Offer documented; no independently accepted client delivery |
| P2 | Enterprise Knowledge API & RAG Reliability | Explicit detailed scope and focused diagnosis/repair demand | Knowledge API in [PR #2](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2), open and not deployed |
| P3 | Permissioned Business AI Agents | Cross-platform CRM/WhatsApp/API tool integrations and authorization concerns | Proposed; no AGESOMA agent case verified |
| P4 | Multi-Tenant AI Support Copilot | Concrete SaaS integration/security requirements, larger delivery surface | Proposed; use validated P2/P3 modules first |
| P5 | LLM Reliability & Cost / Eval Sprint | Observable need for debugging inaccurate answers and operating costs | Proposed; require baseline-to-fix quantitative evidence |

Voice AI remains a research option until enough scoped buyer evidence and a safe, measured pilot exist. Do not treat this shortlist as exact market rank.

## Recurring demand refinement contract

**Weekly Monday research inside the existing combined AGESOMA/AI Engineer routine** (no separate task):

1. Reopen Workana, Upwork and LinkedIn listings and at least one first-party research source. Prefer items posted in the last 30 days; label older items historical rather than current. Target 3 relevant examples per platform if accessible, otherwise state sample limits.
2. Record for each: platform; original URL; title; **publication date vs date observed**; buyer problem; technologies; deliverables; buyer budget when disclosed and verified; contract type; competition/proposals if actually visible; risks; and quote/request status. Avoid scraping behind login, bypassing anti-bot controls or gathering personal contact information.
3. Group requirements semantically: workflow integration, RAG and reliability, permissioned agents, SaaS copilots, LLM quality/cost, voice. Deduplicate repeats and syndicated listings. Separate Workana/Upwork **commissioned project requests** from LinkedIn **job qualifications**.
4. Score each candidate service using 0–5 for **evidence breadth**, **specificity of buyer pain**, **demonstrable outcome**, **fit with reusable original code**, and **economically feasible scope**. Include source URLs and an explicit confidence rating. These are subjective decision scores, **not empirical frequency counts**. Missing budgets or permissions lower confidence.
5. Choose one bounded milestone for the **single active flagship**, not a new repository every Monday. Update proposed service copy or priorities only when cited evidence changes. Publish a reviewable market-evidence PR; never overwrite customer or current source code or auto-merge.
6. On Sunday compare client-facing SERVICES/CASE_STUDIES, real test evidence, Raphael's recruiter portfolio and the private CV. Public materials must have congruent skills, limitations and exact-SHA links; private interviews and learner answers stay private.
7. Report **market sample size**, the three most decision-relevant demand signals, winning offer, expected customer outcome, next verified build/audit acceptance gate, and uncertainty. If sites block access, say so; never fabricate listings or numbers.

**Business decision rule:** Job postings are discovery signals, not contracts or guaranteed ROI. Require original production-ready proof and scope-controlled economics before accepting risky customer deployment work.

## Evidence hygiene

Current examples were verified through publicly accessible indexed pages on 2026-11-04; visibility and the dates shown may drift. Sources are cited by direct links. No permission to contact, apply, place bids or use credentials is implied.
