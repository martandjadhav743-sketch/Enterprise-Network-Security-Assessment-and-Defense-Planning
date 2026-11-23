"""Tests for the simulated network security assessment report."""

import pytest

from src.assessment_report import (
    count_risk_levels,
    create_assessment_report,
    save_assessment_report,
)


def test_count_risk_levels_counts_each_level():
    findings = [
        {"risk_level": "Critical"},
        {"risk_level": "High"},
        {"risk_level": "High"},
        {"risk_level": "Medium"},
        {"risk_level": "Low"},
    ]

    counts = count_risk_levels(findings)

    assert counts == {
        "Critical": 1,
        "High": 2,
        "Medium": 1,
        "Low": 1,
    }


def test_count_risk_levels_returns_zero_counts_for_empty_findings():
    counts = count_risk_levels([])

    assert counts == {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0,
    }


def test_count_risk_levels_rejects_unknown_risk_level():
    findings = [
        {"risk_level": "Unknown"}
    ]

    with pytest.raises(KeyError):
        count_risk_levels(findings)


def test_create_assessment_report_includes_title():
    report = create_assessment_report()

    assert report.startswith("# Network Security Assessment Report")


def test_create_assessment_report_includes_simulated_notice():
    report = create_assessment_report()

    assert "## Simulated Assessment Notice" in report
    assert "simulated" in report.lower()


def test_create_assessment_report_includes_executive_summary():
    report = create_assessment_report()

    assert "## Executive Summary" in report
    assert "simulated findings" in report


def test_create_assessment_report_includes_scope():
    report = create_assessment_report()

    assert "## Assessment Scope" in report
    assert "- Internal LAN" in report
    assert "- Guest Wi-Fi" in report


def test_create_assessment_report_includes_network_overview():
    report = create_assessment_report()

    assert "## Network Overview" in report
    assert "network zones" in report
    assert "assets" in report


def test_create_assessment_report_includes_risk_method():
    report = create_assessment_report()

    assert "## Risk Assessment Method" in report
    assert "likelihood multiplied by impact" in report
    assert "- Critical: risk score of 20 or higher" in report


def test_create_assessment_report_includes_risk_table():
    report = create_assessment_report()

    assert "## Findings and Risk Table" in report
    assert "| Finding ID | Risk Level | Risk Score | Threat / Finding | Impact | Mitigation |" in report


def test_create_assessment_report_includes_defensive_controls():
    report = create_assessment_report()

    assert "## Recommended Defensive Controls" in report
    assert "Segment guest Wi-Fi from all internal networks." in report
    assert "Require multi-factor authentication for administrative access." in report


def test_create_assessment_report_includes_remediation_priorities():
    report = create_assessment_report()

    assert "## Remediation Priorities" in report
    assert "| 1 | FIND-001 | Isolate guest Wi-Fi from internal systems |" in report
    assert "| 2 | FIND-002 | Require MFA for administrative access |" in report


def test_create_assessment_report_includes_conclusion():
    report = create_assessment_report()

    assert "## Conclusion" in report
    assert "network segmentation" in report
    assert "access controls" in report


def test_save_assessment_report_creates_markdown_file(tmp_path):
    output_file = tmp_path / "reports" / "test-assessment-report.md"

    saved_path = save_assessment_report(output_file)

    assert saved_path == output_file
    assert output_file.exists()

    report_text = output_file.read_text(encoding="utf-8")

    assert report_text.startswith("# Network Security Assessment Report")
    assert "## Executive Summary" in report_text
    assert "## Findings and Risk Table" in report_text


def test_save_assessment_report_creates_missing_parent_folder(tmp_path):
    output_file = tmp_path / "new-folder" / "nested-folder" / "test-assessment-report.md"

    saved_path = save_assessment_report(output_file)

    assert output_file.exists()
    assert saved_path == output_file