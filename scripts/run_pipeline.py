import sys
import os

# Ensure local imports work
sys.path.append(os.path.dirname(__file__))

from alert_fetcher import fetch_alerts
from threat_enrichment import enrich_ip
from severity_engine import calculate_severity
from thehive_connector import create_case
from report_generator import generate_incident_report
from notifier import send_email_alert
from playbooks import run_playbook


def run_soc_pipeline():
    print("[+] Starting SOC Automation Pipeline")

    alerts_data = fetch_alerts()
    alerts = alerts_data.get("data", [])

    if not alerts:
        print("[!] No alerts found")
        return

    for alert in alerts:
        print("\n[+] Processing new alert")

        src_ip = alert.get("data", {}).get("srcip", "0.0.0.0")

        # Phase 2: Threat Enrichment
        enrichment = enrich_ip(src_ip)

        # Phase 3: Severity Scoring
        severity = calculate_severity(alert, enrichment)
        print(f"[+] Calculated severity: {severity}")

        # Phase 5: Incident Creation (TheHive)
        case = create_case(alert, enrichment, severity)
        print(f"[+] Case created: {case['case_id']}")

        # Phase B: Alerting
        if severity == "HIGH":
            send_email_alert(case)

        # Phase C: SOAR Playbooks
        run_playbook(case)

        # Phase 6: Incident Report
        generate_incident_report(case)

    print("\n[✓] SOC Automation Pipeline Completed")


if __name__ == "__main__":
    run_soc_pipeline()
