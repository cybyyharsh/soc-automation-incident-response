import os
import requests
from dotenv import load_dotenv

load_dotenv()

VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
USE_REAL_TI = True  # toggle real vs mock

def enrich_ip_mock(ip):
    malicious_ips = {
        "185.220.101.1": 85,
        "45.83.64.22": 65
    }
    score = malicious_ips.get(ip, 10)
    return score

def enrich_ip_virustotal(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        return enrich_ip_mock(ip)

    data = response.json()
    stats = data["data"]["attributes"]["last_analysis_stats"]
    malicious = stats.get("malicious", 0)
    suspicious = stats.get("suspicious", 0)

    return malicious * 10 + suspicious * 5

def enrich_ip(ip):
    score = enrich_ip_virustotal(ip) if USE_REAL_TI else enrich_ip_mock(ip)

    return {
        "ip": ip,
        "reputation_score": score,
        "verdict": "malicious" if score >= 70 else "suspicious"
    }

if __name__ == "__main__":
    print(enrich_ip("8.8.8.8"))

