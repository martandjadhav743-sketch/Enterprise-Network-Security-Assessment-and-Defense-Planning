"""Tests for loading simulated JSON data."""

import json

import pytest

from src.data_loader import load_json_file


def test_load_json_file_reads_valid_json(tmp_path):
    json_file = tmp_path / "valid.json"

    json_file.write_text(
        json.dumps({"company_name": "Test Company"}),
        encoding="utf-8",
    )

    result = load_json_file(json_file)

    assert result == {"company_name": "Test Company"}


def test_load_json_file_reads_nested_json(tmp_path):
    json_file = tmp_path / "nested.json"

    json_file.write_text(
        json.dumps(
            {
                "company": {
                    "name": "Test Company",
                    "industry": "Technology",
                }
            }
        ),
        encoding="utf-8",
    )

    result = load_json_file(json_file)

    assert result["company"]["name"] == "Test Company"
    assert result["company"]["industry"] == "Technology"


def test_load_json_file_rejects_missing_file(tmp_path):
    missing_file = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError):
        load_json_file(missing_file)


def test_load_json_file_rejects_invalid_json(tmp_path):
    invalid_file = tmp_path / "invalid.json"

    invalid_file.write_text("{not valid json", encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        load_json_file(invalid_file)

from src.data_loader import (
    load_company_profile,
    load_network_assets,
    validate_company_profile,
    validate_network_assets,
)


def test_validate_company_profile_accepts_valid_data():
    company_profile = {
        "company": {
            "name": "Test Company",
            "industry": "Technology",
        },
        "business_systems": [
            {
                "system_name": "Customer Portal",
                "criticality": "High",
            }
        ],
    }

    result = validate_company_profile(company_profile)

    assert result == company_profile


def test_validate_company_profile_rejects_missing_company():
    company_profile = {
        "business_systems": []
    }

    with pytest.raises(ValueError):
        validate_company_profile(company_profile)


def test_validate_company_profile_rejects_missing_business_systems():
    company_profile = {
        "company": {
            "name": "Test Company",
        }
    }

    with pytest.raises(ValueError):
        validate_company_profile(company_profile)


def test_validate_company_profile_rejects_non_list_business_systems():
    company_profile = {
        "company": {
            "name": "Test Company",
        },
        "business_systems": "not a list",
    }

    with pytest.raises(ValueError):
        validate_company_profile(company_profile)


def test_validate_network_assets_accepts_valid_data():
    network_assets = {
        "assessment": {
            "assessment_name": "Simulated Assessment",
        },
        "network_zones": [
            {
                "zone_name": "Corporate LAN",
            }
        ],
        "assets": [
            {
                "asset_name": "Web Server",
            }
        ],
    }

    result = validate_network_assets(network_assets)

    assert result == network_assets


def test_validate_network_assets_rejects_missing_assessment():
    network_assets = {
        "network_zones": [],
        "assets": [],
    }

    with pytest.raises(ValueError):
        validate_network_assets(network_assets)


def test_validate_network_assets_rejects_missing_network_zones():
    network_assets = {
        "assessment": {},
        "assets": [],
    }

    with pytest.raises(ValueError):
        validate_network_assets(network_assets)


def test_validate_network_assets_rejects_missing_assets():
    network_assets = {
        "assessment": {},
        "network_zones": [],
    }

    with pytest.raises(ValueError):
        validate_network_assets(network_assets)


def test_validate_network_assets_rejects_non_list_network_zones():
    network_assets = {
        "assessment": {},
        "network_zones": "not a list",
        "assets": [],
    }

    with pytest.raises(ValueError):
        validate_network_assets(network_assets)


def test_validate_network_assets_rejects_non_list_assets():
    network_assets = {
        "assessment": {},
        "network_zones": [],
        "assets": "not a list",
    }

    with pytest.raises(ValueError):
        validate_network_assets(network_assets)


def test_load_company_profile_loads_project_data():
    company_profile = load_company_profile()

    assert "company" in company_profile
    assert "business_systems" in company_profile
    assert isinstance(company_profile["business_systems"], list)


def test_load_network_assets_loads_project_data():
    network_assets = load_network_assets()

    assert "assessment" in network_assets
    assert "network_zones" in network_assets
    assert "assets" in network_assets
    assert isinstance(network_assets["network_zones"], list)
    assert isinstance(network_assets["assets"], list)