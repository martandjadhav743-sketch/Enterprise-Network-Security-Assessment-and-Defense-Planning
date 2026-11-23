"""Tests for the simulated risk-scoring engine."""

import pytest

from src.risk_engine import (
    calculate_risk_level,
    calculate_risk_score,
    analyze_finding,
    analyze_findings,
)


def test_calculate_risk_score_multiplies_likelihood_and_impact():
    assert calculate_risk_score(4, 5) == 20
    assert calculate_risk_score(3, 5) == 15
    assert calculate_risk_score(3, 4) == 12


def test_calculate_risk_level_returns_critical_for_high_scores():
    assert calculate_risk_level(20) == "Critical"
    assert calculate_risk_level(25) == "Critical"


def test_calculate_risk_level_returns_high_for_medium_high_scores():
    assert calculate_risk_level(12) == "High"
    assert calculate_risk_level(19) == "High"


def test_calculate_risk_level_returns_medium_for_medium_scores():
    assert calculate_risk_level(6) == "Medium"
    assert calculate_risk_level(11) == "Medium"


def test_calculate_risk_level_returns_low_for_low_scores():
    assert calculate_risk_level(1) == "Low"
    assert calculate_risk_level(5) == "Low"


def test_calculate_risk_score_rejects_invalid_likelihood():
    with pytest.raises(ValueError):
        calculate_risk_score(0, 5)


def test_calculate_risk_score_rejects_invalid_impact():
    with pytest.raises(ValueError):
        calculate_risk_score(4, 6)


def test_analyze_finding_adds_risk_score_and_level():
    finding = {
        "finding_id": "FIND-TEST",
        "title": "Test finding",
        "description": "Simulated test finding",
        "recommendation": "Apply a defensive control",
        "likelihood": 4,
        "impact": 5,
    }

    result = analyze_finding(finding)

    assert result["risk_score"] == 20
    assert result["risk_level"] == "Critical"


def test_analyze_findings_sorts_by_highest_risk_score():
    findings = [
        {
            "finding_id": "FIND-LOW",
            "title": "Low-risk finding",
            "description": "Simulated low-risk finding",
            "recommendation": "Apply a defensive control",
            "likelihood": 1,
            "impact": 2,
        },
        {
            "finding_id": "FIND-CRITICAL",
            "title": "Critical-risk finding",
            "description": "Simulated critical-risk finding",
            "recommendation": "Apply a defensive control",
            "likelihood": 5,
            "impact": 5,
        },
    ]

    results = analyze_findings(findings)

    assert results[0]["finding_id"] == "FIND-CRITICAL"
    assert results[1]["finding_id"] == "FIND-LOW"