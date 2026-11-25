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
# INCIDENT PICKER
# =====================================================

INCIDENT_OPTIONS = {
    "✉️ Suspicious Email or Message":
        "Phishing",

    "🔐 Account May Be Compromised":
        "Unauthorized Access",

    "📂 Information May Be Exposed":
        "Data Breach",

    "🔒 Computers Locked or Asking For Money":
        "Ransomware",

    "💻 Lost or Stolen Device":
        "Lost or Stolen Device",

    "🌐 Website or Service Problem":
        "Unknown",

    "🦠 Malware or Suspicious Software":
        "Unknown",

    "❓ I'm Not Sure":
        "Unknown"
}

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

logo_col, title_col = st.columns(
    [1, 4]
)

with logo_col:

    st.image(
        "assets/LogoOnly.png",
        width=180
    )

with title_col:

    st.title(
        "Dorothy"
    )

    st.subheader(
        "The Belize Cyber First Aid Agent"
    )

    st.write(
        """
Dorothy helps Belizean organizations investigate
cybersecurity incidents, assess business impact,
evaluate privacy concerns, and recommend immediate
response actions.
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

    st.subheader(
        "Investigation Status"
    )

    if st.session_state.assessment_started:

        assessment = (
            st.session_state.assessment
        )

        progress = get_progress(
            assessment["incident_type"],
            st.session_state.answers
        )

        st.progress(progress)

        st.write(
            f"Progress: {progress}%"
        )

        missing = (
            get_missing_information(
                assessment["incident_type"],
                st.session_state.answers
            )
        )

        st.markdown(
            "### Still Needed"
        )

        if missing:

            for item in missing[:5]:

                st.write(
                    f"⬜ {item}"
                )

        else:

            st.success(
                "Investigation Complete"
            )

    else:

        st.info(
            "Investigation not started."
        )

    st.divider()

    st.markdown(
        """
### Frameworks

- NIST CSF 2.0
- Belize Data Protection Act
- Incident Response Best Practices
"""
    )

# =====================================================
# START SCREEN
# =====================================================

if not st.session_state.assessment_started:

    st.header(
        "Cyber First Aid"
    )

    st.write(
        """
Select the option that best matches
what you're experiencing.
"""
    )

    selected_option = st.radio(
        "What best describes the situation?",
        list(INCIDENT_OPTIONS.keys())
    )

    additional_details = st.text_area(
        "Additional details (optional)",
        height=150,
        placeholder="""
Examples:

Several computers are locked.

A suspicious Microsoft login page was opened.

A laptop containing customer information was lost.
"""
    )

    if st.button(
        "Start Investigation",
        type="primary"
    ):

        incident_type = (
            INCIDENT_OPTIONS[
                selected_option
            ]
        )

        try:

            assessment = create_assessment(
                incident_type.lower()
            )

        except Exception:

            assessment = {
                "incident_type":
                    incident_type,
                "business_severity":
                    "Medium",
                "priority":
                    "Normal",
                "response_target":
                    "Same Business Day",
                "privacy_impact":
                    "Unknown",
                "escalation_required":
                    False,
                "data_protection_review":
                    False,
                "actions":
                    [
                        "Gather additional information."
                    ]
            }

        if (
            assessment["incident_type"]
            == "Unknown"
        ):

            assessment["incident_type"] = (
                incident_type
            )

        st.session_state.assessment = (
            assessment
        )

        st.session_state.assessment_started = True

        first_question = (
            get_next_question(
                assessment["incident_type"],
                0,
                {}
            )
        )

        st.session_state.current_question = (
            first_question
        )

        greeting = f"""
### Investigation Started

Selected Category:

**{selected_option}**

Likely Incident Type:

**{assessment['incident_type']}**

I'll guide you through a structured investigation.

If you do not know an answer,
simply reply:

**Unsure**
"""

        if first_question:

            greeting += f"\n\n### Question 1\n\n{first_question}"

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": greeting
            }
        ]

        st.rerun()

# =====================================================
# INVESTIGATION
# =====================================================

if st.session_state.assessment_started:

    assessment = (
        st.session_state.assessment
    )

    analysis = analyse_answers(
        st.session_state.answers
    )

    confidence = (
        get_confidence_score(
            st.session_state.answers
        )
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

    st.header(
        "Dorothy's Current Assessment"
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

    chat_col, info_col = st.columns(
        [2, 1]
    )

    # =================================================
    # CHAT
    # =================================================

    with chat_col:

        st.subheader(
            "Investigation Chat"
        )

        for message in (
            st.session_state.messages
        ):

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

                next_question = (
                    get_next_question(
                        assessment["incident_type"],
                        len(
                            st.session_state.answers
                        ),
                        st.session_state.answers
                    )
                )

                if next_question:

                    current_analysis = (
                        analyse_answers(
                            st.session_state.answers
                        )
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
- Findings Identified: **{len(current_analysis['findings'])}**

### Next Question

{next_question}
"""
                        }
                    )

                else:

                    st.session_state.investigation_complete = True

                st.rerun()

    # =================================================
    # FINDINGS PANEL
    # =================================================

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
                "No major indicators identified yet."
            )

        st.divider()

        st.subheader(
            "Recommendations"
        )

        if recommendations:

            for item in recommendations:

                st.info(
                    item
                )

        else:

            st.write(
                "Recommendations will appear as Dorothy gathers information."
            )

        st.divider()

        st.subheader(
            "Timeline"
        )

        if st.session_state.timeline:

            for item in (
                st.session_state.timeline
            ):

                st.write(
                    f"• {item}"
                )

        else:

            st.write(
                "Timeline will appear during investigation."
            )

# =====================================================
# FINAL RESULTS
# =====================================================

if st.session_state.investigation_complete:

    assessment = (
        st.session_state.assessment
    )

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
        f"**Priority:** {assessment.get('priority', 'Normal')}"
    )

    st.write(
        f"**Response Target:** {assessment.get('response_target', 'Same Business Day')}"
    )

    st.divider()

    st.subheader(
        "Immediate Actions"
    )

    for action in assessment.get(
        "actions",
        []
    ):

        st.success(
            action
        )

    for recommendation in recommendations:

        st.info(
            recommendation
        )

    st.divider()

    if st.button(
        "Start New Investigation"
    ):

        for key in list(
            DEFAULT_STATE.keys()
        ):

            if key in st.session_state:

                del st.session_state[key]

        st.rerun()

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    """
Dorothy v3.0

Features:
• Cyber First Aid Incident Picker
• Guided Investigations
• Confidence Scoring
• Live Risk Assessment
• Investigation Timeline
• Incident-Specific Playbooks
"""
)
