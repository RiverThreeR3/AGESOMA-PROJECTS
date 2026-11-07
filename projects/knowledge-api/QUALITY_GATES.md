# Knowledge API — Evidence and acceptance gates

This document records **engineering requirements and limitations** for the
deterministic, synthetic-corpus baseline. It is not a claim of enterprise
deployment, generative RAG, real-user quality or customer value.

## Problem addressed by this increment

The original lexical scorer could return a passage after matching just two
topical words from a much broader question, including unsupported near-domain
queries. A citation to a source file does not make that source responsive.

The revised baseline requires:
- at least two matching content tokens when the question has multiple tokens;
- at least 60% of the query's distinct non-stop-word tokens within **one**
  cited passage, not scattered across documents;
- all numeric tokens present in the question to match the passage exactly.

These are **intentionally conservative lexical guardrails**, not calibrated
probabilities or semantic entailment checks. They can withhold a valid answer
(false abstention) and can still return irrelevant passages whose vocabulary
overlaps sufficiently. In particular, dates in prose and spelling variants
are not semantically normalized. The numeric rule prevents simple mismatches
but does not perform arithmetic, temporal reasoning or contradiction
detection.

The two public endpoints have distinct contracts: `POST /v1/search` accepts
strict integer `top_k` (1–5), while `POST /v1/answer` accepts only `query`.
Unsupported extra answer fields no longer appear to be silently honored.
Control/format characters in queries are rejected. These validation checks
are not authorization, ingress request-size limits or abuse prevention.

## Reproduce the evaluation

From `projects/knowledge-api`, with the pinned development dependencies:

```sh
python -m pytest -q
ruff check .
python evaluate.py
```

Two distinct synthetic datasets are used:
- `eval_cases.json`: the original nine source-known and three
  out-of-domain questions; reports source recall@1 and basic abstention.
- `near_domain_cases.json`: newly authored, deliberately difficult
  **unsupported** questions (including numeric mismatches and topical noise).
  Reports regression-only near-domain abstention.

The gate for the new set is 100% abstention on these **known authored fixtures**,
not a 100% real-world accuracy claim. The same cases are included in automated
tests, so they are not a blind holdout. Each reported result needs a link to CI
for the **exact commit SHA**; otherwise the status is `not verified`.

## Enterprise release blockers

1. **Authentication/authorization and tenant isolation:** currently absent.
   Never expose real company documents with this demo API.
2. **Ingestion and provenance:** only five fictional, fixed Markdown files.
   Define a trusted ingestion/approval/deletion process before customer use.
3. **Independent evaluation:** collect separately labeled, truly unseen
   ambiguous and adversarial queries; measure unsupported-answer rate and
   false-abstention cost. Do not tune on the final holdout.
4. **Semantic retrieval/generation:** not present. Add embeddings/LLMs only
   after side-by-side comparison with the deterministic baseline on the
   same frozen evaluation set.
5. **Service security/operations:** real API keys/SSO, per-user permissions,
   ingress limits, request budgets, redacted tracing, concurrency/load tests,
   deployment rollback and threat modeling remain to be done.
6. **Commercial validation:** no independently observed customer pilots,
   delivered contracts, measured operating benefits or production SLAs.

A passed CI run verifies the stated test suite, not production acceptance.
