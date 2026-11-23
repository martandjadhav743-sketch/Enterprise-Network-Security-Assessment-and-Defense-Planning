"""Generate the simulated network security assessment report."""

from pathlib import Path

from src.report_generator import create_risk_table
from src.data_loader import load_company_profile, load_network_assets, load_json_file
from src.risk_engine import analyze_findings


def count_risk_levels(findings):
    """Count findings by risk level."""
    counts = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0,
    }

    for finding in findings:
        risk_level = finding["risk_level"]
        counts[risk_level] += 1

    return counts


def create_assessment_report():
    """Create the complete simulated assessment report."""
    company = load_company_profile()
    network = load_network_assets()
    findings_data = load_json_file("mock_findings.json")

    findings = analyze_findings(findings_data["findings"])
    risk_table = create_risk_table(findings)
    risk_counts = count_risk_levels(findings)

    report = []
    report.append("# Network Security Assessment Report")
    report.append("")
    report.append("## Simulated Assessment Notice")
    report.append("")
    report.append(company["company"]["disclaimer"])
    report.append("")
    report.append("## Executive Summary")
    report.append("")
    report.append(
        "This simulated assessment reviewed the defensive security posture of "
        + company["company"]["name"]
        + ", a fictional organization with "
        + str(company["company"]["employees"])
        + " employees."
    )
    report.append("")
    report.append(
        "The assessment identified "
        + str(len(findings))
        + " simulated findings: "
        + str(risk_counts["Critical"])
        + " Critical, "
        + str(risk_counts["High"])
        + " High, "
        + str(risk_counts["Medium"])
        + " Medium, and "
        + str(risk_counts["Low"])
        + " Low."
    )
    report.append("")
    report.append(
        "The highest-priority defensive improvements are guest Wi-Fi isolation, "
        "multi-factor authentication for administrative access, restricted DMZ-to-server "
        "communication, centralized security logging, and stronger protection for the backup server."
    )
    report.append("")
    report.append("## Assessment Scope")
    report.append("")
    report.append("The simulated environment includes:")
    report.append("")
    report.append("- Internal LAN")
    report.append("- Internet-facing services")
    report.append("- Employee Wi-Fi")
    report.append("- Guest Wi-Fi")
    report.append("- Firewalls, switches, servers, and employee endpoints")
    report.append("- Security monitoring and logging systems")
    report.append("")
    report.append("## Network Overview")
    report.append("")
    report.append(
        "The mock network contains "
        + str(len(network["network_zones"]))
        + " network zones and "
        + str(len(network["assets"]))
        + " assets."
    )
    report.append("")
    report.append("The logical network diagram is available at `diagrams/network_diagram.svg`.")
    report.append("")
    report.append("## Risk Assessment Method")
    report.append("")
    report.append("Each simulated finding is assigned:")
    report.append("")
    report.append("- A likelihood score from 1 to 5")
    report.append("- An impact score from 1 to 5")
    report.append("- A risk score calculated as likelihood multiplied by impact")
    report.append("- A risk level based on the risk score")
    report.append("")
    report.append("Risk levels are defined as:")
    report.append("")
    report.append("- Critical: risk score of 20 or higher")
    report.append("- High: risk score of 12 to 19")
    report.append("- Medium: risk score of 6 to 11")
    report.append("- Low: risk score below 6")
    report.append("")
    report.append("## Findings and Risk Table")
    report.append("")
    report.append(risk_table)
    report.append("")
    report.append("## Recommended Defensive Controls")
    report.append("")
    report.append("1. Segment guest Wi-Fi from all internal networks.")
    report.append("2. Require multi-factor authentication for administrative access.")
    report.append("3. Restrict DMZ server access to only required internal services.")
    report.append("4. Send security logs from firewalls, servers, wireless systems, and endpoints to the SIEM.")
    report.append("5. Separate employee Wi-Fi from the internal wired LAN.")
    report.append("6. Restrict access to the backup server and protect backup data.")
    report.append("7. Review firewall rules regularly and use a default-deny approach.")
    report.append("8. Maintain an accurate asset inventory and monitor for unmanaged devices.")
    report.append("")
    report.append("## Remediation Priorities")
    report.append("")
    report.append("| Priority | Finding | Recommended action |")
    report.append("|---|---|---|")
    report.append("| 1 | FIND-001 | Isolate guest Wi-Fi from internal systems |")
    report.append("| 2 | FIND-002 | Require MFA for administrative access |")
    report.append("| 3 | FIND-003 | Restrict DMZ-to-server VLAN communication |")
    report.append("| 4 | FIND-004 | Centralize logging and monitoring |")
    report.append("| 5 | FIND-006 | Restrict backup server access |")
    report.append("| 6 | FIND-005 | Separate employee Wi-Fi from the internal LAN |")
    report.append("")
    report.append("## Conclusion")
    report.append("")
    report.append(
        "The simulated assessment identifies opportunities to strengthen network segmentation, "
        "access controls, wireless security, logging, and protection of critical business systems. "
        "Implementing the recommended defensive controls would reduce the likelihood and potential "
        "impact of common security incidents."
    )
    report.append("")

    return "\n".join(report)


def save_assessment_report(output_path):
    """Save the assessment report to a Markdown file."""
    report = create_assessment_report()

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")

    return output_path