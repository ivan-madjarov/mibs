# Changelog — SNMP MIB Collection

All notable changes to the MIB repository structure are documented in this file.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

---

## [Unreleased]

---

## [2.0.0] — 2026-03-12

### Changed
- **Full repository restructure**: Reorganised 63 vendor MIB folders from a flat top-level directory into 9 structured category groups
- All folders preserved with their original names; no MIB file content was modified

### Added
- `01_Network_Infrastructure/` — Cisco, Extreme, Brocade, H3C, Enterasys, Cabletron, F5, Fortinet, CheckPoint, Clavister, Vyatta, Xedia, a3com, Infoblox (14 vendors)
- `02_Servers_Hardware/` — DELL, HP, SUPERMICRO, LENOVO, IBM-IMM, Fujitsu iRMC, Fujitsu ServerView MIBs, APC PowerNet, Base Board Management Systems, QuantaStor, NetApp (11 vendors)
- `03_Mitel_Unify_UC/` — Mitel, Unify Phone (NGTC), Unify Professional Services (PS), HiPath, HiPath 3000 HG1500, OSBiz, OSV, OSCC, OSB and SBC, Ribon SBC, Mediatrix, DLS, UC, Xpression, HiMed (15 vendors)
- `04_Security_Endpoint/` — Kaspersky, McAfee (2 vendors)
- `05_Monitoring_Management/` — SNMP Informant, NOC-CUSTOM-MIB, EVNTAGENT, PET events, Clusterlabs Pacemaker, NOTIFICATION-TEST-MIB (6 vendors)
- `06_Virtualization/` — VMware (1 vendor)
- `07_Video_Collaboration/` — Tandberg, Verint, Virtual Care Collaboration Service (VCCS), Circuit (4 vendors)
- `08_Telephony_VoIP/` — Audio Codes, Intervoice, Cordless-IP, MBG-SNMP-MIB, Avaya, ASC, ASYNCOS (7 vendors)
- `09_Standards_RFC/` — RFC MIBs, Siemens PN, NOTIFICATION-TEST-MIB (3 entries)
- `README.md` — Full category index, vendor table, Zenoss usage instructions
- `CHANGELOG.md` — This file

---

## [1.0.0] — 2026-03-04 (Initial commit — flat structure)

### Added
- Initial commit: SNMP MIB collection with 63 vendor folders at top-level (flat structure)
- Vendors included: a3com, APC PowerNet, ASC, ASYNCOS, Audio Codes, Avaya, Base Board Management Systems, Brocade, Cabletron, CheckPoint, Circuit, Cisco, Clavister, Clusterlabs Pacemaker, Cordless-IP, DELL, DLS, Enterasys, EVNTAGENT, Extreme, F5, Fortinet, Fujitsu iRMC, Fujitsu ServerView MIBs, H3C, HiMed, HiPath, HiPath 3000 HG1500, HP, IBM-IMM, Infoblox, Intervoice, Kaspersky, LENOVO, MBG-SNMP-MIB, McAfee, Mediatrix, Mitel, NetApp, NOC-CUSTOM-MIB, _NOT_CATEGORIZED, NOTIFICATION-TEST-MIB, OSB and SBC, OSBiz, OSCC, OSV, PET events, QuantaStor, RFC MIBs, Ribon SBC, Siemens PN, SNMP Informant, SUPERMICRO, Tandberg, UC, Unify Phone (NGTC), Unify Professional Services (PS), Verint, Virtual Care Collaboration Service (VCCS), VMware, Vyatta, Xedia, Xpression
