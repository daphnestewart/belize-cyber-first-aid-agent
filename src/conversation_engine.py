"""
Dorothy
Conversation Engine

Handles:

- Guided investigations
- Interview progression
- Missing information detection
- Investigation progress tracking
- Severity scoring inputs

Author: Daphne Stewart
"""

import json
from pathlib import Path


# =====================================================
# DATA LOADING
# =====================================================

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
# QUESTION MANAGEMENT
# =====================================================

def flatten_questions(incident_type):
    """
    Convert question groups into a single ordered list.
    """

    incident_type = incident_type.lower()

    incident_questions = QUESTIONS.get(
        incident_type,
        QUESTIONS["generic"]
    )

    all_questions = []

    for section_questions in incident_questions.values():

        all_questions.extend(
            section_questions
        )

    return all_questions


def get_next_question(
    incident_type,
    current_index
):
    """
    Returns the next question and whether
    assessment is finished.
    """

    questions = flatten_questions(
        incident_type
    )

    if current_index >= len(questions):
        return None

    return questions[current_index]


# =====================================================
# PROGRESS TRACKING
# =====================================================

def get_progress(
    incident_type,
    answered_questions
):
    """
    Returns percentage complete.
    """

    questions = flatten_questions(
        incident_type
    )

    total_questions = len(questions)

    if total_questions == 0:
        return 100

    progress = int(
        (
            answered_questions /
            total_questions
        ) * 100
    )

    return min(progress, 100)


# =====================================================
# ANSWER ANALYSIS
# =====================================================

def analyse_answers(
    answers
):
    """
    Basic scoring engine.

    Will evolve as Dorothy improves.
    """

    score = 0

    findings = []

    for answer in answers.values():

        response = answer.lower()

        if response.startswith("yes"):

            score += 1

    # More risky indicators

    high_risk_terms = [

        "credentials entered",
        "customer information",
        "employee information",
        "sensitive personal data",
        "administrator",
        "business disruption",
        "files encrypted",
        "ransom note",
        "financial transactions"
    ]

    for question, answer in answers.items():

        answer_lower = answer.lower()
        question_lower = question.lower()

        if answer_lower.startswith("yes"):

            for indicator in high_risk_terms:

                if indicator in question_lower:

                    score += 2

                    findings.append(
                        indicator
                    )

    return {
        "score": score,
        "findings": findings
    }


# =====================================================
# SEVERITY ADJUSTMENT
# =====================================================

def adjust_severity(
    base_severity,
    score
):
    """
    Increase severity based on findings
    collected during investigation.
    """

    levels = [
        "Low",
        "Medium",
        "High",
        "Critical"
    ]

    if base_severity not in levels:

        return base_severity

    current_index = levels.index(
        base_severity
    )

    if score >= 10:

        current_index = min(
            current_index + 2,
            3
        )

    elif score >= 5:

        current_index = min(
            current_index + 1,
            3
        )

    return levels[current_index]


# =====================================================
# SUMMARY GENERATION
# =====================================================

def generate_summary(
    incident_type,
    answers,
    assessment
):
    """
    Generates a human-readable assessment summary.
    """

    summary = []

    summary.append(
        f"Incident Type: {incident_type}"
    )

    summary.append(
        f"Business Severity: {assessment['business_severity']}"
    )

    summary.append(
        f"Privacy Impact: {assessment['privacy_impact']}"
    )

    summary.append("")
    summary.append(
        "Key Findings:"
    )

    for question, answer in answers.items():

        summary.append(
            f"- {question}: {answer}"
        )

    return "\n".join(summary)


# =====================================================
# RECOMMENDATIONS
# =====================================================

def get_follow_up_recommendations(
    answers
):
    """
    Contextual recommendations.
    """

    recommendations = []

    for question, answer in answers.items():

        q = question.lower()
        a = answer.lower()

        if "credentials" in q and a.startswith("yes"):

            recommendations.append(
                "Reset affected passwords immediately."
            )

            recommendations.append(
                "Revoke active sessions."
            )

        if "mfa" in q and a.startswith("no"):

            recommendations.append(
                "Enable Multi-Factor Authentication."
            )

        if (
            "customer information" in q
            and a.startswith("yes")
        ):

            recommendations.append(
                "Conduct a Belize Data Protection impact assessment."
            )

        if (
            "files encrypted" in q
            and a.startswith("yes")
        ):

            recommendations.append(
                "Disconnect affected systems immediately."
            )

        if (
            "ransom note" in q
            and a.startswith("yes")
        ):

            recommendations.append(
                "Escalate immediately and preserve evidence."
            )

    return list(
        set(recommendations)
    )
