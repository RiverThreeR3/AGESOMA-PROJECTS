"""Evaluation-set integrity checks; no provider or model calls."""

import pytest

from evaluate import validate_cases


VALID = [
    {"id": "known", "query": "What is the policy?", "expected_source": "policy.md"},
    {"id": "unknown", "query": "What is the weather?", "expected_source": None},
]


def test_balanced_cases_are_accepted() -> None:
    assert validate_cases(VALID) == VALID


@pytest.mark.parametrize("cases", [
    [],
    {},
    [VALID[0]],
    [VALID[1]],
    [VALID[0], VALID[0], VALID[1]],
    [{**VALID[0], "query": ""}, VALID[1]],
    [{**VALID[0], "expected_source": ""}, VALID[1]],
    [{**VALID[0], "unexpected": True}, VALID[1]],
])
def test_invalid_cases_fail_closed(cases: object) -> None:
    with pytest.raises(ValueError):
        validate_cases(cases)
