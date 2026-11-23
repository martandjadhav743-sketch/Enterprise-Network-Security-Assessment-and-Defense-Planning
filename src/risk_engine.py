"""Calculate simulated risk priorities for defensive network findings."""

VALID_SCORES = {1, 2, 3, 4, 5}


def calculate_risk_score(likelihood, impact):
    """Calculate a simple risk score from likelihood and impact."""
    if likelihood not in VALID_SCORES:
        raise ValueError(f"Likelihood must be one of {sorted(VALID_SCORES)}: {likelihood}")

    if impact not in VALID_SCORES:
        raise ValueError(f"Impact must be one of {sorted(VALID_SCORES)}: {impact}")

    return likelihood * impact


def calculate_risk_level(risk_score):
    """Convert a risk score into a priority level."""
    if not isinstance(risk_score, int):
        raise TypeError("Risk score must be an integer.")

    if risk_score >= 20:
        return "Critical"
    if risk_score >= 12:
        return "High"
    if risk_score >= 6:
        return "Medium"

    return "Low"


def analyze_finding(finding):
    """Add a calculated risk score and priority level to one finding."""
    likelihood = finding.get("likelihood")
    impact = finding.get("impact")

    risk_score = calculate_risk_score(likelihood, impact)
    risk_level = calculate_risk_level(risk_score)

    analyzed_finding = finding.copy()
    analyzed_finding["risk_score"] = risk_score
    analyzed_finding["risk_level"] = risk_level

    return analyzed_finding


def analyze_findings(findings):
    """Analyze every finding and return them sorted by highest risk."""
    analyzed = [analyze_finding(finding) for finding in findings]
    return sorted(analyzed, key=lambda finding: finding["risk_score"], reverse=True)