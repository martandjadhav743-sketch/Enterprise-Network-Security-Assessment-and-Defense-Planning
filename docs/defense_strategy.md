# Defensive Security Strategy

## Purpose

This document defines recommended defensive controls for the fictional
Northwind Business Solutions network.

All systems, IP addresses, configurations, findings, and recommendations are
fictional mock data. No real network was scanned, tested, or modified.

## Defensive Principles

- Use a default-deny approach: allow only necessary communication.
- Apply least privilege to users, administrators, systems, and network zones.
- Segment networks by trust level, business function, and criticality.
- Keep internet-facing systems separated from internal business systems.
- Prevent guest devices from accessing internal resources.
- Require multi-factor authentication for administrative access.
- Centralize security logs and monitor for suspicious activity.
- Restrict outbound server traffic to approved destinations.
- Protect backups and limit access to backup systems.

## Network Segmentation

| Network zone | Recommended access |
|---|---|
| Internet | Untrusted; no direct access to internal systems |
| DMZ | Contains only internet-facing services; limited access to required internal services |
| Internal LAN | Employee access to approved business services |
| Server VLAN | Internal business servers; access limited to authorized users and systems |
| Employee Wi-Fi | Managed employee devices; limited access to required internal services |
| Guest Wi-Fi | Internet access only; no access to internal systems |
| Management VLAN | Highly restricted administrative access; MFA required |

## Recommended Firewall Policy

| Rule ID | Source zone | Destination zone | Service | Action | Purpose |
|---|---|---|---|---|---|
| FW-001 | Internet | DMZ | HTTPS to web server | Allow | Public website access |
| FW-002 | Internet | DMZ | Required email protocols | Allow | Business email |
| FW-003 | DMZ | Server VLAN | Specific CRM service | Allow | Website needs limited CRM data |
| FW-004 | DMZ | Server VLAN | All other traffic | Deny | Prevent broad DMZ access |
| FW-005 | Internal LAN | Server VLAN | Approved CRM and file services | Allow | Employee business access |
| FW-006 | Internal LAN | Server VLAN | All other traffic | Deny | Limit unnecessary access |
| FW-007 | Guest Wi-Fi | Internal LAN | All traffic | Deny | Isolate guest devices |
| FW-008 | Guest Wi-Fi | Server VLAN | All traffic | Deny | Protect business servers |
| FW-009 | Guest Wi-Fi | Internet | Web browsing | Allow | Guest Internet access |
| FW-010 | Employee Wi-Fi | Internal LAN | Approved business services | Allow | Employee wireless access |
| FW-011 | Employee Wi-Fi | Server VLAN | All other traffic | Deny | Limit lateral movement |
| FW-012 | Management VLAN | Server VLAN | Approved administrative services | Allow | Controlled administration |
| FW-013 | Management VLAN | Internet | All traffic | Deny | Restrict administrative egress |
| FW-014 | Server VLAN | Internet | Approved update destinations | Allow | Controlled software updates |
| FW-015 | Server VLAN | Internet | All other traffic | Deny | Restrict server egress |
| FW-016 | Internal LAN | Management VLAN | Security logs to SIEM | Allow | Centralized monitoring |
| FW-017 | Any zone | Any zone | Traffic not explicitly allowed | Deny | Default-deny policy |

## Identity and Access Controls

- Require phishing-resistant multi-factor authentication for all administrative access.
- Use separate administrative accounts that are not used for daily email or web browsing.
- Apply least privilege to all user and administrator accounts.
- Review access regularly and remove accounts or permissions that are no longer needed.
- Restrict administrative access to the management VLAN.
- Use approved remote-access methods with MFA for employees working remotely.

## Wireless Security Controls

- Keep employee Wi-Fi and guest Wi-Fi on separate VLANs.
- Prevent guest Wi-Fi devices from communicating with internal systems.
- Use strong Wi-Fi authentication and encryption for employee devices.
- Use a separate guest network with Internet-only access.
- Monitor wireless authentication failures and unexpected device connections.
- Maintain an inventory of authorized wireless access points.

## Monitoring and Logging Controls

- Send firewall, server, wireless, endpoint, and authentication logs to the SIEM.
- Create alerts for repeated failed logins, unusual administrative activity, and unexpected network connections.
- Monitor changes to firewall rules and network device configurations.
- Retain logs according to the organization’s retention policy.
- Review alerts regularly and document response actions.

## Data Protection Controls

- Restrict access to the backup server to authorized backup and administration systems.
- Keep backup data separated from general business systems.
- Test backup restoration procedures regularly.
- Protect backups with strong access controls and encryption where appropriate.
- Maintain an inventory of critical business data and systems.

## Remediation Roadmap

| Priority | Timeframe | Control |
|---|---|---|
| 1 | Immediate | Block guest Wi-Fi access to internal systems |
| 2 | Immediate | Require MFA for administrative access |
| 3 | Short term | Restrict DMZ-to-server VLAN firewall rules |
| 4 | Short term | Send security logs to the SIEM |
| 5 | Short term | Restrict access to the backup server |
| 6 | Medium term | Separate employee Wi-Fi from the internal LAN |
| 7 | Ongoing | Review firewall rules, access permissions, and logs |