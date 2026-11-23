"""
Belize Cyber First Aid Agent
Incident Assessment Engine

Author: Daphne Stewart
Version: 2.0
"""

import json
from pathlib import Path


DATA_DIR = Path(__file__).parent / "data"


def load_json(filename):
    """Load a JSON file from the data directory."""

    with open(
        DATA_DIR / filename,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


INCIDENTS = load_json("incidents.json")
SEVERITY_MATRIX = load_json("severity_matrix.json")
PRIVACY_MATRIX = load_json("privacy_impact_matrix.json")
PERSONAL_DATA = load_json("personal_data_categories.json")


def identify_incident(description):
    """
    Identify incident type using keywords.
    """

    description = description.lower()

    for incident_key, incident in INCIDENTS.items():

        for keyword in incident["keywords"]:

            if keyword.lower() in description:

                return incident_key

    return None


def determine_privacy_impact(description, default_level):
    """
    Increase privacy impact based on detected data categories.
    """

    description = description.lower()

    # Sensitive personal data
    sensitive_examples = PERSONAL_DATA[
        "sensitive_personal_data"
    ]["examples"]

    for example in sensitive_examples:

        if example.lower() in description:
            return "Critical"

    # Standard personal data
    for category in PERSONAL_DATA.values():

        for example in category["examples"]:

            if example.lower() in description:
                return "High"

    return default_level


def create_assessment(description):
    """
    Generate incident assessment.
    """

    incident_key = identify_incident(description)

    if not incident_key:

        return {
            "incident_type": "Unknown",
            "severity": "Low",
            "privacy_impact": "Low",
            "priority": "Normal",
            "escalation_required": False,
            "data_protection_review": False,
            "playbook": "Manual Review Required",
            "actions": [
                "Collect additional information.",
                "Identify affected systems.",
                "Determine affected users."
            ]
        }

    incident = INCIDENTS[incident_key]

    privacy_impact = determine_privacy_impact(
        description,
        incident["default_privacy_impact"]
    )

    severity = incident["default_severity"]

    severity_info = SEVERITY_MATRIX[severity]
    privacy_info = PRIVACY_MATRIX[privacy_impact]

    escalation_required = (
        incident["escalate"]
        or severity_info["escalate"]
    )

    return {
        "incident_type": incident["name"],
        "severity": severity,
        "priority": severity_info["priority"],
        "privacy_impact": privacy_impact,
        "escalation_required": escalation_required,
        "data_protection_review":
            privacy_info["review_required"],
        "playbook": incident["playbook"],
        "actions": incident["immediate_actions"]
    }


def display_assessment(result):
    """
    Display assessment results.
    """

    print("\n" + "=" * 60)
    print("BELIZE CYBER FIRST AID AGENT")
    print("=" * 60)

    print(f"\nIncident Type: {result['incident_type']}")
    print(f"Business Severity: {result['severity']}")
    print(f"Priority: {result['priority']}")
    print(f"Privacy Impact: {result['privacy_impact']}")

    print(
        f"Escalation Required: "
        f"{'Yes' if result['escalation_required'] else 'No'}"
    )

    print(
        f"Belize Data Protection Review: "
        f"{'Required' if result['data_protection_review'] else 'Not Required'}"
    )

    print(
        f"Recommended Playbook: "
        f"{result['playbook']}"
    )

    print("\nImmediate Actions:")

    for number, action in enumerate(
        result["actions"],
        start=1
    ):

        print(f"{number}. {action}")

    print("\n" + "=" * 60)


def main():

    print("\nBelize Cyber First Aid Agent")
    print("Incident Assessment Prototype\n")

    incident_description = input(
        "Describe the incident:\n\n> "
    )

    result = create_assessment(
        incident_description
    )

    display_assessment(result)


if __name__ == "__main__":
    main()
