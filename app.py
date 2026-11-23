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
        Dorothy helps Belizean small and medium-sized
        businesses identify, assess, document, and
        respond to cybersecurity incidents.

        Inspired by Dorothy Mae Bradley.
        """
    )

st.divider()


# =====================================================
# INCIDENT INPUT
# =====================================================

st.header("Cybersecurity Incident Assessment")

incident_description = st.text_area(
    label="Describe the cybersecurity incident",
    height=200,
    placeholder="""
Example:

An employee entered their Microsoft 365 credentials into
a fake login page. Customer records may have been exposed.
"""
)

assess_button = st.button(
    "Assess Incident",
    type="primary"
)


# =====================================================
# RUN ASSESSMENT
# =====================================================

if assess_button:

    if not incident_description.strip():

        st.warning(
            "Please enter an incident description."
        )

    else:

        result = create_assessment(
            incident_description
        )

        st.success(
            "Assessment completed successfully."
        )

        # =============================================
        # TOP METRICS
        # =============================================

        metric1, metric2, metric3 = st.columns(3)

        with metric1:
            st.metric(
                "Incident Type",
                result["incident_type"]
            )

        with metric2:
            st.metric(
                "Business Severity",
                result["business_severity"]
            )

        with metric3:
            st.metric(
                "Privacy Impact",
                result["privacy_impact"]
            )

        st.divider()

        # =============================================
        # SUMMARY
        # =============================================

        st.subheader("Assessment Summary")

        left_col, right_col = st.columns(2)

        with left_col:

            st.markdown(
                f"""
**Priority:** {result['priority']}

**Response Target:** {result['response_target']}

**Escalation Required:** {"Yes" if result['escalation_required'] else "No"}
"""
            )

        with right_col:

            st.markdown(
                f"""
**Belize Data Protection Review:** {"Required" if result['data_protection_review'] else "Not Required"}

**Recommended Playbook:** `{result['playbook']}`
"""
            )

        st.divider()

        # =============================================
        # IMMEDIATE ACTIONS
        # =============================================

        st.subheader("Immediate Actions")

        for action in result["actions"]:
            st.markdown(f"✅ {action}")

        st.divider()

        # =============================================
        # NIST FUNCTIONS
        # =============================================

        st.subheader(
            "NIST Cybersecurity Framework (CSF) 2.0"
        )

        for function in result["nist_functions"]:
            st.markdown(f"- {function}")

        st.divider()

        # =============================================
        # TRIAGE QUESTIONS
        # =============================================

        st.subheader(
            "Recommended Triage Questions"
        )

        for section, questions in result[
            "questions"
        ].items():

            st.markdown(
                f"### {section.replace('_', ' ').title()}"
            )

            for question in questions:
                st.write(f"• {question}")

        st.divider()

        # =============================================
        # INCIDENT DESCRIPTION
        # =============================================

        with st.expander(
            "View Submitted Incident Description"
        ):

            st.write(
                incident_description
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
**Mission**

Help Belizean businesses:

- Identify incidents
- Assess impact
- Understand privacy risks
- Improve response readiness
"""
    )

    st.markdown("---")

    st.markdown(
        """
**Frameworks Supported**

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
    Dorothy v1.0 | The Belize Cyber First Aid Agent

    Supporting cybersecurity incident classification,
    privacy impact assessment, and response planning
    for Belizean small and medium-sized businesses.
    """
)
