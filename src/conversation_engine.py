"""
Dorothy Conversation Engine

Loads investigation playbooks dynamically.

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


PLAYBOOKS = load_json(
    "investigation_playbooks.json"
)


YES_WORDS = [
    "yes",
    "yeah",
    "yep",
    "sure",
    "correct",
    "obviously",
    "definitely",
    "absolutely"
]

NO_WORDS = [
    "no",
    "nope",
    "negative"
]

UNKNOWN_WORDS = [
    "maybe",
    "unsure",
    "unknown",
    "not sure",
    "dont know",
    "don't know"
]


def normalize_answer(answer):

    text = answer.strip().lower()

    if text in YES_WORDS:
        return "yes"

    if text in NO_WORDS:
        return "no"

    if text in UNKNOWN_WORDS:
        return "unknown"

    return text


def get_questions(incident_type):

    playbook = PLAYBOOKS.get(
        incident_type,
        {}
    )

    questions = []

    for section in [
        "containment",
        "business",
        "privacy"
    ]:

        questions.extend(
            playbook.get(
                section,
                []
            )
        )

    return questions


def get_next_question(
    incident_type,
    answer_count,
    answers=None
):

    if answers is None:
        answers = {}

    questions = get_questions(
        incident_type
    )

    remaining = [
        q
        for q in questions
        if q not in answers
    ]

    if not remaining:
        return None

    return remaining[0]


def get_progress(
    incident_type,
    answers
):

    total = len(
        get_questions(
            incident_type
        )
    )

    if total == 0:
        return 100

    return int(
        len(answers)
        / total
        * 100
    )


def get_confidence_score(
    answers
):

    confidence = 50

    for answer in answers.values():

        text = answer.lower()

        if "all" in text:
            confidence += 10

        if "everyone" in text:
            confidence += 10

        if "encrypted" in text:
            confidence += 20

        if "asking for money" in text:
            confidence += 20

    return min(
        confidence,
        100
    )


def get_missing_information(
    incident_type,
    answers
):

    return [

        question

        for question in get_questions(
            incident_type
        )

        if question not in answers
    ]


def analyse_answers(
    answers
):

    score = 0

    findings = []

    privacy_impact = "Low"

    for question, answer in answers.items():

        a = normalize_answer(
            answer
        )

        q = question.lower()

        if a == "yes":

            score += 1

        if "customer" in q and a == "yes":

            privacy_impact = "High"

            findings.append(
                "Customer data involvement identified."
            )

            score += 3

        if "employee" in q and a == "yes":

            score += 2

            findings.append(
                "Employee information involvement identified."
            )

        if "encrypted" in q and a == "yes":

            score += 5

            findings.append(
                "Files appear encrypted."
            )

        if "administrator" in q and a == "yes":

            score += 4

            findings.append(
                "Administrator account involvement identified."
            )

    return {
        "score": score,
        "privacy_impact": privacy_impact,
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

    if score >= 12:
        index = min(index + 2, 3)

    elif score >= 5:
        index = min(index + 1, 3)

    return levels[index]


def generate_recommendations(
    incident_type,
    answers
):

    recommendations = []

    if incident_type == "Phishing":

        recommendations.extend([
            "Reset affected passwords immediately.",
            "Review mailbox rules.",
            "Review sign-in logs.",
            "Enable MFA where not already enabled."
        ])

    elif incident_type == "Unauthorized Access":

        recommendations.extend([
            "Disable compromised accounts.",
            "Revoke all active sessions.",
            "Review privileged account activity.",
            "Preserve audit logs."
        ])

    elif incident_type == "Data Breach":

        recommendations.extend([
            "Contain the exposure.",
            "Identify affected data subjects.",
            "Assess Data Protection obligations.",
            "Preserve evidence."
        ])

    elif incident_type == "Ransomware":

        recommendations.extend([
            "Disconnect affected systems immediately.",
            "Prevent further spread.",
            "Assess backup availability.",
            "Notify management immediately."
        ])

    elif incident_type == "Lost or Stolen Device":

        recommendations.extend([
            "Attempt remote wipe.",
            "Change passwords.",
            "Revoke active sessions.",
            "Assess data exposure."
        ])

    return recommendations
