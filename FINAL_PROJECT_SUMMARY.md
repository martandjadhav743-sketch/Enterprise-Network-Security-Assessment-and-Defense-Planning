# Final Project Summary

## Project

**Enterprise Network Security Assessment and Defense Planning**

This project completed a simulated, defensive-only network security assessment for the fictional company Northwind Business Solutions. All company details, systems, IP addresses, hostnames, configurations, findings, and events are fictional mock data.

The project was designed for defensive security learning and documentation. It does not assess, scan, exploit, or interact with real networks.

## Original project phases

### Phase 1 — Structure and documentation

The project structure, README, progress documentation, `.gitignore`, Python virtual environment, dependencies, and test configuration were created and corrected.

### Phase 2 — Fictional company and network scope

The fictional company profile, network scope, asset inventory, and network data-flow documentation were created.

The network scope defines:

- Northwind Business Solutions
- Seven network zones
- Eleven simulated assets
- Ten primary data flows
- Assessment objectives and exclusions
- Supporting documentation references

### Phase 3 — Logical network diagram

The logical network diagram was created at `diagrams/network_diagram.svg`. It documents the Internet, DMZ, internal LAN, server VLAN, employee Wi-Fi, guest Wi-Fi, and management VLAN.

### Phase 4 — Mock findings and threat catalog

Six simulated findings were created in `data/mock_findings.json`. The threat and risk catalog at `docs/threat_risk_catalog.md` maps six threats to findings, likelihood and impact inputs, calculated risk scores, and defensive recommendations.

### Phase 5 — Python risk-analysis tool

The Python risk-analysis workflow includes:

- `src/data_loader.py`
- `src/risk_engine.py`
- `src/report_generator.py`
- `src/assessment_report.py`

The risk engine calculates risk as likelihood multiplied by impact and assigns risk levels using the following thresholds:

- Critical: 20 or higher
- High: 12 to 19
- Medium: 6 to 11
- Low: below 6

### Phase 6 — Defensive controls and firewall policy

The defensive strategy and incident-response plan document controls for network segmentation, administrative access, wireless isolation, centralized logging, backup protection, firewall policy, and incident response.

### Phase 7 — Assessment report

The assessment report generator creates `reports/network_security_assessment_report.md`. The report includes an executive summary, assessment scope, network overview, risk method, findings and risk table, recommended defensive controls, remediation priorities, and conclusion.

### Phase 8 — Automated tests

The project includes automated tests for the data loader, risk engine, report generator, and assessment report.

Final test result:

```text
48 passed
```

Final source coverage:

```text
98%
```

### Phase 9 — End-to-end verification and documentation

The final workflow was verified by regenerating the risk table and assessment report, running all automated tests, and reviewing the generated output.

Final verification results:

```text
Risk table generated
Assessment report generated
48 passed
98% source coverage
```

## Final deliverables

| Deliverable | Location |
|---|---|
| Company profile | `data/mock_company_profile.json` |
| Network scope | `data/mock_network_scope.json` |
| Network asset inventory | `data/mock_network_assets.json` |
| Network data flows | `docs/network_data_flows.md` |
| Logical network diagram | `diagrams/network_diagram.svg` |
| Simulated findings | `data/mock_findings.json` |
| Threat and risk catalog | `docs/threat_risk_catalog.md` |
| Risk table | `reports/risk_table.md` |
| Defensive strategy | `docs/defense_strategy.md` |
| Incident-response plan | `docs/incident_response_plan.md` |
| Assessment report | `reports/network_security_assessment_report.md` |
| Automated tests | `tests/` |
| Final verification screenshots | `screenshots/` |

## Optional extra

A presentation may be added as an optional supporting artifact. It is not a required phase in the original project plan.