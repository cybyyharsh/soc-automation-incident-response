import json
from datetime import datetime
from pathlib import Path

ACTIONS_DIR = Path("actions")
ACTIONS_DIR.mkdir(exist_ok=True)

def block_ip(ip):
    """
    DEV-SAFE:
    Simulate IP blocking by writing an action record.
    """
    action = {
        "action": "block_ip",
        "ip": ip,
        "method": "simulated-firewall",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    _write_action(action)

def create_response_tasks(case):
    """
    Create analyst tasks for the incident.
    """
    tasks = [
        {"task": "Validate alert authenticity"},
        {"task": "Check related logs and events"},
        {"task": "Assess blast radius"},
        {"task": "Confirm containment effectiveness"}
    ]

    action = {
        "action": "create_tasks",
        "case_id": case["case_id"],
        "tasks": tasks,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    _write_action(action)

def simulate_containment(case):
    """
    Simulate host isolation / containment.
    """
    action = {
        "action": "contain_host",
        "host": case["host"],
        "status": "isolated (simulated)",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    _write_action(action)

def run_playbook(case):
    """
    SOAR Playbook Runner
    Executes actions based on severity.
    """
    if case["severity"] != "HIGH":
        return

    block_ip(case["source_ip"])
    create_response_tasks(case)
    simulate_containment(case)

def _write_action(action):
    fname = ACTIONS_DIR / f"{action['action']}_{int(datetime.utcnow().timestamp())}.json"
    fname.write_text(json.dumps(action, indent=2))
    print(f"[+] Playbook action executed: {action['action']}")
