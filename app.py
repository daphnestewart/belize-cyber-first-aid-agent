import streamlit as st
from src.incident_assessor import create_assessment


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Dorothy",
    page_icon="assets/LogoOnly.png",
    layout="wide"
)


# =====================================================
# HELPER FUNCTIONS
# =====================================================

def calculate_risk_score(
    credentials_entered,
    mfa_enabled,
    customer_data,
    multiple_users
):
    score = 0

    if credentials_entered == "Yes":
        score += 2

    if customer_data == "Yes":
        score += 2

    if mfa_enabled == "No":
        score += 1

    if multiple_users == "Yes":
        score += 2

    return score


def determine_adjusted_severity(
    base_severity,
    score
):
    severity_levels = [
        "Low",
        "Medium",
        "High",
        "Critical"
    ]

    if base_severity not in severity_levels:
        return base_severity

    index = severity_levels.index(base_severity)

    if score >= 5:
        index = min(index + 2, 3)

    elif score >= 3:
        index = min(index + 1, 3)

    return severity_levels[index]


def generate_explanation(
    credentials_entered,
    mfa_enabled,
    customer_data,
    multiple_users
):

    reasons = []

    if credentials_entered == "Yes":
        reasons.append(
            "Credentials were entered into a potentially malicious system."
        )

    if customer_data == "Yes":
        reasons.append(
            "Customer information may be affected."
        )

    if mfa_enabled == "No":
        reasons.append(
            "Multi-Factor Authentication was not enabled."
        )

    if multiple_users == "Yes":
        reasons.append(
            "Multiple users appear to be affected."
        )

    return reasons


# =====================================================
# HEADER
# =====================================================

col1, col2 = st.columns([1, 3])

with col1:
    st.image(
        "assets/LogoOnly.png",
        width=250
    )

with col2:

    st.title("Dorothy")

    st.subheader(
        "The Belize Cyber First Aid Agent"
    )

    st.write(
        """
        Dorothy helps Belizean small and medium-sized businesses
        identify, assess, document, and respond to cybersecurity incidents.

        Inspired by Nurse Dorothy Mae Bradley.
        """
    )

st.divider()


# =====================================================
# INCIDENT DESCRIPTION
# =====================================================

st.header("Incident Assessment")

incident_description = st.text_area(
    "Describe the cybersecurity incident",
    height=180,
    placeholder="""
Example:

An employee entered their Microsoft 365 credentials into a fake login page.
Customer information may have been accessible through the account.
"""
)


# =====================================================
# INITIAL ANALYSIS
# =====================================================

if st.button(
    "Start Assessment",
    type="primary"
):

    if not incident_description.strip():

        st.warning(
            "Please enter an incident description."
        )

    else:

        result = create_assessment(
            incident_description
        )

        st.session_state["assessment"] = result
        st.session_state["incident"] = incident_description


# =====================================================
# INTERACTIVE ASSESSMENT
# =====================================================

