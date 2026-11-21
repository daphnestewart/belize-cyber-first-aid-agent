INCIDENT_TYPES = {
    "phishing": "Medium",
    "malware": "Medium",
    "data breach": "High",
    "unauthorized access": "High",
    "ransomware": "Critical",
    "lost device": "Medium",
}


def assess_incident(description):
    description = description.lower()

    for incident, severity in INCIDENT_TYPES.items():
        if incident in description:
            return incident.title(), severity

    return "Unknown", "Low"


incident = input("Describe the incident: ")

incident_type, severity = assess_incident(incident)

print(f"Incident Type: {incident_type}")
print(f"Severity: {severity}")
