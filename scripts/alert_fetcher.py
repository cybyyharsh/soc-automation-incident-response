USE_MOCK = True

def fetch_mock_alerts():
    """
    Mock Wazuh alerts for development/testing.
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

def fetch_alerts_from_wazuh():
    """
    Placeholder for real Wazuh API integration.
    """
    raise NotImplementedError("Live Wazuh API integration not enabled")

def fetch_alerts(limit=5):
    if USE_MOCK:
        return fetch_mock_alerts()
    else:
        return fetch_alerts_from_wazuh()

if __name__ == "__main__":
    alerts = fetch_alerts()
    print(f"Fetched {len(alerts['data'])} alerts")