if "assessment" in st.session_state:

    result = st.session_state["assessment"]

    st.divider()

    st.header("Interactive Assessment")

    credentials_entered = st.radio(
        "Were credentials entered?",
        ["Unknown", "Yes", "No"]
    )

    mfa_enabled = st.radio(
        "Was Multi-Factor Authentication (MFA) enabled?",
        ["Unknown", "Yes", "No"]
    )

    customer_data = st.radio(
        "Was customer information accessible?",
        ["Unknown", "Yes", "No"]
    )

    multiple_users = st.radio(
        "Were multiple users affected?",
        ["Unknown", "Yes", "No"]
    )

    if st.button(
        "Complete Assessment"
    ):

        score = calculate_risk_score(
            credentials_entered,
            mfa_enabled,
            customer_data,
            multiple_users
        )

        adjusted_severity = determine_adjusted_severity(
            result["business_severity"],
            score
        )

        explanations = generate_explanation(
            credentials_entered,
            mfa_enabled,
            customer_data,
            multiple_users
        )

        st.success(
            "Assessment completed."
        )

        # ==========================================
        # METRICS
        # ==========================================

        metric1, metric2, metric3 = st.columns(3)

        with metric1:
            st.metric(
                "Incident Type",
                result["incident_type"]
            )

        with metric2:
            st.metric(
                "Business Severity",
                adjusted_severity
            )

        with metric3:
            st.metric(
                "Privacy Impact",
                result["privacy_impact"]
            )

        st.divider()

        # ==========================================
        # SUMMARY
        # ==========================================

        st.subheader("Assessment Summary")

        left, right = st.columns(2)

        with left:

            st.write(
                f"**Priority:** {result['priority']}"
            )

            st.write(
                f"**Response Target:** {result['response_target']}"
            )

            st.write(
                f"**Risk Score:** {score}"
            )

        with right:

            st.write(
                f"**Escalation Required:** {'Yes' if result['escalation_required'] else 'No'}"
            )

            st.write(
                f"**Belize Data Protection Review:** {'Required' if result['data_protection_review'] else 'Not Required'}"
            )

        st.divider()

        # ==========================================
        # WHY THIS RATING?
        # ==========================================

        st.subheader(
            "Why Dorothy Chose This Rating"
        )

        if explanations:

            for item in explanations:
                st.write(f"✅ {item}")

        else:

            st.write(
                "No additional risk indicators were identified."
            )

        st.divider()

        # ==========================================
        # IMMEDIATE ACTIONS
        # ==========================================

        st.subheader(
            "Recommended Immediate Actions"
        )

        for action in result["actions"]:
            st.success(action)

        if customer_data == "Yes":

            st.warning(
                "Customer information may be involved. Conduct a privacy impact assessment."
            )

        if mfa_enabled == "No":

            st.warning(
                "Enable Multi-Factor Authentication as soon as possible."
            )

        st.divider()

        # ==========================================
        # NIST FUNCTIONS
        # ==========================================

        st.subheader(
            "NIST Cybersecurity Framework Alignment"
        )

        st.info(
            " • ".join(
                result["nist_functions"]
            )
        )

        st.divider()

        # ==========================================
        # TRIAGE QUESTIONS
        # ==========================================

        st.subheader(
            "Additional Investigation Questions"
        )

        for section, questions in result[
            "questions"
        ].items():

            st.markdown(
                f"### {section.replace('_', ' ').title()}"
            )

            for question in questions:

                st.write(
                    f"• {question}"
                )

        st.divider()

        # ==========================================
        # INCIDENT REPORT
        # ==========================================

        report = f"""
DOROTHY INCIDENT REPORT

Incident Type:
{result['incident_type']}

Business Severity:
{adjusted_severity}

Privacy Impact:
{result['privacy_impact']}

Priority:
{result['priority']}

Response Target:
{result['response_target']}

Escalation Required:
{'Yes' if result['escalation_required'] else 'No'}

Belize Data Protection Review:
{'Required' if result['data_protection_review'] else 'Not Required'}

Recommended Playbook:
{result['playbook']}

Risk Score:
{score}

Incident Description:
{st.session_state['incident']}
"""

        st.download_button(
            label="Download Incident Report",
            data=report,
            file_name="dorothy_incident_report.txt",
            mime="text/plain"
        )


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.image(
        "assets/LogoOnly.png",
        use_container_width=True
    )

    st.markdown("## Dorothy")

    st.markdown(
        """
### Mission

Helping Belizean businesses:

- Identify cyber incidents
- Assess business impact
- Assess privacy impact
- Support incident response
- Improve cyber resilience
"""
    )

    st.markdown("---")

    st.markdown(
        """
### Frameworks

- NIST CSF 2.0
- Belize Data Protection Act
- Incident Response Best Practices
"""
    )


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    """
    Dorothy v1.1

    The Belize Cyber First Aid Agent

    Supporting incident assessment, privacy impact analysis,
    and response planning for Belizean small and medium-sized businesses.
    """
)
