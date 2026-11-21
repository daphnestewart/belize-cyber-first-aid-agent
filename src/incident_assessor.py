"""
Belize Cyber First Aid Agent
Incident Assessment Engine

Version: 1.0
Author: Daphne Stewart
"""

INCIDENT_TYPES = {
    "phishing": {
        "severity": "Medium",
        "privacy_impact": "Low",
        "playbook": "phishing.md",
        "actions": [
            "Preserve the email.",
            "Reset credentials if entered.",
            "Enable MFA.",
            "Review login activity."
        ]
    },

    "unauthorized access": {
        "severity": "High",
        "privacy_impact": "Medium",
        "playbook": "unauthorized-access.md",
        "actions": [
            "Disable compromised accounts.",
            "Reset passwords.",
            "Preserve logs.",
            "Review recent activity."
        ]
    },

    "data breach": {
        "severity": "High",
        "privacy_impact": "High",
        "playbook": "data-breach.md",
        "actions": [
            "Contain the breach.",
            "Identify exposed information.",
            "Preserve evidence.",
            "Begin privacy impact assessment."
        ]
    },

    "ransomware": {
        "severity": "Critical",
        "privacy_impact": "High",
        "playbook": "ransomware.md",
        "actions": [
            "Disconnect affected systems.",
            "Preserve evidence.",
            "Notify management.",
            "Assess backup availability."
        ]
    },

    "lost device": {
        "severity": "Medium",
        "privacy_impact": "Medium",
        "playbook": "lost-device.md",
        "actions": [
            "Report device loss.",
            "Revoke active sessions.",
            "Change passwords.",
            "Determine data exposure."
        ]
    }
}


PERSONAL_DATA_KEYWORDS = [
    "customer",
    "customers",
    "employee",
    "employees",
    "payroll",
    "hr",
    "database",
    "personal data",
    "personal information",
    "records",
    "medical",
    "health data",
    "financial information"
]


CRITICAL_KEYWORDS = [
    "administrator",
    "admin account",
    "ransomware",
    "multiple systems",
    "customer database",
    "sensitive data"
]


def determine_privacy_impact(description, default_level):

    description = description.lower()

    for keyword in PERSONAL_DATA_KEYWORDS:
        if keyword in description:

            if keyword in ["medical", "health data"]:
                return "Critical"

            return "High"

    return default_level


def requires_escalation(severity, privacy_impact):

    if severity in ["Critical", "High"]:
        return True

    if privacy_impact in ["High", "Critical"]:
        return True

    return False


def assess_incident(description):

    description = description.lower()

    for incident, details in INCIDENT_TYPES.items():

        if incident in description:

            privacy_impact = determine_privacy_impact(
                description,
                details["privacy_impact"]
            )

            escalation = requires_escalation(
                details["severity"],
                privacy_impact
            )

            return {
                "incident_type": incident.title(),
                "severity": details["severity"],
                "privacy_impact": privacy_impact,
                "escalation_required": escalation,
                "data_protection_review": privacy_impact in ["High", "Critical"],
                "playbook": details["playbook"],
                "actions": details["actions"]
            }

    return {
        "incident_type": "Unknown",
        "severity": "Low",
        "privacy_impact": "Low",
        "escalation_required": False,
        "data_protection_review": False,
        "playbook": "Manual Review Required",
        "actions": [
            "Collect additional information.",
            "Perform manual classification."
        ]
    }


def display_result(result):

    print("\n" + "=" * 50)
    print("BELIZE CYBER FIRST AID AGENT")
    print("=" * 50)

    print(f"\nIncident Type: {result['incident_type']}")
    print(f"Business Severity: {result['severity']}")
    print(f"Privacy Impact: {result['privacy_impact']}")
    print(
        f"Escalation Required: "
        f"{'Yes' if result['escalation_required'] else 'No'}"
    )

    print(
        f"Belize Data Protection Review: "
        f"{'Required' if result['data_protection_review'] else 'Not Required'}"
    )

    print(f"Recommended Playbook: {result['playbook']}")

    print("\nImmediate Actions:")

    for i, action in enumerate(result["actions"], start=1):
        print(f"{i}. {action}")

    print("\n" + "=" * 50)


def main():

    print("Belize Cyber First Aid Agent")
    print("Incident Assessment Prototype\n")

    incident = input("Describe the incident: ")

    result = assess_incident(incident)

    display_result(result)


if __name__ == "__main__":
    main()
