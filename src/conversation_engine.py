"""
Dorothy Conversation Engine

Manages:

- Guided investigation
- Question progression
- Answer tracking
- Risk scoring
- Severity adjustment
- Investigation summaries

Author: Daphne Stewart
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def load_json(filename):

    with open(
        DATA_DIR / filename,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


QUESTIONS = load_json(
    "incident_questions.json"
)


def normalise_incident_type(
    incident_type
):
    """
    Converts human friendly names
    to JSON keys.
    """

    mapping = {
        "Phishing": "phishing",
        "Unauthorized Access": "unauthorized_access",
        "Data Breach": "data_breach",
        "Ransomware": "ransomware",
        "Lost or Stolen Device": "lost_device",
        "Lost Device": "lost_device"
    }

    return mapping.get(
        incident_type,
        "generic"
    )


def get_questions(
    incident_type
):

    key = normalise_incident_type(
        incident_type
    )

    incident_questions = QUESTIONS.get(
        key,
        QUESTIONS["generic"]
    )

    ordered_questions = []

    ordered_questions.extend(
        incident_questions["initial_questions"]
    )

    ordered_questions.extend(
        incident_questions["business_impact_questions"]
    )

    ordered_questions.extend(
        incident_questions["privacy_questions"]
    )

    return ordered_questions


def get_next_question(
    incident_type,
    answer_count
):
    """
    Returns next unanswered question.
    """

    questions = get_questions(
        incident_type
    )

    if answer_count >= len(questions):
        return None

    return questions[
        answer_count
    ]


def get_progress(
    incident_type,
    answer_count
):
    """
    Percentage complete.
    """

    questions = get_questions(
        incident_type
    )

    total = len(questions)

    if total == 0:
        return 100

    progress = int(
        (
            answer_count /
            total
        ) * 100
    )

    return min(progress, 100)


def analyse_answers(
    answers
):

    score = 0

    findings = []

    for question, answer in answers.items():

        q = question.lower()
        a = answer.lower()

        if (
            "credentials entered" in q
            and "yes" in a
        ):
            score += 3

            findings.append(
                "Credentials were entered."
            )

        if (
            "customer information" in q
            and "yes" in a
        ):
            score += 3

            findings.append(
                "Customer information may be affected."
            )

        if (
            "employee information" in q
            and "yes" in a
        ):
            score += 2

            findings.append(
                "Employee information may be affected."
            )

        if (
            "administrator" in q
            and "yes" in a
        ):
            score += 3

            findings.append(
                "Administrator account involvement."
            )

        if (
            "business operation" in q
            and "yes" in a
        ):
            score += 2

            findings.append(
                "Business operations may be disrupted."
            )

        if (
            "files encrypted" in q
            and "yes" in a
        ):
            score += 3

            findings.append(
                "Files appear encrypted."
            )

        if (
            "sensitive personal data" in q
            and "yes" in a
        ):
            score += 4

            findings.append(
                "Sensitive personal data involved."
            )

        if (
            "financial transactions" in q
            and "yes" in a
        ):
            score += 3

            findings.append(
                "Financial activity detected."
            )

    return {
        "score": score,
        "findings": findings
    }


def adjust_severity(
    base_severity,
    score
):

    levels = [
        "Low",
        "Medium",
        "High",
        "Critical"
    ]

    if base_severity not in levels:
        return base_severity

    index = levels.index(
        base_severity
    )

    if score >= 10:
        index = min(index + 2, 3)

    elif score >= 5:
        index = min(index + 1, 3)

    return levels[index]


def generate_recommendations(
    answers
):

    recommendations = []

    for question, answer in answers.items():

        q = question.lower()
        a = answer.lower()

        if (
            "credentials entered" in q
            and "yes" in a
        ):
            recommendations.append(
                "Reset passwords immediately."
            )

            recommendations.append(
                "Revoke active sessions."
            )

        if (
            "customer information" in q
            and "yes" in a
        ):
            recommendations.append(
                "Conduct a Belize Data Protection review."
            )

        if (
            "files encrypted" in q
            and "yes" in a
        ):
            recommendations.append(
                "Disconnect affected systems from the network."
            )

        if (
            "administrator" in q
            and "yes" in a
        ):
            recommendations.append(
                "Review privileged account activity."
            )

    return sorted(
        list(set(recommendations))
    )
