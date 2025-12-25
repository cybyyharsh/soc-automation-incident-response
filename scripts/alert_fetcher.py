def fetch_alerts(limit=5):
    """
    Mock Wazuh alerts for development/testing.
    Replace with real Wazuh API in production.
    """
    return {
        "data": [
            {
                "rule": {"description": "SSH brute force attempt"},
                "agent": {"name": "linux-server"},
                "data": {"srcip": "185.220.101.1"},
                "level": 10
            },
            {
                "rule": {"description": "Multiple failed login attempts"},
                "agent": {"name": "web-server"},
                "data": {"srcip": "45.83.64.22"},
                "level": 7
            }
        ]
    }

if __name__ == "__main__":
    alerts = fetch_alerts()
    print(f"Fetched {len(alerts['data'])} alerts")

