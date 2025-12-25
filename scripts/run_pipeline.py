import sys
import os
sys.path.append(os.path.dirname(__file__))
from alert_fetcher import fetch_alerts
from threat_enrichment import enrich_ip
from severity_engine import calculate_severity
from thehive_connector import create_case
from report_generator import generate_incident_report

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

        enrichment = enrich_ip(src_ip)
        severity = calculate_severity(alert, enrichment)

        case = create_case(alert, enrichment, severity)

        report_path = generate_incident_report(case)

        print(f"[+] Incident handled | Severity: {severity}")
        print(f"[+] Report generated: {report_path}")

    print("\n[✓] SOC Automation Pipeline Completed")


if __name__ == "__main__":
    run_soc_pipeline()
