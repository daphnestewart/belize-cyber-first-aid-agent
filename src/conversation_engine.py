"""
Dorothy Conversation Engine

Smarter investigation engine with:

- Answer normalization
- Risk-based branching
- Business-friendly investigations
- Confidence scoring
- Missing information tracking
- Dynamic risk assessment

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

# =====================================================
# ANSWER NORMALIZATION
# =====================================================

YES_WORDS = [
    "yes",
    "y",
    "yeah",
    "yep",
    "sure",
    "correct",
    "obviously",
    "definitely",
    "of course",
    "certainly",
    "absolutely"
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
    "not sure",
    "dont know",
    "don't know",
    "maybe"
]

HIGH_IMPACT_WORDS = [
    "all",
    "everyone",
    "entire company",
    "whole office",
    "every computer",
    "all computers",
    "everything"
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
            "lost_device",

        "Unknown":
            "generic"
    }

    return mapping.get(
        incident_type,
        "generic"
    )


# =====================================================
# BUSINESS-FRIENDLY QUESTIONS
# =====================================================

QUESTION_REPLACEMENTS = {

    "Was Multi-Factor Authentication enabled?":
        "Did users normally sign in using a second verification step such as a mobile app, code, or text message?",

    "Is sensitive personal data involved?":
        "Did the affected systems contain payroll, medical, HR, banking, government ID, or other confidential personal information?",

    "Could personal data have been accessed?":
        "Could someone have viewed names, email addresses, phone numbers, payroll records, customer records, or other information about people?"
}


# =====================================================
# BASE QUESTIONS
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

    improved_questions = []

    for question in questions:

        improved_questions.append(
            QUESTION_REPLACEMENTS.get(
                question,
                question
            )
        )

    return improved_questions


# =====================================================
# RISK-BASED FOLLOW-UPS
# =====================================================

def get_branching_questions(
    incident_type,
    answers
):

    follow_ups = []

    for question, answer in answers.items():

        normalized = normalize_answer(
            answer
        )

        q = question.lower()

        # PHISHING

        if (
            "credentials entered"
            in q
            and normalized == "yes"
        ):

            add = [

                "Has the password been reset since the incident?",

                "Have all active sessions been revoked?",

                "Have sign-in logs been reviewed?",

                "Did the user have access to customer information?",

                "Did the user have access to employee records?"
            ]

            for item in add:

                if item not in answers:
                    follow_ups.append(item)

        # RANSOMWARE

        if (
            "asking for money" in answer.lower()
            or "ransom" in answer.lower()
        ):

            add = [

                "Are files inaccessible or encrypted?",

                "Have affected systems been disconnected from the network?",

                "Are backups available?",

                "Are multiple computers affected?",

                "Can employees continue normal work operations?"
            ]

            for item in add:

                if item not in answers:
                    follow_ups.append(item)

        # BUSINESS-WIDE IMPACT

        if any(
            indicator in answer.lower()
            for indicator in HIGH_IMPACT_WORDS
        ):

            add = [

                "Are critical business operations currently disrupted?",

                "Has management been notified?",

                "Do you know how many users are affected?"
            ]

            for item in add:

                if item not in answers:
                    follow_ups.append(item)

    return list(dict.fromkeys(follow_ups))


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

    follow_ups = get_branching_questions(
        incident_type,
        answers
    )

    all_questions = (
        follow_ups +
        base_questions
    )

    remaining = [

        question
        for question in all_questions
        if question not in answers
    ]

    if not remaining:
        return None

    return remaining[0]


# =====================================================
# INVESTIGATION PROGRESS
# =====================================================

def get_progress(
    incident_type,
    answers
):

    total = len(
        get_questions(
            incident_type
        )
    )

    total += len(
        get_branching_questions(
            incident_type,
            answers
        )
    )

    if total == 0:
        return 100

    progress = int(
        (len(answers) / total)
        * 100
    )

    return min(progress, 100)


# =====================================================
# CONFIDENCE
# =====================================================

def get_confidence_score(
    answers
):

    confidence = 50

    for question, answer in answers.items():

        text = answer.lower()

        if "asking for money" in text:
            confidence += 20

        if "all" in text:
            confidence += 10

        if "everyone" in text:
            confidence += 10

        if "encrypted" in text:
            confidence += 20

    return min(confidence, 100)


# =====================================================
# MISSING INFO
# =====================================================

def get_missing_information(
    incident_type,
    answers
):

    questions = get_questions(
        incident_type
    )

    return [

        question
        for question in questions
        if question not in answers
    ]


# =====================================================
# ANALYSIS
# =====================================================

def analyse_answers(
    answers
):

    score = 0

    privacy_impact = "Low"

    findings = []

    for question, answer in answers.items():

        q = question.lower()
        a = normalize_answer(answer)

        raw = answer.lower()

        if "credentials entered" in q and a == "yes":

            score += 4

            findings.append(
                "Credentials were entered into a potentially malicious website."
            )

        if any(
            word in raw
            for word in HIGH_IMPACT_WORDS
        ):

            score += 4

            findings.append(
                "Incident appears to affect a large number of systems or users."
            )

        if (
            "business operation"
            in q
            and a == "yes"
        ):

            score += 3

            findings.append(
                "Business operations are disrupted."
            )

        if (
            "customer information"
            in q
            and a == "yes"
        ):

            privacy_impact = "High"

            score += 3

            findings.append(
                "Customer information may be involved."
            )

        if (
            "employee information"
            in q
            and a == "yes"
        ):

            score += 2

            if privacy_impact == "Low":
                privacy_impact = "Medium"

            findings.append(
                "Employee information may be involved."
            )

        if (
            "personal data"
            in q
            and a == "yes"
        ):

            privacy_impact = "High"

            score += 3

            findings.append(
                "Personal data may have been exposed."
            )

        if (
            "encrypted"
            in q
            and a == "yes"
        ):

            score += 5

            findings.append(
                "Files appear encrypted."
            )

        if (
            "backups available"
            in q
            and a == "no"
        ):

            score += 3

            findings.append(
                "No backups appear available."
            )

        if (
            "password been reset"
            in q
            and a == "no"
        ):

            score += 3

            findings.append(
                "Compromised credentials may still be active."
            )

    return {
        "score": score,
        "findings": findings,
        "privacy_impact": privacy_impact
    }


# =====================================================
# SEVERITY
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

    if score >= 12:
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

        q = question.lower()
        a = normalize_answer(answer)

        if (
            "password been reset"
            in q
            and a == "no"
        ):

            recommendations.append(
                "Reset affected passwords immediately."
            )

        if (
            "active sessions"
            in q
            and a == "no"
        ):

            recommendations.append(
                "Revoke all active sessions immediately."
            )

        if (
            "customer information"
            in q
            and a == "yes"
        ):

            recommendations.append(
                "Perform a Belize Data Protection impact assessment."
            )

        if (
            "encrypted"
            in q
            and a == "yes"
        ):

            recommendations.append(
                "Disconnect affected systems from the network immediately."
            )

        if (
            "backups available"
            in q
            and a == "no"
        ):

            recommendations.append(
                "Escalate immediately because recovery options may be limited."
            )

    return sorted(
        list(set(recommendations))
    )
