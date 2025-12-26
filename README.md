SOC Automation & Incident Response Platform
Overview

This project is an end-to-end SOC Automation and Incident Response platform that simulates how modern enterprise Security Operations Centers (SOC) ingest alerts, enrich them with threat intelligence, assess severity, create incidents, trigger automated response playbooks (SOAR-style), generate alerts, and produce incident reports — all through a single command execution.

The system is designed with modularity, safety, and realism, making it suitable for development, demonstrations, and interview evaluation without relying on paid or production services.

Key Objectives

Automate SOC alert handling from ingestion to response

Demonstrate SOAR-style response playbooks

Maintain dev-safe execution (no destructive actions)

Follow enterprise engineering practices

Be fully explainable in SOC / Cybersecurity interviews

Alert → Threat Enrichment → Severity Engine → Case Created
                                   ↘
                            Response Playbooks
                              ├─ Block IP (simulated)
                              ├─ Create Response Tasks
                              └─ Host Containment (simulated)
Features
Alert Ingestion

Simulated SIEM alerts (Wazuh-style structure)

Easily extendable to live SIEM APIs

Threat Intelligence Enrichment

IP reputation enrichment (mocked for development)

Pluggable design for VirusTotal or other TI feeds

Severity Scoring Engine

Dynamic severity calculation based on:

Alert level

Threat intelligence score

Outputs: LOW, MEDIUM, HIGH

Incident Creation

Centralized incident object creation

Designed to be compatible with TheHive-style case management

Clean separation between pipeline and connector logic

SOAR-Style Response Playbooks (Phase C)

Executed automatically for HIGH severity incidents:

IP Blocking (Simulated)
Records firewall-style block actions safely

Response Task Creation
Generates analyst investigation tasks

Host Containment (Simulated)
Marks affected host as isolated

All response actions are logged as structured JSON artifacts.

Alerting (Development-Safe)

High-severity incidents generate alerts

Alerts are written to a local outbox (no SMTP / no secrets)

Ensures deterministic testing and CI compatibility

Incident Report Generation

Automatically generates incident reports

Designed for SOC documentation and audit workflows

One-Command Orchestration

Entire pipeline runs with a single command

No manual intervention required

soc-automation-incident-response/
│
├─ scripts/
│   ├─ alert_fetcher.py          # SIEM alert ingestion
│   ├─ threat_enrichment.py      # Threat intelligence enrichment
│   ├─ severity_engine.py        # Severity scoring logic
│   ├─ thehive_connector.py      # Incident creation (TheHive-style)
│   ├─ notifier.py               # Dev-safe alerting (outbox)
│   ├─ playbooks.py              # SOAR response playbooks
│   ├─ report_generator.py       # Incident report generation
│   └─ run_pipeline.py           # End-to-end orchestrator
│
├─ actions/                      # SOAR playbook execution logs
├─ outbox/                       # Alert notifications (dev-safe)
├─ reports/                      # Generated incident reports
├─ README.md
└─ .gitignore
