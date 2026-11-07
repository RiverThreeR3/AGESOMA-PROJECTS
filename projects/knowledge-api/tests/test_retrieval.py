"""Deterministic, dependency-free retrieval unit tests."""

from pathlib import Path

import pytest

from evaluate import evaluate
from retrieval import KnowledgeIndex, tokenize


CORPUS = Path(__file__).resolve().parents[1] / "corpus"


def test_normalization_and_word_boundaries() -> None:
    assert tokenize("Café PAYMENT payments") == frozenset(
        {"cafe", "payment", "payments"}
    )


def test_retrieval_is_deterministic() -> None:
    index = KnowledgeIndex(CORPUS)
    assert index.search("invoices generated") == index.search("invoices generated")


def test_rejects_out_of_range_top_k() -> None:
    index = KnowledgeIndex(CORPUS)
    with pytest.raises(ValueError):
        index.search("invoices", top_k=0)


def test_rejects_empty_corpus(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="empty"):
        KnowledgeIndex(tmp_path)


def test_rejects_oversized_document(tmp_path: Path) -> None:
    (tmp_path / "large.md").write_text("A" * 17_000, encoding="utf-8")
    with pytest.raises(ValueError, match="size limit"):
        KnowledgeIndex(tmp_path)


def test_synthetic_evaluation_passes_explicit_gates() -> None:
    result = evaluate()
    assert result["total_cases"] == 12
    assert result["known_cases"] == 9
    assert result["unknown_cases"] == 3
    assert result["source_recall_at_1"] >= 0.8
    assert result["unknown_abstention_rate"] == 1.0
    assert result["near_domain_cases"] == 8
    assert result["near_domain_abstention_rate"] == 1.0
