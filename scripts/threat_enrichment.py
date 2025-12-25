def enrich_ip(ip_address):
    """
    Mock threat intelligence enrichment.
    Replace with AbuseIPDB / VirusTotal in production.
    """
    malicious_ips = {
        "185.220.101.1": 85,
        "45.83.64.22": 65
    }

    score = malicious_ips.get(ip_address, 10)

    return {
        "ip": ip_address,
        "reputation_score": score,
        "verdict": "malicious" if score > 70 else "suspicious"
    }

if __name__ == "__main__":
    test_ip = "185.220.101.1"
    result = enrich_ip(test_ip)
    print(result)

