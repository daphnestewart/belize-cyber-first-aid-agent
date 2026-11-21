def assess_incident(description):
    description = description.lower()

    if "ransomware" in description:
        return "Critical"

    if "data breach" in description:
        return "High"

    if "phishing" in description:
        return "Medium"

    return "Low"


incident = input("Describe the incident: ")
severity = assess_incident(incident)

print(f"Incident Severity: {severity}")
