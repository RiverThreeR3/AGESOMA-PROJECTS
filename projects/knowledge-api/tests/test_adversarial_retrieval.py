"""Adversarial lexical-retrieval regressions using only synthetic corpus data.

These are deterministic safety checks, not independent holdout measurements or
evidence of answer correctness on real user queries.
"""

from pathlib import Path

import pytest

from retrieval import KnowledgeIndex, tokenize


CORPUS = Path(__file__).resolve().parents[1] / "corpus"


@pytest.mark.parametrize(
    "query",
    [
        "quasar nebula astrophysics",
        "xylophone zirconium zeppelin",
        "the and or with",
    ],
)
def test_unrelated_or_stopword_only_queries_abstain(query: str) -> None:
    index = KnowledgeIndex(CORPUS)
    assert index.search(query, top_k=1) == []


def test_repeating_query_words_does_not_inflate_retrieval_score() -> None:
    index = KnowledgeIndex(CORPUS)
    original = index.search("refund", top_k=1)
    repeated = index.search("refund refund refund", top_k=1)
    assert repeated == original


def test_tokenization_removes_repeated_terms() -> None:
    assert tokenize("refund refund REFUND") == frozenset({"refund"})
