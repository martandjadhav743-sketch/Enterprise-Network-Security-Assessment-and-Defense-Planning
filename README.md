# Enterprise Network Security Assessment and Defense Planning

This project performs a simulated, defensive-only network security assessment for the fictional company **Northwind Business Solutions**. It uses mock data to identify defensive improvements, calculate risk, document controls, and produce an assessment report.

All company details, systems, IP addresses, hostnames, configurations, findings, and events are fictional. This project must not be used to assess, scan, exploit, or interact with real networks.

## Project purpose

The project demonstrates an end-to-end defensive security assessment workflow:

1. Define a fictional company and network scope.
2. Create a logical network diagram.
3. Document simulated findings and threats.
4. Calculate risk using a Python-based risk engine.
5. Recommend defensive controls and incident-response actions.
6. Generate a complete assessment report.
7. Verify the project with automated tests.

## Project structure

```text
.
├── data/
│   ├── mock_company_profile.json
│   ├── mock_findings.json
│   ├── mock_network_assets.json
│   └── mock_network_scope.json
├── diagrams/
│   └── network_diagram.svg
├── docs/
│   ├── defense_strategy.md
│   ├── incident_response_plan.md
│   ├── network_data_flows.md
│   └── threat_risk_catalog.md
├── reports/
│   ├── network_security_assessment_report.md
│   └── risk_table.md
├── src/
│   ├── assessment_report.py
│   ├── data_loader.py
│   ├── report_generator.py
│   ├── risk_engine.py
│   └── __init__.py
├── tests/
├── presentations/
├── README.md
├── PROGRESS.md
├── pytest.ini
└── requirements.txt
```

## Key deliverables

| Deliverable | Location |
|---|---|
| Company profile | `data/mock_company_profile.json` |
| Network scope | `data/mock_network_scope.json` |
| Network asset inventory | `data/mock_network_assets.json` |
| Network data flows | `docs/network_data_flows.md` |
| Logical network diagram | `diagrams/network_diagram.svg` |
| Simulated findings | `data/mock_findings.json` |
| Threat and risk catalog | `docs/threat_risk_catalog.md` |
| Risk-analysis engine | `src/risk_engine.py` |
| Risk table | `reports/risk_table.md` |
| Defensive strategy | `docs/defense_strategy.md` |
| Incident-response plan | `docs/incident_response_plan.md` |
| Assessment report generator | `src/assessment_report.py` |
| Assessment report | `reports/network_security_assessment_report.md` |
| Automated tests | `tests/` |

## Requirements

- Python 3.14 or later
- PowerShell on Windows
- Git
- A Python virtual environment

## Setup

From the project root, create and activate the virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
pip install -r requirements.txt
```

## Generate the risk table

Generate the risk table using the assessment report workflow:

```powershell
python -c "from src.assessment_report import create_assessment_report; report = create_assessment_report(); from pathlib import Path; Path(r'reports\risk_table.md').write_text(report, encoding='utf-8'); print('Risk table generated')"
```

Expected output:

```text
Risk table generated
```

The generated risk table is saved at:

```text
reports/risk_table.md
```

## Generate the assessment report

Generate the full assessment report:

```powershell
python -c "from src.assessment_report import create_assessment_report; report = create_assessment_report(); from pathlib import Path; Path(r'reports\network_security_assessment_report.md').write_text(report, encoding='utf-8'); print('Assessment report generated')"
```

Expected output:

```text
Assessment report generated
```

The generated report is saved at:

```text
reports/network_security_assessment_report.md
```

## Run automated tests

Run all automated tests with coverage:

```powershell
pytest --cov=src --cov-report=term-missing
```

Expected result:

```text
48 passed
```

## Security disclaimer

This project is for defensive security learning and documentation only. It contains fictional mock data and does not provide instructions, tools, or procedures for attacking, scanning, exploiting, or compromising real systems.