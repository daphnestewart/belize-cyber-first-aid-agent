"""
Belize Cyber First Aid Agent
Incident Assessment Engine

Author: Daphne Stewart
Version: 3.0
"""

import json
from pathlib import Path


# =====================================================
# Data Loading
# =====================================================

DATA_DIR = Path(__file__).parent / "data"


def load_json(filename):
    """Load JSON configuration files."""

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
QUESTIONS = load_json("incident_questions.json")
ESCALATION_RULES = load_json("escalation_rules.json")
REPORT_TEMPLATE = load_json("report_template.json")
PLAYBOOKS = load_json("playbook_mapping.json")


# =====================================================
# Incident Identification
# =====================================================

def identify_incident(description):
    """
    Identify incident type based on keywords.
    """

    description = description.lower()

    for incident_key, incident in INCIDENTS.items():

        for keyword in incident["keywords"]:

            if keyword.lower() in description:
                return incident_key

    return None


# =====================================================
# Privacy Impact Assessment
# =====================================================

def determine_privacy_impact(
    description,
    default_level
):
    """
    Determine privacy impact based on personal data indicators.
    """

    description = description.lower()

    # Sensitive Personal Data = Critical

    sensitive_entries = PERSONAL_DATA[
        "sensitive_personal_data"
    ]["examples"]

    for item in sensitive_entries:

        if item.lower() in description:
            return "Critical"

    # Other personal data = High

    for category_key, category in PERSONAL_DATA.items():

        if category_key == "sensitive_personal_data":
            continue

        for item in category["examples"]:

            if item.lower() in description:
                return "High"

    return default_level


# =====================================================
# Escalation Logic
# =====================================================

def check_escalation(
    incident_key,
    severity,
    privacy_impact
):
    """
    Determine whether escalation is required.
    """

    auto_rules = ESCALATION_RULES[
        "automatic_escalation"
    ]

    if severity in auto_rules["severity_levels"]:
        return True

    if privacy_impact in auto_rules["privacy_impact_levels"]:
        return True

    if incident_key in auto_rules["incident_types"]:
        return True

    return False


# =====================================================
# Assessment Engine
# =====================================================

def create_assessment(description):

    incident_key = identify_incident(description)

    if not incident_key:

        return {
            "incident_type": "Unknown",
            "business_severity": "Low",
            "priority": "Normal",
            "response_target": "Manual Review",
            "privacy_impact": "Low",
            "privacy_description": "Unknown",
            "escalation_required": False,
            "data_protection_review": False,
            "playbook": "Manual Review Required",
            "nist_functions": [
                "Govern",
                "Identify"
            ],
            "questions": QUESTIONS["generic"],
            "actions": [
                "Collect additional information.",
                "Determine affected systems.",
                "Identify affected users.",
                "Perform manual classification."
            ]
        }

    incident = INCIDENTS[incident_key]

    privacy_impact = determine_privacy_impact(
        description,
        incident["default_privacy_impact"]
    )

    severity = incident["default_severity"]

    severity_details = SEVERITY_MATRIX[severity]

    privacy_details = PRIVACY_MATRIX[privacy_impact]

    escalation_required = check_escalation(
        incident_key,
        severity,
        privacy_impact
    )

    playbook_info = PLAYBOOKS.get(
        incident_key,
        {}
    )

    return {
        "incident_type": incident["name"],

        "business_severity": severity,

        "priority":
            severity_details["priority"],

        "response_target":
            severity_details.get(
                "response_target",
                "Immediate"
            ),

        "privacy_impact":
            privacy_impact,

        "privacy_description":
            privacy_details["description"],

        "escalation_required":
            escalation_required,

        "data_protection_review":
            privacy_details["review_required"],

        "playbook":
            playbook_info.get(
                "file_path",
                "No playbook assigned"
            ),

        "nist_functions":
            playbook_info.get(
                "nist_functions",
                ["Govern", "Identify"]
            ),

        "questions":
            QUESTIONS.get(
                incident_key,
                QUESTIONS["generic"]
            ),

        "actions":
            incident["immediate_actions"]
    }


# =====================================================
# Display Results
# =====================================================

def display_assessment(result):

    print("\n" + "=" * 70)
    print("BELIZE CYBER FIRST AID AGENT")
    print("=" * 70)

    print(
        f"\nIncident Type: "
        f"{result['incident_type']}"
    )

    print(
        f"Business Severity: "
        f"{result['business_severity']}"
    )

    print(
        f"Priority: "
        f"{result['priority']}"
    )

    print(
        f"Response Target: "
        f"{result['response_target']}"
    )

    print(
        f"Privacy Impact: "
        f"{result['privacy_impact']}"
    )

    print(
        f"Privacy Description: "
        f"{result['privacy_description']}"
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
        f"Recommended Playbook: "
        f"{result['playbook']}"
    )

    print("\nNIST CSF 2.0 Functions:")

    for function in result["nist_functions"]:
        print(f"- {function}")

    print("\nImmediate Actions:")

    for index, action in enumerate(
        result["actions"],
        start=1
    ):
        print(f"{index}. {action}")

    print("\nRecommended Triage Questions:")

    for section, question_list in result[
        "questions"
    ].items():

        print(
            f"\n{section.replace('_', ' ').title()}"
        )

        for question in question_list:
            print(f"- {question}")

    print("\n" + "=" * 70)


# =====================================================
# Main
# =====================================================

def main():

    print("\nBelize Cyber First Aid Agent")
    print("Incident Assessment Prototype")
    print("-" * 40)

    description = input(
        "\nDescribe the incident:\n\n> "
    )

    assessment = create_assessment(
        description
    )

    display_assessment(
        assessment
    )


if __name__ == "__main__":
    main()
