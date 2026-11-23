# Simulated Incident Response and Monitoring Plan

## Purpose

This document describes a defensive incident-response and monitoring plan for
the fictional Northwind Business Solutions network.

All systems, events, alerts, and response actions are fictional mock data.
No real network, device, or system was accessed, scanned, modified, or monitored.

## Incident Response Team

| Role | Responsibility |
|---|---|
| Incident response lead | Coordinates the response and communicates with leadership |
| Network administrator | Reviews firewall, switch, and wireless configurations |
| System administrator | Reviews server and endpoint security settings |
| Security analyst | Reviews alerts, logs, and possible indicators of compromise |
| Management representative | Approves major response decisions and business continuity actions |

## Incident Response Lifecycle

### 1. Preparation

- Maintain an accurate asset inventory.
- Document normal network activity and system behavior.
- Ensure security logs are sent to the SIEM.
- Define roles, contact information, and escalation procedures.
- Test backup restoration procedures regularly.
- Review and practice the incident-response plan.

### 2. Detection and Analysis

- Review SIEM alerts and security logs.
- Identify unusual authentication activity, unexpected network connections, and configuration changes.
- Determine whether an alert represents a real incident, a false positive, or a policy violation.
- Document the affected systems, users, time range, and initial observations.
- Preserve relevant logs and evidence before making changes.

### 3. Containment

- Isolate affected systems or network segments only when necessary.
- Prevent an incident from spreading to other systems.
- Disable compromised accounts or revoke unnecessary access.
- Apply short-term firewall restrictions to limit further activity.
- Preserve evidence and avoid deleting or modifying original logs.

### 4. Eradication and Recovery

- Remove the root cause of the incident.
- Restore affected systems from known-good backups when appropriate.
- Reset compromised credentials and review privileged access.
- Apply security updates and configuration changes needed to prevent recurrence.
- Validate that systems are functioning normally before returning them to service.

### 5. Post-Incident Activities

- Create an incident timeline and after-action report.
- Identify the initial cause and any control gaps.
- Document lessons learned.
- Update detection rules, firewall policies, and response procedures.
- Share relevant findings with management and technical teams.

## Simulated Monitoring Scenarios

| Scenario ID | Simulated alert | Possible concern | Defensive response |
|---|---|---|---|
| MON-001 | Multiple failed administrative logins | Possible password guessing or credential misuse | Review source, account, and time; enforce MFA; escalate if suspicious |
| MON-002 | Guest Wi-Fi device attempts internal access | Guest network isolation failure | Review firewall logs; block guest-to-internal traffic; investigate configuration |
| MON-003 | Unexpected outbound connection from a server | Possible unauthorized server communication | Review destination and process; restrict egress; investigate if needed |
| MON-004 | Firewall rule changed outside approved change process | Possible unauthorized configuration change | Review change record; restore approved configuration if needed |
| MON-005 | Backup server accessed by unusual account | Possible unauthorized access to backups | Review access logs; restrict access; investigate account activity |

## Logging Requirements

The following sources should send logs to the SIEM:

- Firewall
- Router
- Core switch
- Wireless access points
- Web and email servers
- CRM and file servers
- Backup server
- Endpoint security tools
- Identity and authentication systems

## Alert Review Process

1. Review new alerts during each business day.
2. Classify each alert as informational, suspicious, or confirmed incident.
3. Investigate suspicious alerts using relevant logs and asset information.
4. Escalate confirmed incidents to the incident-response lead.
5. Document the investigation, actions taken, and final outcome.

## Important Safety Rule

This plan is for defensive learning only. It does not provide instructions for
attacking, exploiting, or compromising systems. Response actions must preserve
evidence and avoid deleting or modifying original logs.