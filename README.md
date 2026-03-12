# SNMP MIB Collection

This repository contains SNMP MIB files for all network devices, servers, and applications monitored by Zenoss at Mitel.

**Last Reorganised:** March 12, 2026  
**Total Vendors:** 63  
**Category Groups:** 9 + 1 (uncategorised)

---

## Directory Structure

```
mibs/
├── 01_Network_Infrastructure/   ← Routers, switches, firewalls, load balancers
├── 02_Servers_Hardware/         ← Physical servers, BMCs, storage, UPS
├── 03_Mitel_Unify_UC/           ← All Mitel and Unify (former Siemens ENT) products
├── 04_Security_Endpoint/        ← Endpoint security and AV products
├── 05_Monitoring_Management/    ← SNMP agents, monitoring frameworks, management tools
├── 06_Virtualization/           ← Hypervisors and virtual infrastructure
├── 07_Video_Collaboration/      ← Video conferencing, recording, contact centre
├── 08_Telephony_VoIP/           ← SIP gateways, VoIP gateways, codecs, SBCs
├── 09_Standards_RFC/            ← IETF RFC MIBs, SNMP standards, vendor-neutral
└── _NOT_CATEGORIZED/            ← Pending review and classification
```

---

## Category Details

### 01 — Network Infrastructure (14 vendors)

Routers, switches, firewalls, load balancers, and network management platforms.

| Vendor Folder | Product Family |
|---|---|
| Cisco | IOS, NX-OS, ASA, Catalyst |
| Extreme | ExtremeXOS, Summit |
| Brocade | SAN switches, FCX, VDX |
| H3C | Comware switches/routers |
| Enterasys | Network edge switches |
| Cabletron | Legacy switches |
| F5 | BIG-IP load balancers |
| Fortinet | FortiGate firewalls |
| CheckPoint | NGFW, management |
| Clavister | NetWall firewalls |
| Vyatta | Open-source router/firewall |
| Xedia | Legacy access concentrators |
| a3com | 3Com legacy switches |
| Infoblox | DNS/DHCP/IPAM appliances |

---

### 02 — Servers & Hardware (10 vendors)

Physical servers, BMC/IPMI controllers, storage, UPS, and server management software.

| Vendor Folder | Product Family |
|---|---|
| DELL | PowerEdge servers, DRAC/iDRAC |
| HP | ProLiant, iLO management |
| SUPERMICRO | Server platforms |
| LENOVO | ThinkSystem servers |
| IBM-IMM | Integrated Management Module |
| Fujitsu iRMC | iRMC server management |
| Fujitsu ServerView MIBs | ServerView management suite |
| APC PowerNet | UPS, PDU, power management |
| Base Board Management Systems | Generic BMC/IPMI profiles |
| QuantaStor | Storage appliances |
| NetApp | ONTAP storage |

---

### 03 — Mitel & Unify UC (15 vendors)

All Mitel (post-AASTRA), Unify (former Siemens Enterprise Networks), and related UC platforms.

| Vendor Folder | Product Family |
|---|---|
| Mitel | MiVoice Business (3300 ICP), MiVoice Office 400, MiVoice 5000, SX-2000 |
| Unify Phone (NGTC) | OpenScape Voice, OpenScape UC |
| Unify Professional Services (PS) | Unify PS custom MIBs |
| HiPath | Siemens HiPath 4000, HiPath 3000 series |
| HiPath 3000 HG1500 | HiPath 3000 media gateways |
| OSBiz | OpenScape Business (formerly HiPath 3000) |
| OSV | OpenScape Voice |
| OSCC | OpenScape Contact Center |
| OSB and SBC | OpenScape Branch and SBC |
| Ribon SBC | Ribbon (formerly GENBAND) SBC |
| Mediatrix | AudioCodes/Mediatrix VoIP gateways |
| DLS | Device Loading Service (DLS) |
| UC | UC server / application server |
| Xpression | OpenText Xpression fax/messaging |
| HiMed | Siemens HiMed hospital comms |

> **Note:** Mitel MiVoice Business MIBs for Zenoss ZenPack development are in `Mitel/Mitel Voice Business (MiVB)/`. See `docs/MITEL_MIVB_MIB_ZENOSS_ANALYSIS.md` for full MIB analysis and `zenoss/dev/zenpacks/ZenPack.mitel.MiVoiceBusiness/` for the ZenPack.

---

### 04 — Security & Endpoint (2 vendors)

| Vendor Folder | Product Family |
|---|---|
| Kaspersky | Kaspersky Security Center |
| McAfee | ePolicy Orchestrator |

---

### 05 — Monitoring & Management (6 vendors)

SNMP management agents, monitoring frameworks, notification tools, and cluster managers.

| Vendor Folder | Product Family |
|---|---|
| SNMP Informant | Windows SNMP extension agent |
| NOC-CUSTOM-MIB | Custom NOC monitoring MIBs |
| EVNTAGENT | Event agent MIBs |
| PET events | Platform Event Trap (PET) — IPMI |
| Clusterlabs Pacemaker | Linux HA cluster manager |
| NOTIFICATION-TEST-MIB | SNMP notification testing |

---

### 06 — Virtualization (1 vendor)

| Vendor Folder | Product Family |
|---|---|
| VMware | ESXi, vCenter, vSphere |

---

### 07 — Video & Collaboration (4 vendors)

Video conferencing endpoints, recording systems, and contact centre infrastructure.

| Vendor Folder | Product Family |
|---|---|
| Tandberg | Cisco Tandberg video endpoints |
| Verint | Recording and analytics |
| Virtual Care Collaboration Service (VCCS) | Mitel VCCS / virtual care |
| Circuit | Circuit collaboration platform |

---

### 08 — Telephony & VoIP (8 vendors)

SIP/VoIP gateways, codecs, media gateways, and SBCs from non-Mitel/Unify vendors.

| Vendor Folder | Product Family |
|---|---|
| Audio Codes | MediaPack, Mediant gateways |
| Intervoice | IVR / voice automation |
| Cordless-IP | DECT/IP DECT systems |
| MBG-SNMP-MIB | Mitel Border Gateway / SBC MIBs |
| Avaya | IP Office, Aura (legacy scope) |
| ASC | ASC recording / analytics |
| ASYNCOS | Cisco Email Security (IronPort) |

---

### 09 — Standards & RFC (3 entries)

| Vendor Folder | Content |
|---|---|
| RFC MIBs | Standard IETF RFC MIB modules (MIB-II, IF-MIB, HOST-RESOURCES-MIB, etc.) |
| Siemens PN | Siemens PROFINET industrial MIBs |
| NOTIFICATION-TEST-MIB | SNMP notification testing MIB |

---

### _NOT_CATEGORIZED

Vendor folders held here pending review. They have not been linked to a known product or validated for use in Zenoss.

---

## Using MIBs with Zenoss

1. Load MIBs via **Advanced → MIBs → Add MIB Package** in the Zenoss UI
2. Load MIBs in dependency order — load base/root MIBs before their dependents
3. Verify OID resolution in the MIB browser after loading
4. For Mitel MiVB: follow the load order in `docs/MITEL_MIVB_MIB_ZENOSS_ANALYSIS.md` Section 5.2

---

*Repository:* `mitel-networks/mibs`  
*Related:* `mitel-networks/zenoss/dev/zenpacks/`, `mitel-networks/docs/`
