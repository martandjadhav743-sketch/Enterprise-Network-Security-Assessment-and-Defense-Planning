"""Load and validate the simulated network assessment data."""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FOLDER = PROJECT_ROOT / "data"

REQUIRED_COMPANY_KEYS = {"company", "business_systems"}
REQUIRED_ASSET_KEYS = {"assessment", "network_zones", "assets"}


def load_json_file(file_name):
    """Load a JSON file from the project data folder."""
    file_path = DATA_FOLDER / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"Mock data file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as json_file:
        return json.load(json_file)


def validate_company_profile(data):
    """Check that the mock company profile has the expected sections."""
    if not isinstance(data, dict):
        raise ValueError("Company profile must be a JSON object.")

    missing_keys = REQUIRED_COMPANY_KEYS - data.keys()
    if missing_keys:
        raise ValueError(f"Company profile is missing: {', '.join(sorted(missing_keys))}")

    if not isinstance(data["business_systems"], list):
        raise ValueError("business_systems must be a list.")

    return data


def validate_network_assets(data):
    """Check that the mock network asset inventory has the expected sections."""
    if not isinstance(data, dict):
        raise ValueError("Network asset inventory must be a JSON object.")

    missing_keys = REQUIRED_ASSET_KEYS - data.keys()
    if missing_keys:
        raise ValueError(f"Network asset inventory is missing: {', '.join(sorted(missing_keys))}")

    if not isinstance(data["network_zones"], list):
        raise ValueError("network_zones must be a list.")

    if not isinstance(data["assets"], list):
        raise ValueError("assets must be a list.")

    return data


def load_company_profile():
    """Load and validate the mock company profile."""
    return validate_company_profile(load_json_file("mock_company_profile.json"))


def load_network_assets():
    """Load and validate the mock network asset inventory."""
    return validate_network_assets(load_json_file("mock_network_assets.json"))