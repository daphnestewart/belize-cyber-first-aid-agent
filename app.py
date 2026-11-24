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

if "messages" not in st.session_state:
    st.session_state.messages = []

if "assessment_started" not in st.session_state:
    st.session_state.assessment_started = False

if "incident_description" not in st.session_state:
    st.session_state.incident_description = ""

if "assessment" not in st.session_state:
    st.session_state.assessment = None

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "current_question" not in st.session_state:
    st.session_state.current_question = None

if "investigation_complete" not in st.session_state:
    st.session_state.investigation_complete = False

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
        "The Belize Cyber First Aid Agent by Daphne Stewart"
    )

    st.write(
        """
        Dorothy assists Belizean organizations with
        cybersecurity incident investigation, triage,
        impact assessment, and response planning.

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
2. Answer Questions
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
        height=180,
        placeholder="""
Example:

An employee entered Microsoft 365 credentials
into a fake login page.
"""
    )

    if st.button(
        "Begin Investigation",
        type="primary"
    ):

        if incident_description.strip():

            assessment = create_assessment(
                incident_description
            )

            st.session_state.incident_description = (
                incident_description
            )

            st.session_state.assessment = (
                assessment
            )

            st.session_state.assessment_started = (
                True
            )

            first_question = get_next_question(
                assessment["incident_type"],
                0
            )

            st.session_state.current_question = (
                first_question
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content":
                    f"""
I have classified this as:

**{assessment['incident_type']}**

To properly assess business and privacy impacts, I need to ask a few questions.

Question 1:

{first_question}
                    """
                }
            )

            st.rerun()

# =====================================================
# INVESTIGATION
# =====================================================

if st.session_state.assessment_started:

    assessment = st.session_state.assessment

    progress = get_progress(
        assessment["incident_type"],
        st.session_state.question_index
    )

    st.progress(progress)

    st.caption(
        f"Investigation Progress: {progress}%"
    )

    st.subheader(
        f"Incident Type: {assessment['incident_type']}"
    )

    # Display Chat History

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
            "Type your answer..."
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

            st.session_state.question_index += 1

            next_question = get_next_question(
                assessment["incident_type"],
                st.session_state.question_index
            )

            if next_question:

                st.session_state.current_question = (
                    next_question
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content":
                        next_question
                    }
                )

            else:

                st.session_state.investigation_complete = (
                    True
                )

            st.rerun()

# =====================================================
# RESULTS
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

    recommendations = (
        generate_recommendations(
            st.session_state.answers
        )
    )

    st.divider()

    st.header("Dorothy's Assessment")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Incident Type",
            assessment["incident_type"]
        )

    with col2:

        st.metric(
            "Business Severity",
            adjusted_severity
        )

    with col3:

        st.metric(
            "Privacy Impact",
            assessment["privacy_impact"]
        )

    st.divider()

    st.subheader(
        "Key Findings"
    )

    if analysis["findings"]:

        for finding in analysis["findings"]:

            st.warning(finding)

    else:

        st.info(
            "No major risk indicators identified."
        )

    st.divider()

    st.subheader(
        "Assessment Summary"
    )

    st.write(
        f"**Priority:** {assessment['priority']}"
    )

    st.write(
        f"**Response Target:** {assessment['response_target']}"
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
        "Recommended Immediate Actions"
    )

    for action in assessment["actions"]:

        st.success(action)

    for recommendation in recommendations:

        st.info(recommendation)

    st.divider()

    st.subheader(
        "NIST CSF 2.0 Alignment"
    )

    st.info(
        " • ".join(
            assessment["nist_functions"]
        )
    )

    st.divider()

    st.subheader(
        "Investigation Answers"
    )

    for question, answer in (
        st.session_state.answers.items()
    ):

        st.markdown(
            f"**{question}**"
        )

        st.write(answer)

    st.divider()

    if st.button(
        "Start New Investigation"
    ):

        st.session_state.messages = []

        st.session_state.assessment_started = False

        st.session_state.incident_description = ""

        st.session_state.assessment = None

        st.session_state.answers = {}

        st.session_state.question_index = 0

        st.session_state.current_question = None

        st.session_state.investigation_complete = False

        st.rerun()

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    """
Dorothy v2

The Belize Cyber First Aid Agent

Guiding organizations through cybersecurity
incident investigations one question at a time.
"""
)
