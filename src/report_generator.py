"""Generate a Markdown risk table from simulated security findings."""

from pathlib import Path

RISK_TABLE_HEADERS = [
    "Finding ID",
    "Risk Level",
    "Risk Score",
    "Threat / Finding",
    "Impact",
    "Mitigation",
]


def create_risk_table(findings):
    """Create a Markdown table showing findings sorted by risk."""
    if not findings:
        raise ValueError("No findings were provided for the risk table.")

    lines = []
    lines.append("| " + " | ".join(RISK_TABLE_HEADERS) + " |")
    lines.append("|---|---|---:|---|---|---|")

    for finding in findings:
        required_keys = {
            "finding_id",
            "risk_level",
            "risk_score",
            "title",
            "description",
            "recommendation",
        }

        missing_keys = required_keys - finding.keys()
        if missing_keys:
            raise ValueError(
                f"Finding {finding.get('finding_id', 'unknown')} is missing: "
                f"{', '.join(sorted(missing_keys))}"
            )

        lines.append(
            "| "
            + finding["finding_id"]
            + " | "
            + finding["risk_level"]
            + " | "
            + str(finding["risk_score"])
            + " | "
            + finding["title"]
            + " | "
            + finding["description"]
            + " | "
            + finding["recommendation"]
            + " |"
        )

    return "\n".join(lines)


def save_risk_table(findings, output_path):
    """Save the Markdown risk table to a file."""
    risk_table = create_risk_table(findings)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(risk_table, encoding="utf-8")

    return output_path