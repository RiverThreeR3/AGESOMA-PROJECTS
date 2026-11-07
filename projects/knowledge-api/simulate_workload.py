"""Reproducible fictional service-desk workload simulation.

This script executes the actual local KnowledgeIndex against synthetic messages.
It models handling time using declared assumptions; it does NOT measure customer
ROI, real accuracy, LLM capability, or third-party CRM/WhatsApp integration.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from retrieval import KnowledgeIndex


ROOT = Path(__file__).resolve().parent
CASES_PATH = ROOT / "simulations" / "workload_cases.json"
CORPUS = ROOT / "corpus"


def _positive_int(value: object, label: str) -> int:
    if type(value) is not int or value <= 0:
        raise ValueError(f"{label} must be a positive integer")
    return value


def validate_workload(payload: object) -> dict[str, Any]:
    """Fail closed on malformed or inconsistent modeling assumptions."""
    if not isinstance(payload, dict) or set(payload) != {
        "schema_version", "description", "scenarios", "cases"
    }:
        raise ValueError("Invalid workload schema")
    if payload["schema_version"] != 1 or not isinstance(payload["description"], str):
        raise ValueError("Invalid workload metadata")
    scenarios = payload["scenarios"]
    cases = payload["cases"]
    if not isinstance(scenarios, dict) or not scenarios:
        raise ValueError("Scenarios must be a nonempty mapping")
    if not isinstance(cases, list) or not cases:
        raise ValueError("Cases must be a nonempty list")
    for key, config in scenarios.items():
        if not isinstance(key, str) or not key:
            raise ValueError("Invalid scenario id")
        if not isinstance(config, dict) or set(config) != {
            "title", "manual_minutes_per_ticket", "review_minutes_per_supported_ticket"
        }:
            raise ValueError("Invalid scenario configuration")
        if not isinstance(config["title"], str) or not config["title"].strip():
            raise ValueError("Scenario title must be nonempty")
        baseline = _positive_int(config["manual_minutes_per_ticket"], "manual minutes")
        reviewed = _positive_int(
            config["review_minutes_per_supported_ticket"], "review minutes"
        )
        if reviewed >= baseline:
            raise ValueError("Review time must be lower than manual time")
    seen: set[str] = set()
    for case in cases:
        if not isinstance(case, dict) or set(case) != {
            "scenario", "id", "query", "expected_source", "expected_fragment"
        }:
            raise ValueError("Invalid case schema")
        if case["scenario"] not in scenarios:
            raise ValueError("Case uses unknown scenario")
        if not isinstance(case["id"], str) or not case["id"].strip():
            raise ValueError("Invalid case id")
        if case["id"] in seen:
            raise ValueError("Duplicate case id")
        seen.add(case["id"])
        if not isinstance(case["query"], str) or not 3 <= len(case["query"]) <= 500:
            raise ValueError("Invalid synthetic query")
        source, fragment = case["expected_source"], case["expected_fragment"]
        if (source is None) != (fragment is None):
            raise ValueError("Expected source and fragment must both be null or strings")
        if source is not None and (
            not isinstance(source, str) or not source.endswith(".md")
            or not isinstance(fragment, str) or not fragment.strip()
        ):
            raise ValueError("Invalid expected evidence")
    if any(not any(c["scenario"] == key for c in cases) for key in scenarios):
        raise ValueError("Every scenario requires at least one case")
    return payload


def run_simulation(
    workload: dict[str, Any] | None = None,
    index: KnowledgeIndex | None = None,
) -> dict[str, Any]:
    """Compare actual lexical output to synthetic labeled evidence requirements."""
    if workload is None:
        workload = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    validated = validate_workload(workload)
    if index is None:
        index = KnowledgeIndex(CORPUS)

    outcomes = {name: {
        "title": config["title"],
        "ticket_count": 0,
        "source_and_excerpt_matches": 0,
        "human_handoff_drafts": 0,
        "unsafe_or_mismatched_candidates": 0,
        "false_abstentions": 0,
        "assumed_manual_minutes": 0,
        "modeled_assisted_minutes": 0,
        "modeled_minutes_saved": 0,
        "manual_minutes_per_ticket": config["manual_minutes_per_ticket"],
        "review_minutes_per_supported_ticket": config["review_minutes_per_supported_ticket"],
        "modeled_time_reduction_percent": 0.0,
    } for name, config in validated["scenarios"].items()}
    detail = []

    for case in validated["cases"]:
        bucket = outcomes[case["scenario"]]
        bucket["ticket_count"] += 1
        baseline = bucket["manual_minutes_per_ticket"]
        reviewed = bucket["review_minutes_per_supported_ticket"]
        bucket["assumed_manual_minutes"] += baseline

        hits = index.search(case["query"], top_k=1)
        hit = hits[0] if hits else None
        expected_source = case["expected_source"]
        supported = expected_source is not None
        matched = bool(
            hit is not None and supported
            and hit.source_id == expected_source
            and case["expected_fragment"].casefold() in hit.excerpt.casefold()
        )
        unsafe_candidate = hit is not None and not matched
        false_abstention = hit is None and supported
        disposition = "cited_draft_for_human_review" if matched else "human_handoff_draft"

        if matched:
            bucket["source_and_excerpt_matches"] += 1
            bucket["modeled_assisted_minutes"] += reviewed
        else:
            bucket["human_handoff_drafts"] += 1
            bucket["modeled_assisted_minutes"] += baseline
        if unsafe_candidate:
            bucket["unsafe_or_mismatched_candidates"] += 1
        if false_abstention:
            bucket["false_abstentions"] += 1

        detail.append({
            "id": case["id"],
            "scenario": case["scenario"],
            "disposition": disposition,
            "expected_source": expected_source,
            "candidate_source": hit.source_id if hit else None,
            "source_and_excerpt_match": matched,
            "unsafe_or_mismatched_candidate": unsafe_candidate,
        })

    for bucket in outcomes.values():
        bucket["modeled_minutes_saved"] = (
            bucket["assumed_manual_minutes"] - bucket["modeled_assisted_minutes"]
        )
        bucket["modeled_time_reduction_percent"] = round(
            100 * bucket["modeled_minutes_saved"] / bucket["assumed_manual_minutes"], 2
        )

    return {
        "evidence_type": "FICTIONAL_WORKLOAD_EXECUTED_ON_REAL_LOCAL_CODE_WITH_ASSUMED_TIME_MODEL",
        "case_provenance": "Hand-authored development fixtures, NOT unseen holdout or real traffic",
        "external_integrations": "NONE: handoff and review are drafts only",
        "scenarios": outcomes,
        "case_details": detail,
    }


def markdown_report(result: dict[str, Any]) -> str:
    rows = [
        "# AGESOMA — Synthetic Business Workload Simulation",
        "",
        "**Synthetic case outcomes, not real-world customer results.** This executes the",
        "actual lexical retrieval code against authored fictional tickets. No LLM, CRM,",
        "n8n, WhatsApp, client deployment, real customer or third-party API is involved.",
        "",
        "| Workload | Unique authored tickets | Passage+source matches | Human handoff drafts | Unsafe/mismatched candidates | Modeled manual minutes | Modeled assisted minutes | Assumed minutes saved | Modeled time reduction |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["scenarios"].values():
        rows.append(
            f"| {item['title']} | {item['ticket_count']} | "
            f"{item['source_and_excerpt_matches']} | {item['human_handoff_drafts']} | "
            f"{item['unsafe_or_mismatched_candidates']} | "
            f"{item['assumed_manual_minutes']} | {item['modeled_assisted_minutes']} | "
            f"{item['modeled_minutes_saved']} | {item['modeled_time_reduction_percent']:.2f}% |"
        )
    rows.extend([
        "",
        "## Time assumptions (invented for scenario analysis)",
        "",
    ])
    for item in result["scenarios"].values():
        rows.append(
            f"- **{item['title']}:** manual = "
            f"{item['manual_minutes_per_ticket']} minutes/ticket; "
            f"cited draft reviewed by a person = "
            f"{item['review_minutes_per_supported_ticket']} minutes/ticket. "
            "All handoffs retain full manual handling time."
        )
    rows.extend([
        "",
        "A *passage+source match* means an exact expected substring was found in the",
        "correct fictional file, **not** that the answer is generally correct.",
        "Unsafe candidates are counted even though this test harness routes them",
        "to a manual draft using labels available only to the evaluator.",
        "",
        "Savings are arithmetic under chosen assumptions, **not measured time, money,",
        "ROI, productivity uplift, validation with clients or a deployable SLA**.",
        "The fixture questions are development tests and must never be called",
        "independent/blind evaluation or representative demand.",
    ])
    return "\n".join(rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    args = parser.parse_args()
    result = run_simulation()
    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(markdown_report(result))
    if any(
        bucket["unsafe_or_mismatched_candidates"]
        for bucket in result["scenarios"].values()
    ):
        raise SystemExit("Synthetic workload has unsafe or mismatched candidates")
