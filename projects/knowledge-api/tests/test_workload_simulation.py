"""Evidence-focused regression tests for the synthetic workload simulator."""

from copy import deepcopy

import pytest

from retrieval import Hit
from simulate_workload import (
    CASES_PATH,
    markdown_report,
    run_simulation,
    validate_workload,
)
import json


def sample() -> dict:
    return json.loads(CASES_PATH.read_text(encoding="utf-8"))


def test_all_author_fixtures_are_scored_and_accounted_for() -> None:
    result = run_simulation()
    assert set(result["scenarios"]) == {"support", "operations"}
    assert len(result["case_details"]) == 30
    assert len({c["id"] for c in result["case_details"]}) == 30
    for scenario in result["scenarios"].values():
        assert scenario["ticket_count"] == 15
        assert (
            scenario["source_and_excerpt_matches"]
            + scenario["human_handoff_drafts"]
            == scenario["ticket_count"]
        )
        assert scenario["unsafe_or_mismatched_candidates"] == 0
        assert scenario["modeled_minutes_saved"] == (
            scenario["assumed_manual_minutes"]
            - scenario["modeled_assisted_minutes"]
        )
        assert scenario["modeled_assisted_minutes"] >= 0


def test_results_are_deterministic_and_transparent() -> None:
    first = run_simulation()
    assert first == run_simulation()
    assert "FICTIONAL_WORKLOAD" in first["evidence_type"]
    assert "NOT unseen" in first["case_provenance"]
    report = markdown_report(first)
    assert "not real-world customer results" in report
    assert "not measured time" in report


@pytest.mark.parametrize("mutator", [
    lambda p: p["cases"].append(p["cases"][0].copy()),
    lambda p: p["scenarios"]["support"].update({"manual_minutes_per_ticket": -1}),
    lambda p: p["scenarios"]["support"].update({"review_minutes_per_supported_ticket": 6}),
    lambda p: p["cases"][0].update({"expected_fragment": None}),
    lambda p: p["cases"][0].update({"query": "x"}),
    lambda p: p["cases"][0].update({"scenario": "unknown"}),
])
def test_invalid_assumptions_and_cases_rejected(mutator) -> None:
    data = deepcopy(sample())
    mutator(data)
    with pytest.raises(ValueError):
        validate_workload(data)


def test_unknown_query_with_wrong_candidate_is_not_counted_as_saving() -> None:
    data = sample()
    data["cases"] = [next(case for case in data["cases"] if case["id"] == "s11")]
    data["scenarios"] = {"support": data["scenarios"]["support"]}

    class MisleadingIndex:
        def search(self, query: str, *, top_k: int):
            return [Hit(
                source_id="refunds.md",
                title="Refund policy",
                line=2,
                excerpt="Customers may request a refund within 30 days of purchase.",
                score=1.0,
            )]

    report = run_simulation(workload=data, index=MisleadingIndex())
    record = report["scenarios"]["support"]
    assert record["unsafe_or_mismatched_candidates"] == 1
    assert record["source_and_excerpt_matches"] == 0
    assert record["human_handoff_drafts"] == 1
    assert record["modeled_minutes_saved"] == 0
