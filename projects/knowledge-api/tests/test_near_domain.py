"""Near-domain regression probes using only fictional, authored questions.

These cases are engineering regression tests, NOT an independent unseen
benchmark or measured production false-answer rate.
"""

import json
from pathlib import Path

import pytest

from retrieval import KnowledgeIndex


ROOT = Path(__file__).resolve().parents[1]
CASES = json.loads((ROOT / "near_domain_cases.json").read_text(encoding="utf-8"))


@pytest.mark.parametrize("case", CASES, ids=[case["id"] for case in CASES])
def test_unsupported_near_domain_questions_abstain(case: dict[str, str]) -> None:
    index = KnowledgeIndex(ROOT / "corpus")
    assert index.search(case["query"], top_k=1) == []


@pytest.mark.parametrize(
    ("query", "source"),
    [
        ("When do password reset links expire?", "passwords.md"),
        ("When are invoices generated each month?", "invoices.md"),
        ("How many calendar days are allowed for invoice corrections?", "invoices.md"),
        ("What approval is required for production access?", "access.md"),
    ],
)
def test_supported_document_questions_remain_retrievable(
    query: str, source: str
) -> None:
    index = KnowledgeIndex(ROOT / "corpus")
    result = index.search(query, top_k=1)
    assert result and result[0].source_id == source
