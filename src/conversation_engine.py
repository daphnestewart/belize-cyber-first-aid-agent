"""
Dorothy Conversation Engine

Author: Daphne Stewart

Provides:

- Guided investigations
- Answer normalization
- Branching questions
- Risk analysis
- Severity adjustment
- Recommendations
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


# =====================================================
# ANSWER NORMALIZATION
# =====================================================

YES_WORDS = [
    "yes",
    "y",
    "yeah",
    "yep",
    "sure",
    "affirmative",
    "correct",
    "obviously",
    "definitely"
]


NO_WORDS = [
    "no",
    "n",
    "nope",
    "negative"
]


UNKNOWN_WORDS = [
    "unknown",
    "unsure",
    "dont know",
    "don't know",
    "not sure",
    "maybe"
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


# =====================================================
# INCIDENT TYPE MAPPING
# =====================================================

def normalise_incident_type(
    incident_type
):

    mapping = {

        "Phishing":
            "phishing",

        "Unauthorized Access":
            "unauthorized_access",

        "Data Breach":
            "data_breach",

        "Ransomware":
            "ransomware",

        "Lost or Stolen Device":
            "lost_device",

        "Lost Device":
            "lost_device"
    }

    return mapping.get(
        incident_type,
        "generic"
    )


# =====================================================
# CORE QUESTIONS
# =====================================================

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

    questions = []

    questions.extend(
        incident_questions["initial_questions"]
    )

    questions.extend(
        incident_questions["business_impact_questions"]
    )

    questions.extend(
        incident_questions["privacy_questions"]
    )

    return questions


# =====================================================
# BRANCHING QUESTIONS
# =====================================================

def get_branching_questions(
    incident_type,
    answers
):

    follow_ups = []

    if incident_type == "Phishing":

        for question, answer in answers.items():

            normalized = normalize_answer(
                answer
            )

            q = question.lower()

            if (
                "credentials entered"
                in q
                and normalized == "yes"
            ):

                add = [
                    "Has the password been reset?",
                    "Have active sessions been revoked?",
                    "Was Multi-Factor Authentication enabled?",
                    "Have sign-in logs been reviewed?"
                ]

                for item in add:

                    if item not in answers:
                        follow_ups.append(item)

            if (
                "customer information"
                in q
                and normalized == "yes"
            ):

                add = [
                    "How many customers may be affected?",
                    "Has management been notified of the potential exposure?"
                ]

                for item in add:

                    if item not in answers:
                        follow_ups.append(item)

            if (
                "employee information"
                in q
                and normalized == "yes"
            ):

                add = [
                    "Could employee records have been viewed or downloaded?"
                ]

                for item in add:

                    if item not in answers:
                        follow_ups.append(item)

    return follow_ups


# =====================================================
# NEXT QUESTION
# =====================================================

def get_next_question(
    incident_type,
    answer_count,
    answers=None
):

    if answers is None:
        answers = {}

    base_questions = get_questions(
        incident_type
    )

    branching_questions = (
        get_branching_questions(
            incident_type,
            answers
        )
    )

    all_questions = (
        base_questions +
        branching_questions
    )

    remaining = [

        q
        for q in all_questions
        if q not in answers
    ]

    if not remaining:
        return None

    return remaining[0]


# =====================================================
# PROGRESS
# =====================================================

def get_progress(
    incident_type,
    answers
):

    base_questions = get_questions(
        incident_type
    )

    branching_questions = (
        get_branching_questions(
            incident_type,
            answers
        )
    )

    total = len(
        base_questions +
        branching_questions
    )

    completed = len(
        answers
    )

    if total == 0:
        return 100

    progress = int(
        (completed / total) * 100
    )

    return min(progress, 100)


# =====================================================
# ANALYSIS
# =====================================================

def analyse_answers(
    answers
):

    score = 0

    findings = []

    privacy_impact = "Low"

    for question, answer in answers.items():

        answer = normalize_answer(
            answer
        )

        question = question.lower()

        if (
            "credentials entered"
            in question
            and answer == "yes"
        ):

            score += 4

            findings.append(
                "Credentials were entered into a potentially malicious website."
            )

        if (
            "customer information"
            in question
            and answer == "yes"
        ):

            score += 3

            privacy_impact = "High"

            findings.append(
                "Customer information may be affected."
            )

        if (
            "employee information"
            in question
            and answer == "yes"
        ):

            score += 2

            if privacy_impact == "Low":
                privacy_impact = "Medium"

            findings.append(
                "Employee information may be affected."
            )

        if (
            "personal data"
            in question
            and answer == "yes"
        ):

            privacy_impact = "High"

            findings.append(
                "Personal data may have been accessed."
            )

        if (
            "password been reset"
            in question
            and answer == "no"
        ):

            score += 3

            findings.append(
                "Compromised credentials may still be active."
            )

        if (
            "active sessions"
            in question
            and answer == "no"
        ):

            score += 2

            findings.append(
                "Potentially malicious sessions may still exist."
            )

        if (
            "multi-factor authentication"
            in question
            and answer == "no"
        ):

            score += 2

            findings.append(
                "MFA was not enabled."
            )

        if (
            "administrator"
            in question
            and answer == "yes"
        ):

            score += 4

            findings.append(
                "Administrator account involvement."
            )

    return {
        "score": score,
        "findings": findings,
        "privacy_impact": privacy_impact
    }


# =====================================================
# SEVERITY ADJUSTMENT
# =====================================================

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


# =====================================================
# RECOMMENDATIONS
# =====================================================

def generate_recommendations(
    answers
):

    recommendations = []

    for question, answer in answers.items():

        answer = normalize_answer(
            answer
        )

        question = question.lower()

        if (
            "credentials entered"
            in question
            and answer == "yes"
        ):

            recommendations.extend([
                "Reset affected passwords immediately.",
                "Review sign-in logs.",
                "Revoke active sessions."
            ])

        if (
            "multi-factor authentication"
            in question
            and answer == "no"
        ):

            recommendations.append(
                "Enable Multi-Factor Authentication."
            )

        if (
            "customer information"
            in question
            and answer == "yes"
        ):

            recommendations.append(
                "Perform a Belize Data Protection impact assessment."
            )

        if (
            "employee information"
            in question
            and answer == "yes"
        ):

            recommendations.append(
                "Review potential exposure of employee records."
            )

    return sorted(
        list(set(recommendations))
    )
