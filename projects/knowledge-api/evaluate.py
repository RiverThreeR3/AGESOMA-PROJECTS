"""Repeatable synthetic retrieval evaluation. No LLM calls or production claims."""

import json
from pathlib import Path

from retrieval import KnowledgeIndex


ROOT = Path(__file__).resolve().parent


def validate_cases(cases: object) -> list[dict[str, str | None]]:
    """Reject invalid or unbalanced evaluation sets before calculating scores."""
    if not isinstance(cases, list) or not cases:
        raise ValueError("Evaluation cases must be a nonempty list")
    seen: set[str] = set()
    known = 0
    unknown = 0
    for case in cases:
        if not isinstance(case, dict) or set(case) != {"id", "query", "expected_source"}:
            raise ValueError("Each case requires exactly id, query and expected_source")
        if any(not isinstance(case[key], str) or not case[key].strip() for key in ("id", "query")):
            raise ValueError("Case id and query must be nonempty strings")
        if case["id"] in seen:
            raise ValueError("Duplicate evaluation case id")
        seen.add(case["id"])
        source = case["expected_source"]
        if source is None:
            unknown += 1
        elif isinstance(source, str) and source.strip():
            known += 1
        else:
            raise ValueError("expected_source must be a nonempty string or null")
    if not known or not unknown:
        raise ValueError("Evaluation must include known and unknown questions")
    return cases


def evaluate() -> dict[str, float | int]:
    index = KnowledgeIndex(ROOT / "corpus")
    cases = validate_cases(json.loads((ROOT / "eval_cases.json").read_text(encoding="utf-8")))
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
