# Dorothy

## The Belize Cyber First Aid Agent

Dorothy is an AI-assisted cybersecurity incident response platform designed to help Belizean small and medium-sized businesses identify, assess, document, and respond to cybersecurity incidents.

Named in honor of Nurse Dorothy Mae Bradley, this project aims to provide practical guidance and support during cybersecurity incidents while promoting resilience, preparedness, and data protection awareness.

---

## Mission

Many small businesses lack dedicated cybersecurity teams and struggle to respond effectively when cyber incidents occur.

Dorothy helps organizations:

- Identify cybersecurity incidents
- Assess business impact
- Assess privacy impact
- Understand escalation requirements
- Follow incident response playbooks
- Support Belize Data Protection Act considerations
- Strengthen cybersecurity resilience

---

## Features

### Incident Classification

Dorothy currently supports:

- Phishing
- Unauthorized Access
- Data Breach
- Ransomware
- Lost or Stolen Device

---

### Business Severity Assessment

Classifies incidents as:

- Low
- Medium
- High
- Critical

---

### Privacy Impact Assessment

Separately evaluates privacy risks relating to:

- Customer information
- Employee information
- Financial information
- Sensitive personal data

---

### Belize Data Protection Considerations

Dorothy helps organizations identify incidents that may require further privacy review by assessing:

- Personal data exposure
- Sensitive personal data exposure
- Potential impact on affected individuals

---

### NIST Cybersecurity Framework (CSF) 2.0 Alignment

Dorothy aligns incident response activities with:

- Govern
- Identify
- Protect
- Detect
- Respond
- Recover

---

### Incident Response Playbooks

Built-in support for:

- Phishing Incident Playbook
- Unauthorized Access Incident Playbook
- Data Breach Incident Playbook
- Ransomware Incident Playbook
- Lost or Stolen Device Incident Playbook

---

### Guided Incident Triage

Dorothy provides:

- Immediate response actions
- Recommended triage questions
- Escalation recommendations
- Playbook references

---

## Technology Stack

- Python
- Streamlit
- GitHub
- GitHub Codespaces
- JSON Knowledge Base

Future Integrations:

- Microsoft Copilot Studio
- Azure AI Services
- Microsoft Teams
- Automated Incident Report Generation

---

## Project Structure

```text
dorothy/
│
├── app.py
├── README.md
├── LICENSE
├── .gitignore
│
├── assets/
│   └── Dorothy.jpg
│
├── docs/
│   └── incident-classification.md
│
├── playbooks/
│   ├── phishing.md
│   ├── ransomware.md
│   ├── data-breach.md
│   ├── unauthorized-access.md
│   └── lost-device.md
│
├── src/
│   ├── incident_assessor.py
│   │
│   └── data/
│       ├── incidents.json
│       ├── severity_matrix.json
│       ├── privacy_impact_matrix.json
│       ├── personal_data_categories.json
│       ├── incident_questions.json
│       ├── escalation_rules.json
│       ├── report_template.json
│       └── playbook_mapping.json
│
└── samples/
```

---

## Running Dorothy

### Install Dependencies

```bash
pip install streamlit
```

### Launch Application

```bash
streamlit run app.py
```

---

## Example Incident

### Incident Description

```text
An employee entered Microsoft 365 credentials into a fake login page. Customer information may have been accessible.
```

### Dorothy Assessment

```text
Incident Type: Phishing

Business Severity: Medium

Privacy Impact: High

Escalation Required: Yes

Belize Data Protection Review: Required

Recommended Playbook:
playbooks/phishing.md
```

---

## Roadmap

### Version 1.0

- [x] Incident classification
- [x] Severity assessment
- [x] Privacy impact assessment
- [x] NIST CSF 2.0 alignment
- [x] Streamlit interface
- [x] Incident playbooks

### Version 2.0

- [ ] Incident report generation
- [ ] Executive summary generation
- [ ] Downloadable PDF reports
- [ ] Enhanced escalation engine

### Version 3.0

- [ ] Microsoft Copilot Studio integration
- [ ] Teams chatbot integration
- [ ] Azure AI integration
- [ ] Knowledge base expansion

### Version 4.0

- [ ] Industry-specific guidance
- [ ] Business continuity support
- [ ] Security awareness module
- [ ] Multi-user capabilities

---

## Inspiration

Dorothy is named in honor of Nurse Dorothy Mae Bradley.

The project reflects the values of support, guidance, and resilience by helping Belizean businesses navigate cybersecurity incidents with greater confidence and preparedness.

---

## Author

Daphne Stewart 
Cybersecurity Enthusiast | GIAC Certified Incident Handler

---

## License

This project is licensed under the MIT License.

See the LICENSE file for details.
