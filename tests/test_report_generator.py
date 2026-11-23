"""Tests for generating simulated Markdown risk reports."""

import pytest

from src.report_generator import create_risk_table, save_risk_table


def get_valid_finding():
    return {
        "finding_id": "FIND-001",
        "risk_level": "Critical",
        "risk_score": 20,
        "title": "Test finding",
        "description": "Simulated test finding",
        "recommendation": "Apply a defensive control",
    }


def test_create_risk_table_creates_header_row():
    finding = get_valid_finding()

    risk_table = create_risk_table([finding])

    assert "| Finding ID | Risk Level | Risk Score | Threat / Finding | Impact | Mitigation |" in risk_table


def test_create_risk_table_creates_separator_row():
    finding = get_valid_finding()

    risk_table = create_risk_table([finding])

    assert "|---|---|---:|---|---|---|" in risk_table


def test_create_risk_table_includes_finding_details():
    finding = get_valid_finding()

    risk_table = create_risk_table([finding])

    assert "| FIND-001 | Critical | 20 | Test finding | Simulated test finding | Apply a defensive control |" in risk_table


def test_create_risk_table_includes_multiple_findings():
    first_finding = get_valid_finding()

    second_finding = {
        "finding_id": "FIND-002",
        "risk_level": "High",
        "risk_score": 12,
        "title": "Second test finding",
        "description": "Simulated second test finding",
        "recommendation": "Apply a defensive control",
    }

    risk_table = create_risk_table([first_finding, second_finding])

    assert "FIND-001" in risk_table
    assert "FIND-002" in risk_table


def test_create_risk_table_rejects_empty_findings():
    with pytest.raises(ValueError):
        create_risk_table([])


def test_create_risk_table_rejects_missing_required_key():
    finding = get_valid_finding()
    del finding["recommendation"]

    with pytest.raises(ValueError):
        create_risk_table([finding])


def test_save_risk_table_creates_markdown_file(tmp_path):
    finding = get_valid_finding()
    output_file = tmp_path / "reports" / "test-risk-report.md"

    saved_path = save_risk_table([finding], output_file)

    assert saved_path == output_file
    assert output_file.exists()

    report_text = output_file.read_text(encoding="utf-8")

    assert "| Finding ID | Risk Level | Risk Score | Threat / Finding | Impact | Mitigation |" in report_text
    assert "FIND-001" in report_text


def test_save_risk_table_creates_missing_parent_folder(tmp_path):
    finding = get_valid_finding()
    output_file = tmp_path / "new-folder" / "nested-folder" / "test-risk-report.md"

    saved_path = save_risk_table([finding], output_file)

    assert output_file.exists()
    assert saved_path == output_file