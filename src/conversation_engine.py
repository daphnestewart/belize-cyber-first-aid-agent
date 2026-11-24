REQUIRED_FIELDS = {
    "Phishing": [
        "credentials_entered",
        "mfa_enabled",
        "customer_data",
        "multiple_users"
    ],

    "Unauthorized Access": [
        "admin_account",
        "customer_data",
        "multiple_users"
    ],

    "Data Breach": [
        "customer_data",
        "employee_data",
        "sensitive_data",
        "records_affected"
    ],

    "Ransomware": [
        "systems_affected",
        "backups_available",
        "business_disruption"
    ],

    "Lost or Stolen Device": [
        "device_encrypted",
        "customer_data",
        "remote_wipe_attempted"
    ]
}


QUESTION_BANK = {

    "credentials_entered":
        "Were credentials entered into the suspicious website?",

    "mfa_enabled":
        "Was Multi-Factor Authentication enabled?",

    "customer_data":
        "Did the affected account or system contain customer information?",

    "multiple_users":
        "Were multiple users affected?",

    "admin_account":
        "Was an administrator account involved?",

    "employee_data":
        "Did the system contain employee data?",

    "sensitive_data":
        "Did the system contain sensitive personal data?",

    "records_affected":
        "Approximately how many records may be affected?",

    "systems_affected":
        "How many systems are affected?",

    "backups_available":
        "Are backups available?",

    "business_disruption":
        "Has business operation been disrupted?",

    "device_encrypted":
        "Was the device encrypted?",

    "remote_wipe_attempted":
        "Has remote wipe been attempted?"
}


def get_next_question(
    incident_type,
    answers
):

    required_fields = REQUIRED_FIELDS.get(
        incident_type,
        []
    )

    for field in required_fields:

        if field not in answers:

            return field, QUESTION_BANK[field]

    return None, None
