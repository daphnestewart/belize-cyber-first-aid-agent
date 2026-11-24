import streamlit as st

from src.incident_assessor import create_assessment

from src.conversation_engine import (
    get_next_question,
    get_progress,
    analyse_answers,
    adjust_severity,
    generate_recommendations
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Dorothy",
    page_icon="assets/LogoOnly.png",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================

defaults = {
    "messages": [],
    "assessment_started": False,
    "incident_description": "",
    "assessment": None,
    "answers": {},
    "question_index": 0,
    "current_question": None,
    "investigation_complete": False
}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value


# =====================================================
# HEADER
# =====================================================

col1, col2 = st.columns([1, 4])

with col1:
    st.image(
        "assets/LogoOnly.png",
        width=220
    )

with col2:

    st.title("Dorothy")

    st.subheader(
        "The Belize Cyber First Aid Agent"
    )

    st.write(
        """
        Dorothy assists Belizean organizations with
        cybersecurity incident investigation,
        privacy impact assessment,
        and response planning.

        Inspired by Nurse Dorothy Mae Bradley.
        """
    )

st.divider()

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
### Investigation Process

1. Describe Incident
2. Interview
3. Assess Risk
4. Review Findings
5. Take Action
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
# START ASSESSMENT
# =====================================================

if not st.session_state.assessment_started:

    incident_description = st.text_area(
        "Describe the cybersecurity incident",
        height=180
    )

    if st.button(
        "Begin Investigation",
        type="primary"
    ):

        if incident_description.strip():

            assessment = create_assessment(
                incident_description
            )

            st.session_state.assessment = assessment

            st.session_state.incident_description = (
                incident_description
            )

            st.session_state.assessment_started = True

            first_question = get_next_question(
                assessment["incident_type"],
                0,
                {}
            )

            st.session_state.current_question = (
                first_question
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content":
                    f"""
I have classified this incident as:

**{assessment['incident_type']}**

I need additional information before finalizing the assessment.

{first_question}
"""
                }
            )

            st.rerun()

# =====================================================
# INVESTIGATION MODE
# =====================================================

if st.session_state.assessment_started:

    assessment = st.session_state.assessment

    # ==========================================
    # LIVE ANALYSIS
    # ==========================================

    analysis = analyse_answers(
        st.session_state.answers
    )

    adjusted_severity = adjust_severity(
        assessment["business_severity"],
        analysis["score"]
    )

    recommendations = generate_recommendations(
        st.session_state.answers
    )

    # ==========================================
    # LIVE STATUS DASHBOARD
    # ==========================================

    st.subheader("Dorothy's Current Assessment")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Incident Type",
            assessment["incident_type"]
        )

    with c2:
        st.metric(
            "Severity",
            adjusted_severity
        )

    with c3:
        st.metric(
            "Privacy Impact",
            analysis["privacy_impact"]
        )

    with c4:
        st.metric(
            "Risk Score",
            analysis["score"]
        )

    progress = get_progress(
        assessment["incident_type"],
        st.session_state.answers
    )

    st.progress(progress)

    st.caption(
        f"Investigation Progress: {progress}%"
    )

    if analysis["findings"]:

        st.info(
            f"{len(analysis['findings'])} risk indicators currently identified."
        )

    st.divider()

    # ==========================================
    # CHAT + LIVE PANEL
    # ==========================================

    chat_col, findings_col = st.columns(
        [2, 1]
    )

    # ==========================================
    # CHAT WINDOW
    # ==========================================

    with chat_col:

        st.subheader(
            "Investigation Chat"
        )

        for message in st.session_state.messages:

            with st.chat_message(
                message["role"]
            ):

                st.markdown(
                    message["content"]
                )

        if (
            not st.session_state.investigation_complete
        ):

            user_response = st.chat_input(
                "Enter your response..."
            )

            if user_response:

                current_question = (
                    st.session_state.current_question
                )

                st.session_state.answers[
                    current_question
                ] = user_response

                st.session_state.messages.append(
                    {
                        "role": "user",
                        "content": user_response
                    }
                )

                next_question = get_next_question(
                    assessment["incident_type"],
                    len(
                        st.session_state.answers
                    ),
                    st.session_state.answers
                )

                if next_question:

                    st.session_state.current_question = (
                        next_question
                    )

                    # LIVE ANALYSIS MESSAGE

                    current_analysis = analyse_answers(
                        st.session_state.answers
                    )

                    current_severity = (
                        adjust_severity(
                            assessment[
                                "business_severity"
                            ],
                            current_analysis["score"]
                        )
                    )

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content":
                            f"""
Current Severity: **{current_severity}**

Current Privacy Impact: **{current_analysis['privacy_impact']}**

Next Question:

{next_question}
"""
                        }
                    )

                else:

                    st.session_state.investigation_complete = (
                        True
                    )

                st.rerun()

    # ==========================================
    # LIVE FINDINGS
    # ==========================================

    with findings_col:

        st.subheader(
            "Current Findings"
        )

        if analysis["findings"]:

            for finding in analysis["findings"]:

                st.warning(finding)

        else:

            st.success(
                "No major indicators identified yet."
            )

        st.subheader(
            "Recommendations"
        )

        if recommendations:

            for item in recommendations:

                st.info(item)

        else:

            st.write(
                "Recommendations will appear as risk indicators are identified."
            )

# =====================================================
# FINAL RESULTS
# =====================================================

if st.session_state.investigation_complete:

    assessment = st.session_state.assessment

    analysis = analyse_answers(
        st.session_state.answers
    )

    adjusted_severity = adjust_severity(
        assessment["business_severity"],
        analysis["score"]
    )

    recommendations = generate_recommendations(
        st.session_state.answers
    )

    st.divider()

    st.header(
        "Final Investigation Assessment"
    )

    st.success(
        "Dorothy has completed the investigation."
    )

    st.write(
        f"**Business Severity:** {adjusted_severity}"
    )

    st.write(
        f"**Privacy Impact:** {analysis['privacy_impact']}"
    )

    st.write(
        f"**Risk Score:** {analysis['score']}"
    )

    st.write(
        f"**Escalation Required:** {'Yes' if assessment['escalation_required'] else 'No'}"
    )

    st.write(
        f"**Belize Data Protection Review:** {'Required' if assessment['data_protection_review'] else 'Not Required'}"
    )

    st.divider()

    st.subheader(
        "Immediate Actions"
    )

    for action in assessment["actions"]:

        st.success(action)

    for recommendation in recommendations:

        st.info(recommendation)

    st.divider()

    if st.button(
        "Start New Investigation"
    ):

        for key in list(defaults.keys()):
            del st.session_state[key]

        st.rerun()

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    """
Dorothy v2.1

The Belize Cyber First Aid Agent

Now providing live investigation updates,
dynamic risk scoring,
branching questions,
and real-time recommendations.
"""
)
