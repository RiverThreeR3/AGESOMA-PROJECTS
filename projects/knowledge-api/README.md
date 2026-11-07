# Knowledge API — Extractive Retrieval Baseline

**Status:** Extractive baseline in [Knowledge API PR #2](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2), not merged or deployed. On 2026-11-07, [GitHub Actions run 42369952198](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/actions/runs/42369952198) passed on reviewed revision `8431180a18dd6e9391a8473acad20259b69b0eb3`: **39 pytest cases passed** (one dependency deprecation warning), Ruff passed, synthetic source recall@1 = **1.0 on 9 authored cases**, synthetic abstention = **1.0 on 3 authored cases**, and Docker build/health smoke passed. These are small, authored fixtures, **not independent held-out accuracy or a real-model evaluation**. Any later PR revision requires its **own exact-SHA CI check**. No production deployment or complete RAG system is claimed.

## Engineering problem

Document question-answering interfaces need a reliable way to retrieve relevant text, show where an answer comes from, and decline unsupported queries. This project implements a **small, deterministic extractive baseline** to make those behaviors directly inspectable before adding embeddings, vector search or an LLM.

The current implementation uses **five fictional Markdown policy documents**. It provides typed FastAPI endpoints, lexical retrieval, verbatim source passages, line-level citations, explicit abstention and synthetic regression/evaluation cases. The code does not claim real-document ingestion, production authorization, customer outcomes or generative answer quality.

## Architecture

```text
HTTP client
  |-- POST /v1/search (query, top_k)
  |-- POST /v1/answer (query)
  v
FastAPI / typed input validation
  v
Fixed approved synthetic Markdown corpus
  v
Unicode normalization -> whole-word lexical scoring (IDF)
  v
Extractive source passage and source file + line citation
  |-- answer found: verbatim document line
  '-- no matching evidence: explicit abstention
```

**No LLM, embedding model, pgvector, agents, file-upload endpoint, external side effects, or caller-controlled file paths.** The API runs locally and operates on five fictional policy documents. Source line numbers refer to committed Markdown lines. Citation does not imply that the best-matching passage fully answers every question.

## Run locally

Requirements: Python 3.12+.

```bash
cd projects/knowledge-api
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
uvicorn app:app --reload
```

On Windows, activate with `.venv\Scripts\activate`.

```bash
curl -sS http://127.0.0.1:8000/healthz
curl -sS http://127.0.0.1:8000/v1/answer \
  -H "Content-Type: application/json" \
  -d '{"query":"When do password reset links expire?"}'
```

Expected answer contains `Password reset links expire after 15 minutes.`, `passwords.md`, and source line `3`.

API schema and browser docs: `http://127.0.0.1:8000/docs`.

## Reproduce tests and synthetic evaluation

```bash
cd projects/knowledge-api
python -m pytest -q
ruff check .
python evaluate.py
```

The 12 manually authored **synthetic evaluation cases** include 9 known-source questions and 3 out-of-domain questions. Metrics are:
- `source_recall_at_1`: fraction of known questions whose top retrieved source matches the expected source;
- `unknown_abstention_rate`: fraction of out-of-domain questions receiving no retrieval results.

Observed results in GitHub Actions run 41942623996: source_recall_at_1 = 1.0; unknown_abstention_rate = 1.0. The CI gates are `source_recall_at_1 >= 0.8` and `unknown_abstention_rate == 1.0`. These cases were authored for the demo; they are **not a held-out independent benchmark** and do not establish real-world accuracy, hallucination rate, model performance or business outcomes. Some unrelated questions may still match common corpus terms and return an unsupported passage.

## Docker

```bash
cd projects/knowledge-api
docker build -t agesoma-knowledge-api:dev .
docker run --rm -p 8000:8000 agesoma-knowledge-api:dev
```

The container runs as a non-root user. GitHub Actions includes dependency installation, Ruff, pytest, the synthetic evaluation, compilation, Docker build, and a `/healthz` smoke test.

## Security boundaries and limitations

- Public demo with **no authentication or multi-tenant security**: never deploy with real/private documents or expose to the internet without authentication, authorization, rate limits, logging safeguards and independent security review.
- Corpus is fixed at build time and includes only explicitly authored fictional content; requests cannot upload files or select filesystem paths.
- Output is verbatim extractive text, not an LLM response; no execution of instructions contained in user queries and no tool privileges.
- Input schema rejects unknown fields, limits length to 500 characters and top_k to 1–5. Reverse-proxy request size limits are not implemented.
- No PDF parsing, chunking strategy across document formats, vector similarity, tenancy, RBAC, model costs, p95 latency measurements, telemetry, persistence, CI deployment or real-model tests.
- Synthetic texts may be reused for this project; upstream FastAPI is distributed under the MIT License. **No licensing grant for the original AGESOMA source code is implied by public GitHub visibility.** Repository owner should choose an explicit project license before external redistribution or cloning for commercial purposes.

## Next audited increment

1. Confirm tests, Docker smoke and evaluation in GitHub Actions at the PR commit.
2. Perform failure analysis with additional adversarial/ambiguous questions and a separately authored evaluation set.
3. Add a benchmarked pgvector/embedding retrieval option only if it improves the baseline and maintain documented abstention and citations.
4. Add PDF ingestion and isolated access controls only after defining threat model and acceptance tests.

## Attribution

API framework: [FastAPI](https://github.com/fastapi/fastapi) (MIT). The sample corpus, retrieval logic and evaluation setup were authored specifically for this project. No external repository code was copied into this implementation.
