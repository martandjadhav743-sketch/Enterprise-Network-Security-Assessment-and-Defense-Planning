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
python -c "import json; data=json.load(open(r'data\mock_company_profile.json', encoding='utf-8')); print('JSON is valid'); print(data['company']['name']); print(len(data['business_systems']), 'business systems')"
```

5. Validate the mock network asset inventory:

```powershell
python -c "import json; d=json.load(open(r'data\mock_network_assets.json', encoding='utf-8')); print('JSON is valid'); print(len(d['network_zones']), 'network zones'); print(len(d['assets']), 'assets'); print(sum(1 for a in d['assets'] if a['criticality']=='Critical'), 'critical assets')"
```

6. Open the logical network diagram:

```powershell
Start-Process .\diagrams\network_diagram.svg
```

## Project Status

See `PROGRESS.md` for the current phase and completed work.