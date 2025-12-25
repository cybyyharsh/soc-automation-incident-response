def calculate_severity(alert, enrichment):
    """
    Calculate SOC severity based on alert data and threat intelligence.
    """

    alert_level = alert.get("level", 1)
    description = alert.get("rule", {}).get("description", "").lower()
    reputation = enrichment.get("reputation_score", 0)

    # HIGH severity conditions
    if reputation >= 80:
        return "HIGH"

    if "brute force" in description and alert_level >= 8:
        return "HIGH"

    # MEDIUM severity conditions
    if 50 <= reputation < 80:
        return "MEDIUM"

    if alert_level >= 6:
        return "MEDIUM"

    # LOW severity
    return "LOW"


if __name__ == "__main__":
    sample_alert = {
        "rule": {"description": "SSH brute force attempt"},
        "level": 10
    }

    sample_enrichment = {
        "reputation_score": 85
    }

    severity = calculate_severity(sample_alert, sample_enrichment)
    print(f"Calculated Severity: {severity}")

