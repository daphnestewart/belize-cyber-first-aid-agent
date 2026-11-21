import json


def load_incidents():

    with open(
        "src/data/incidents.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


INCIDENT_TYPES = load_incidents()

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
    "health",
    "financial"
]


def determine_privacy_impact(description, default_level):

    description = description.lower()

    for keyword in PERSONAL_DATA_KEYWORDS:

        if keyword in description:

            if keyword in ["medical", "health"]:
                return "Critical"

            return "High"

    return default_level


def requires_escalation(severity, privacy_impact):

    return (
        severity in ["High", "Critical"]
        or privacy_impact in ["High", "Critical"]
    )


def assess_incident(description):

    description = description.lower()

    for incident, details in INCIDENT_TYPES.items():

        if incident in description:

            privacy_impact = determine_privacy_impact(
                description,
                details["privacy_impact"]
            )

            return {
                "incident_type": incident.title(),
                "severity": details["severity"],
                "privacy_impact": privacy_impact,
                "escalation_required": requires_escalation(
                    details["severity"],
                    privacy_impact
                ),
                "data_protection_review":
                    privacy_impact in ["High", "Critical"],
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

    print(
        f"\nIncident Type: {result['incident_type']}"
    )

    print(
        f"Business Severity: {result['severity']}"
    )

    print(
        f"Privacy Impact: {result['privacy_impact']}"
    )

    print(
        f"Escalation Required: "
        f"{'Yes' if result['escalation_required'] else 'No'}"
    )

    print(
        f"Belize Data Protection Review: "
        f"{'Required' if result['data_protection_review'] else 'Not Required'}"
    )

    print(
        f"Recommended Playbook: {result['playbook']}"
    )

    print("\nImmediate Actions:")

    for i, action in enumerate(result["actions"], start=1):

        print(f"{i}. {action}")

    print("\n" + "=" * 50)


def main():

    print("\nBelize Cyber First Aid Agent\n")

    incident = input(
        "Describe the incident: "
    )

    result = assess_incident(incident)

    display_result(result)


if __name__ == "__main__":
    main()
