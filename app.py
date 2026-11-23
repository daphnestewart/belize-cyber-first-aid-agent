import streamlit as st

st.set_page_config(
    page_title="Belize Cyber First Aid Agent",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Belize Cyber First Aid Agent")

st.write("""
Welcome to the Belize Cyber First Aid Agent.

Describe a cybersecurity incident below to begin an assessment.
""")

incident = st.text_area(
    "Describe the incident",
    height=150
)

if st.button("Assess Incident"):

    if incident.strip():
        st.success("Assessment engine will be connected next.")
        st.write("Incident Description:")
        st.write(incident)

    else:
        st.warning("Please enter an incident description.")
