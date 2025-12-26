# SOC Automation & Incident Response Platform

## Overview
This project implements an **end-to-end Security Operations Center (SOC) automation pipeline** that simulates real-world incident detection, enrichment, prioritization, and response workflows.  
It is designed to demonstrate **SOC analyst decision-making**, **automation logic**, and **incident response readiness** using a modular, production-aligned architecture.

The platform executes the full SOC workflow using a **single command**, making it suitable for demos, interviews, and portfolio evaluation.

---

## Problem Statement
Modern SOC teams face:
- High alert volumes from SIEM platforms
- Manual and time-consuming alert triage
- Delayed incident response
- Inconsistent incident documentation

Manual handling of these tasks leads to analyst fatigue and increased response time.

---

## Solution
This project provides a **lightweight SOC automation framework** that:
- Ingests security alerts
- Enriches alerts with threat intelligence
- Calculates severity using SOC decision logic
- Creates structured incident cases
- Generates audit-ready incident reports automatically

The design follows **enterprise SOC best practices** with clear separation of concerns and extensible modules.

---

## Architecture Overview

Alert Source (SIEM-aligned)
        ↓
Alert Ingestion Layer
        ↓
Threat Intelligence Enrichment
        ↓
Severity Scoring Engine
        ↓
Incident Creation (Case Management)
        ↓
Automated Incident Report (PDF)

---

## Technology Stack

- **Language:** Python 3  
- **SIEM Alignment:** Wazuh (API-ready design)  
- **Threat Intelligence:** IP reputation enrichment (mock, production-ready)  
- **Incident Management:** TheHive-aligned case workflow  
- **Reporting:** PDF generation using ReportLab  
- **Platform:** Linux (Kali / Ubuntu)  
- **Version Control:** Git & GitHub  

All components are implemented using **open-source and free tools**.

---

## Key Features

- Modular SOC automation pipeline
- Threat intelligence enrichment for alert context
- Rule-based severity scoring aligned with SOC triage practices
- Automated incident creation workflow
- Professional PDF incident reports
- One-command execution for full pipeline demo
- Clean Git history and enterprise-grade structure

---

## Project Structure

## SIEM Integration — Wazuh

This project is designed to align with **Wazuh SIEM**, a widely used open-source security monitoring platform.

### Integration Approach
- The alert ingestion layer is architected to consume alerts from **Wazuh Manager via its REST API**
- For development and demonstration purposes, **mock alerts** are used to simulate real SOC conditions
- The same ingestion module can be switched to **live Wazuh alerts** with minimal configuration changes

### Why Mock Alerts Are Used
In enterprise SOC environments:
- Direct access to production SIEM systems is restricted
- Automation development is typically performed against mock or staging data
- This approach enables rapid development without impacting SOC operations

### Production-Ready Design
In a production deployment:
- Wazuh Manager would forward alerts to the automation engine
- Alerts would be fetched from the Wazuh API (`/security/events`)
- The remaining pipeline (enrichment, severity scoring, incident creation, reporting) remains unchanged

This design follows **industry-standard SOC automation practices** and ensures compatibility with real Wazuh deployments.
## SOC Automation Flow

```text
Alert → Severity Engine → Case Created
                     ↘
               Response Playbook
                 ├─ Block IP (simulated)
                 ├─ Create Response Tasks
                 └─ Host Containment (simulated)
