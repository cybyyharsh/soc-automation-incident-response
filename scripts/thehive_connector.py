import uuid
from datetime import datetime

def create_case(alert, enrichment, severity):
    """
    Mock TheHive case creation.
    Replace with real TheHive API in production.
    """

    case_id = str(uuid.uuid4())[:8]

    case = {
        "case_id": case_id,
        "title": alert.get("rule", {}).get("description", "Security Incident"),
        "severity": severity,
        "source_ip": enrichment.get("ip"),
        "host": alert.get("agent", {}).get("name", "unknown"),
        "created_at": datetime.utcnow().isoformat() + "Z",
        "status": "Open"
    }

    print("Incident created in TheHive:")
    print(case)

    return case


if __name__ == "__main__":
    sample_alert = {
        "rule": {"description": "SSH brute force attempt"},
        "agent": {"name": "linux-server"},
        "level": 10
    }

    sample_enrichment = {
        "ip": "185.220.101.1",
        "reputation_score": 85
    }

    severity = "HIGH"

    create_case(sample_alert, sample_enrichment, severity)
