# Open-Source Repository Audit — AGESOMA-PROJECTS

**Review date:** 2026-11-04  
**Scope:** public AI Engineering services and case studies, with one active market-selected flagship project carried across weeks as needed.  
**Current evidence (2026-11-04):** the `main` branch contains only the initial README. The documentation lives in PR #1, while the original Knowledge API application, its dependency definitions and tests are **under review in PR #2**. No current-commit CI, runtime integration or production deployment was independently executed or verified in this particular market/source audit. The dependencies below were reviewed as candidates; the code in PR #2 must be separately inspected before marking any candidate as implemented.

## Source repository candidates

| Candidate GitHub repository | License inspected in GitHub | Potential function | Decision | Key gate before using |
| --- | --- | --- | --- | --- |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | MIT | Typed HTTP APIs, validation, OpenAPI endpoints | **Candidate — dependency** | Use a pinned compatible version, add security controls and integration tests |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | PostgreSQL-style permissive license | Vector search in PostgreSQL for RAG | **Candidate — dependency** | Verify local Postgres extension compatibility, indexing, permissions and tenant isolation |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | MIT | Stateful, tool-using agents with control over steps | **Conditional candidate** | Only when stateful orchestration is needed; implement tool authorization and test failure/retries |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | Apache-2.0 | LLM/RAG/agent evaluation metrics | **Candidate — development/test dependency** | Pin a version, use test data, review telemetry and any paid cloud features separately; avoid claiming real-model measurements when using mocks |
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | MIT | Standardized MCP tool servers/clients | **Conditional candidate** | Use only for job-driven MCP need; audit tool permissions, transports and input validation |

Sources: public upstream GitHub README and LICENSE / LICENSE.md files were read during the 2026-11-04 audit. Recheck the exact dependency version and its dependency tree before using or redistributing software; this is not a vulnerability scan or full supply-chain review.

## Recommended pilot

For a **RAG Knowledge API**, start with:

- FastAPI for the public API;
- PostgreSQL + pgvector for vector search only if retrieval evaluation warrants it;
- a small deterministic keyword-retrieval baseline before any LLM dependency;
- DeepEval or a small transparent evaluation harness for measured retrieval and answer quality.

Do not add LangGraph or MCP by default to a pure RAG API. Add them only when a verified buyer requirement needs stateful tool workflows or MCP. Make a separate vendor/provider decision for embeddings/LLM, including cost and data handling.

## Public-source policy

1. Reuse a well-maintained dependency instead of copying an entire GitHub repository into the portfolio.
2. Check licenses and preserve copyright/attribution notices if copying or adapting code; public availability **does not** mean blanket permission to copy.
3. Never present upstream work as the AGESOMA-PROJECTS team's original development. Attribute origins and publish original engineering additions with tests and clear authorship.
4. Store source code for the weekly project in **one public repository**, preferentially AGESOMA-PROJECTS, and link it from the Raphael AIEngineer portfolio without duplicating the codebase.
5. No access, modification, or dependency on the private `RiverThreeR3/AGESOMA` repository in this workflow.
6. New real dependencies must appear in pinned requirement/lock files and reproducible CI. A name in this audit does NOT imply installation or working integration.
7. If a real job-demand audit ranks another stack higher, redo this audit and select better repositories for that project, recording rationale and tradeoffs.

## Current verdict

**No new dependency installation, test run or real customer integration verified by this documentation audit.** The Knowledge API code exists in an open PR and requires exact-SHA dependency, license, test and deployment review. Future work must record the chosen sources, pinned versions, license notices and reproducible CI evidence.
