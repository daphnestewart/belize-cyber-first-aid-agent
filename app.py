import streamlit as st

from src.incident_assessor import create_assessment

from src.conversation_engine import (
    get_next_question,
    get_progress,
    analyse_answers,
    adjust_severity,
    generate_recommendations,
    get_confidence_score,
    get_missing_information
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

DEFAULT_STATE = {
    "assessment_started": False,
    "assessment": None,
    "messages": [],
    "answers": {},
    "current_question": None,
    "timeline": [],
    "investigation_complete": False
}

for key, value in DEFAULT_STATE.items():

    if key not in st.session_state:

        if isinstance(value, list):
            st.session_state[key] = []

        elif isinstance(value, dict):
            st.session_state[key] = {}

        else:
            st.session_state[key] = value

# =====================================================
# HEADER
# =====================================================

header_col1, header_col2 = st.columns([1, 4])

with header_col1:

    st.image(
        "assets/LogoOnly.png",
        width=180
    )

with header_col2:

    st.title("Dorothy")

    st.subheader(
        "The Belize Cyber First Aid Agent"
    )

    st.write(
        """
Dorothy helps Belizean organizations investigate, assess,
and respond to cybersecurity incidents.

She gathers information step-by-step, evaluates business
impact, privacy impact, and provides response guidance.
"""
    )

st.divider()

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("## Investigation Status")

    if st.session_state.assessment:

        assessment = st.session_state.assessment

        progress = get_progress(
            assessment["incident_type"],
            st.session_state.answers
        )

        st.progress(progress)

        st.write(
            f"Progress: {progress}%"
        )

        missing = get_missing_information(
            assessment["incident_type"],
            st.session_state.answers
        )

        st.markdown("### Still Needed")

        if missing:

            for item in missing[:5]:

                st.write(
                    f"⬜ {item}"
                )

        else:

            st.success(
                "Investigation complete"
            )

# =====================================================
# START SCREEN
# =====================================================

if not st.session_state.assessment_started:

    st.header(
        "Start an Investigation"
    )

    incident_description = st.text_area(
        "Describe what happened",
        height=180,
        placeholder="""
Examples:

An employee entered credentials into a fake Microsoft login page.

All computers are locked and a message is asking for money.

A laptop containing customer information was stolen.
"""
    )

    if st.button(
        "Begin Investigation",
        type="primary"
    ):

        if not incident_description.strip():

            st.warning(
                "Please provide a description."
            )

        else:

            assessment = create_assessment(
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
I believe this may be:

**{assessment['incident_type']}**

To understand the situation better, I need some additional information.

**Question 1**

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

    analysis = analyse_answers(
        st.session_state.answers
    )

    confidence = get_confidence_score(
        st.session_state.answers
    )

    severity = adjust_severity(
        assessment["business_severity"],
        analysis["score"]
    )

    recommendations = (
        generate_recommendations(
            assessment["incident_type"],
            st.session_state.answers
        )
    )

    # ==========================================
    # LIVE DASHBOARD
    # ==========================================

    st.header(
        "Current Assessment"
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:

        st.metric(
            "Incident",
            assessment["incident_type"]
        )

    with c2:

        st.metric(
            "Severity",
            severity
        )

    with c3:

        st.metric(
            "Privacy",
            analysis["privacy_impact"]
        )

    with c4:

        st.metric(
            "Risk Score",
            analysis["score"]
        )

    with c5:

        st.metric(
            "Confidence",
            f"{confidence}%"
        )

    st.divider()

    # ==========================================
    # LAYOUT
    # ==========================================

    chat_col, info_col = st.columns(
        [2, 1]
    )

    # ==========================================
    # CHAT
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

        if not st.session_state.investigation_complete:

            user_response = st.chat_input(
                "Type your response..."
            )

            if user_response:

                current_question = (
                    st.session_state.current_question
                )

                st.session_state.answers[
                    current_question
                ] = user_response

                st.session_state.timeline.append(
                    f"{current_question} → {user_response}"
                )

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

                    current_analysis = analyse_answers(
                        st.session_state.answers
                    )

                    current_confidence = (
                        get_confidence_score(
                            st.session_state.answers
                        )
                    )

                    current_severity = (
                        adjust_severity(
                            assessment[
                                "business_severity"
                            ],
                            current_analysis[
                                "score"
                            ]
                        )
                    )

                    st.session_state.current_question = (
                        next_question
                    )

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content":
                            f"""
### Current Assessment

- Severity: **{current_severity}**
- Privacy Impact: **{current_analysis['privacy_impact']}**
- Confidence: **{current_confidence}%**
- Findings: **{len(current_analysis['findings'])}**

### Next Question

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
    # RIGHT PANEL
    # ==========================================

    with info_col:

        st.subheader(
            "Findings"
        )

        if analysis["findings"]:

            for finding in analysis["findings"]:

                st.warning(
                    finding
                )

        else:

            st.success(
                "No significant indicators identified yet."
            )

        st.divider()

        st.subheader(
            "Recommendations"
        )

        if recommendations:

            for item in recommendations:

                st.info(item)

        else:

            st.write(
                "Recommendations will appear as information is gathered."
            )

        st.divider()

        st.subheader(
            "Timeline"
        )

        if st.session_state.timeline:

            for item in st.session_state.timeline:

                st.write(
                    f"• {item}"
                )

# =====================================================
# FINAL ASSESSMENT
# =====================================================

if st.session_state.investigation_complete:

    assessment = st.session_state.assessment

    analysis = analyse_answers(
        st.session_state.answers
    )

    severity = adjust_severity(
        assessment["business_severity"],
        analysis["score"]
    )

    recommendations = (
        generate_recommendations(
            assessment["incident_type"],
            st.session_state.answers
        )
    )

    st.divider()

    st.header(
        "Final Investigation Assessment"
    )

    st.success(
        "Dorothy has completed the investigation."
    )

    st.write(
        f"**Incident Type:** {assessment['incident_type']}"
    )

    st.write(
        f"**Business Severity:** {severity}"
    )

    st.write(
        f"**Privacy Impact:** {analysis['privacy_impact']}"
    )

    st.write(
        f"**Risk Score:** {analysis['score']}"
    )

    st.write(
        f"**Priority:** {assessment['priority']}"
    )

    st.write(
        f"**Response Target:** {assessment['response_target']}"
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

    if st.button(
        "Start New Investigation"
    ):

        for key in list(DEFAULT_STATE.keys()):

            if key in st.session_state:

                del st.session_state[key]

        st.rerun()

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    """
Dorothy v2.2

Features:
• Dynamic investigations
• Confidence scoring
• Missing information tracking
• Investigation timeline
• Live assessment updates
• Incident-specific playbooks
"""
)
