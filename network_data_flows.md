# Simulated Network Data Flows

## Purpose

This document describes the main data flows in the fictional network used for
this defensive security assessment project.

All IP addresses, hostnames, systems, users, and events are fictional mock data.
This document does not describe or assess a real network.

## Network Zones

| Zone | Trust level | Main purpose |
|---|---|---|
| Internet | Untrusted | External users and public services |
| DMZ | Restricted | Internet-facing web and email services |
| Internal LAN | Internal | Employee workstations and internal business systems |
| Server VLAN | Restricted | Internal business servers |
| Employee Wi-Fi | Internal | Managed employee wireless devices |
| Guest Wi-Fi | Untrusted | Visitor and personal devices |
| Management VLAN | Highly restricted | Administrative access and security monitoring |

## Primary Data Flows

| Flow ID | Source zone | Destination zone | Data or service | Expected direction | Security control |
|---|---|---|---|---|---|
| DF-01 | Internet | DMZ | HTTPS requests to the corporate website | Inbound | Firewall allows only required web traffic |
| DF-02 | Internet | DMZ | Email traffic to the email server | Inbound | Firewall allows only required email protocols |
| DF-03 | DMZ | Server VLAN | Website or email server requests internal business data | Outbound from DMZ | Firewall restricts destinations, ports, and protocols |
| DF-04 | Internal LAN | Server VLAN | Employees access CRM and file services | Internal | Access is limited to authorized users and services |
| DF-05 | Employee Wi-Fi | Internal LAN | Managed employee devices access internal resources | Internal | Wireless isolation and access controls |
| DF-06 | Guest Wi-Fi | Internet | Guest devices access the Internet | Outbound | Guest network is separated from internal systems |
| DF-07 | Guest Wi-Fi | Internal LAN | Guest devices access internal systems | Blocked by default | No direct access should be permitted |
| DF-08 | Management VLAN | Server VLAN | Administrators manage servers | Internal | Restricted administrative access and MFA |
| DF-09 | Internal LAN | Management VLAN | Security logs are sent to the SIEM | Outbound | Logging is centralized and access is restricted |
| DF-10 | Server VLAN | Internet | Servers access external update services | Outbound | Only approved update destinations are allowed |

## Defensive Design Principles

- Use segmentation to limit unnecessary communication between zones.
- Apply a default-deny approach: allow only necessary traffic.
- Keep internet-facing systems in the DMZ, separated from internal servers.
- Prevent guest Wi-Fi devices from reaching internal systems.
- Restrict administrative access to the management VLAN.
- Send security logs to the centralized SIEM for monitoring and alerting.
- Limit outbound server traffic to approved update and business destinations.

## Assessment Note

The data flows above represent the intended secure design for the fictional
company. In later phases, simulated findings will identify gaps between this
intended design and the mock current-state configuration.