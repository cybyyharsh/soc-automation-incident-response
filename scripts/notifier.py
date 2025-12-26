import json
from datetime import datetime
from pathlib import Path

OUTBOX = Path("outbox")
OUTBOX.mkdir(exist_ok=True)

def send_email_alert(case):
    """
    DEV MODE:
    Write email alerts to a local outbox instead of SMTP.
    Switch to SMTP in production.
    """
    payload = {
        "to": "soc@company.com",
        "subject": f"[SOC ALERT] HIGH Severity Incident - {case['title']}",
        "body": {
            "severity": case["severity"],
            "title": case["title"],
            "source_ip": case["source_ip"],
            "host": case["host"],
            "created_at": case["created_at"],
        },
        "sent_at": datetime.utcnow().isoformat() + "Z",
    }

    fname = OUTBOX / f"alert_{int(datetime.utcnow().timestamp())}.json"
    fname.write_text(json.dumps(payload, indent=2))
    print(f"[+] DEV alert written to {fname}")

if __name__ == "__main__":
    demo_case = {
        "title": "SSH brute force attempt",
        "severity": "HIGH",
        "source_ip": "185.220.101.1",
        "host": "linux-server",
        "created_at": "2025-01-01T00:00:00Z"
    }
    send_email_alert(demo_case)
