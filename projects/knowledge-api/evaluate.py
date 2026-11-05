"""Repeatable synthetic retrieval evaluation. No LLM calls or production claims."""

import json
from pathlib import Path

from retrieval import KnowledgeIndex


ROOT = Path(__file__).resolve().parent


def evaluate() -> dict[str, float | int]:
    index = KnowledgeIndex(ROOT / "corpus")
    cases = json.loads((ROOT / "eval_cases.json").read_text(encoding="utf-8"))
    known = [case for case in cases if case["expected_source"] is not None]
    unknown = [case for case in cases if case["expected_source"] is None]
    correct = sum(
        bool(hits := index.search(case["query"], top_k=1))
        and hits[0].source_id == case["expected_source"]
        for case in known
    )
    abstained = sum(not index.search(case["query"], top_k=1) for case in unknown)
    return {
        "total_cases": len(cases),
        "known_cases": len(known),
        "unknown_cases": len(unknown),
        "source_recall_at_1": round(correct / len(known), 4),
        "unknown_abstention_rate": round(abstained / len(unknown), 4),
    }


if __name__ == "__main__":
    result = evaluate()
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["source_recall_at_1"] < 0.8:
        raise SystemExit("Source recall@1 is below the demo threshold of 0.8")
    if result["unknown_abstention_rate"] < 1.0:
        raise SystemExit("Unknown-question abstention is below the demo threshold of 1.0")
