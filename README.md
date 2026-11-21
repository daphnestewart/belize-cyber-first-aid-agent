
# Belize Cyber First Aid Agent

An AI-powered incident response assistant designed to help small and medium-sized businesses in Belize identify, assess, document, and respond to cybersecurity incidents.

The project aims to provide practical, easy-to-follow incident handling guidance for organizations that may not have dedicated cybersecurity personnel. The assistant helps users classify incidents, determine severity, follow response playbooks, and generate incident reports while promoting cybersecurity awareness and business resilience.

---

## Mission

Many small businesses are targets of cyber threats such as phishing, ransomware, account compromise, and data breaches but lack access to dedicated security teams.

Belize Cyber First Aid Agent seeks to bridge that gap by providing:

- Immediate incident guidance
- Severity assessment
- Incident documentation support
- Security awareness recommendations
- Business continuity-focused response actions

---

## Features

### Incident Classification

Identify common cybersecurity incidents including:

- Phishing
- Malware
- Ransomware
- Unauthorized Access
- Business Email Compromise
- Data Breaches
- Lost or Stolen Devices
- Service Disruptions

### Severity Assessment

Assess incidents based on impact and risk levels:

- Low
- Medium
- High
- Critical

### Incident Response Playbooks

Provide step-by-step guidance for:

- Containment
- Evidence preservation
- Recovery actions
- Follow-up recommendations

### Incident Report Generation

Generate structured reports containing:

- Incident summary
- Timeline
- Affected systems
- Actions taken
- Recommendations

### Compliance Awareness

Support awareness of:

- Belize Data Protection requirements
- Documentation best practices
- Incident recordkeeping

---

## Project Structure

```text
belize-cyber-first-aid-agent/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   └── incident-classification.md
│
├── playbooks/
│   ├── phishing.md
│   ├── ransomware.md
│   ├── data-breach.md
│   ├── lost-device.md
│   └── unauthorized-access.md
│
├── samples/
│   ├── sample-phishing-report.md
│   └── sample-data-breach-report.md
│
└── src/
    └── incident_assessor.py
```

---

## Technology Stack

- Python
- Streamlit
- GitHub Copilot
- Microsoft Copilot Studio
- Azure AI Services
- GitHub Actions

---

## Roadmap

### Version 1 (MVP)

- [ ] Incident classification
- [ ] Severity scoring
- [ ] Response playbooks
- [ ] Incident report templates

### Version 2

- [ ] Streamlit web interface
- [ ] AI-generated recommendations
- [ ] Downloadable incident reports
- [ ] Risk scoring system

### Version 3

- [ ] Azure OpenAI integration
- [ ] Copilot Studio deployment
- [ ] Microsoft Teams integration
- [ ] Dashboard and analytics

### Version 4

- [ ] Knowledge base for Belize SMEs
- [ ] Cyber awareness resources
- [ ] Industry-specific guidance
- [ ] Multi-user support

---

## Example Use Case

**User Input**

> An employee clicked a suspicious invoice attachment and entered their Microsoft 365 password.

**Agent Response**

**Incident Type:** Phishing

**Severity:** Medium

**Recommended Actions:**

1. Reset the affected password immediately.
2. Enable Multi-Factor Authentication (MFA).
3. Review account sign-in logs.
4. Preserve the suspicious email.
5. Notify management and document the incident.

---

## Future Goals

- Support small businesses across Belize.
- Promote cybersecurity awareness.
- Provide accessible incident handling guidance.
- Support educational and community cybersecurity initiatives.
- Align with cybersecurity best practices including the NIST Cybersecurity Framework.

---

## Contributing

Contributions, suggestions, and feedback are welcome.

Please open an issue or submit a pull request to help improve the project.

---

## Author

**Daphne Stewart** 
GIAC Certified Incident Handler | AI & Security Advocate

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
