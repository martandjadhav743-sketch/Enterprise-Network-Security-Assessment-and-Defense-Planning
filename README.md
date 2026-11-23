# Enterprise Network Security Assessment and Defense Planning

This project simulates a defensive network security assessment for a fictional
small-to-medium enterprise with 50–100 employees.

The project uses only mock data and simulated findings. It does not scan,
attack, modify, or access any real network, device, or system.

## Objective

Assess the security posture of a fictional enterprise network and produce a
professional, defensive security assessment report.

## Scope

The simulated environment includes:

- Internal LAN
- Internet-facing services
- Employee Wi-Fi
- Guest Wi-Fi
- Firewalls, switches, servers, and employee endpoints
- Monitoring and logging systems

## Deliverables

- Logical network diagram
- Mock findings and threat catalog
- Risk analysis table
- Defensive control recommendations
- Network security assessment report
- Automated tests

## Safety Notice

This project is for defensive security learning only.

- No real networks are scanned.
- No real systems are modified.
- No malware, exploits, or offensive tools are created.
- All findings, IP addresses, hostnames, and events are fictional mock data.
- Simulation mode is the default.

## How to Run

1. Open PowerShell.
2. Move to the project folder:

```powershell
cd "C:\Users\marta\Desktop\Projects\Enterprise Network Security Assessment and Defense Planning"
```

3. Activate the Python virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Validate the mock company profile:

```powershell
python -c "from src.data_loader import load_company_profile, load_network_assets; company=load_company_profile(); assets=load_network_assets(); print('Company:', company['company']['name']); print('Business systems:', len(company['business_systems'])); print('Network zones:', len(assets['network_zones'])); print('Assets:', len(assets['assets']))"
```

5. Analyze the simulated findings and display the risk table:

```powershell
python -c "from src.data_loader import load_json_file; from src.risk_engine import analyze_findings; from src.report_generator import create_risk_table; findings=analyze_findings(load_json_file('mock_findings.json')['findings']); print(create_risk_table(findings))"
```

6. Generate and save the full assessment report:

```powershell
python -c "from src.assessment_report import save_assessment_report; path=save_assessment_report('reports/network_security_assessment_report.md'); print('Saved:', path)"
```

7. Open the generated report:

```powershell
Start-Process .\reports\network_security_assessment_report.md
```

## Defensive Controls

The project includes a defensive security strategy and incident-response plan.

Key controls include:

- Network segmentation
- Default-deny firewall policy
- Guest Wi-Fi isolation
- Multi-factor authentication for administrative access
- Restricted DMZ-to-server communication
- Centralized security logging and monitoring
- Backup access restrictions
- Incident-response preparation, detection, containment, recovery, and review

## Project Status

See `PROGRESS.md` for the current phase and completed work.