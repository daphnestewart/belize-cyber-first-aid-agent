# Incident Classification Framework

## Purpose

The Belize Cyber First Aid Agent Incident Classification Framework provides a structured approach for identifying, assessing, prioritizing, documenting, responding to, and recovering from cybersecurity incidents affecting small and medium-sized businesses (SMEs) in Belize.

The framework is designed to:

- Support consistent incident response practices.
- Protect business operations and organizational assets.
- Protect personal information.
- Promote cyber resilience and business continuity.
- Support privacy and personal data protection obligations under the Belize Data Protection Act, 2021, including security of processing and personal data breach considerations. 【1-ef3315】【2-d8ceb6】
- Align with the NIST Cybersecurity Framework (CSF) 2.0.

---

# Framework Principles

When responding to any cybersecurity incident:

1. Protect people first.
2. Protect business operations.
3. Preserve evidence.
4. Contain threats quickly.
5. Document all actions and decisions.
6. Assess both cybersecurity and privacy impacts.
7. Communicate appropriately with stakeholders.
8. Restore business operations safely.
9. Learn from every incident.
10. Continuously improve security controls.

---

# NIST Cybersecurity Framework (CSF) 2.0 Alignment

This framework aligns incident response activities with the six NIST CSF 2.0 functions:

## Govern

Establish oversight, accountability, risk management, and policies for cybersecurity and data protection.

## Identify

Understand assets, systems, users, risks, and incident scope.

## Protect

Implement safeguards that reduce the likelihood and impact of incidents.

## Detect

Identify potential cybersecurity events through monitoring, reporting, and analysis.

## Respond

Contain, investigate, and manage incidents.

## Recover

Restore operations and improve resilience.

---

# GOVERN

## Purpose

Governance establishes the foundation for effective cybersecurity and incident response.

Every organization should understand:

- What assets it owns.
- What information it processes.
- Who is responsible for security.
- What risks it faces.
- How incidents will be managed.

---

## Roles and Responsibilities

### Business Owner

Responsible for:

- Cybersecurity oversight
- Risk acceptance decisions
- Incident escalation decisions
- Resource allocation
- External communication approval

### Management

Responsible for:

- Incident reporting
- Operational coordination
- Supporting investigations
- Ensuring policy compliance

### Employees

Responsible for:

- Reporting suspicious activity
- Following security procedures
- Protecting company information

### IT Support Provider

Responsible for:

- Technical investigations
- Containment actions
- Security monitoring
- Recovery activities

---

## Governance Documentation

Organizations should maintain:

- Incident Response Plan
- Data Protection Policy
- Acceptable Use Policy
- Password Policy
- Backup and Recovery Policy
- Asset Inventory
- Business Continuity Plan

---

## Risk Management

Organizations should regularly assess:

- Cybersecurity risks
- Data protection risks
- Third-party risks
- Operational risks
- Insider threats

Risk assessments should be reviewed:

- Annually
- After major incidents
- Following significant organizational changes

---

## Continuous Improvement

Following every incident:

- Perform a lessons learned review.
- Evaluate control effectiveness.
- Update procedures.
- Improve training.
- Update playbooks where necessary.

---

# INCIDENT RESPONSE LIFECYCLE

---

## IDENTIFY

### Objective

Understand what happened and determine the scope and impact.

### Determine

- What happened?
- When did it happen?
- How was it discovered?
- Which systems are affected?
- Which users are affected?
- Is business data involved?
- Is personal data involved?

### Outputs

- Incident category
- Initial severity level
- Initial privacy impact rating
- Escalation recommendation

---

## PROTECT

### Objective

Prevent additional damage and reduce organizational risk.

### Examples

- Enable Multi-Factor Authentication (MFA)
- Restrict privileged access
- Encrypt devices
- Apply security updates
- Improve access controls

### Outputs

- Implemented security safeguards
- Additional protection measures

---

## DETECT

### Objective

Identify indicators of compromise or suspicious activity.

### Detection Sources

- User reports
- Security software alerts
- Audit logs
- Microsoft 365 alerts
- Network monitoring
- Endpoint monitoring

### Examples

- Failed login attempts
- Suspicious account activity
- Malware detection
- Unusual file access
- Unexpected data transfers

### Outputs

- Detection evidence
- Investigation triggers

---

## RESPOND

### Objective

Contain and manage the incident.

### Activities

- Disable compromised accounts
- Isolate systems
- Preserve evidence
- Investigate root cause
- Coordinate stakeholders

### Outputs

- Contained incident
- Investigation findings
- Documented actions

---

## RECOVER

### Objective

Restore business operations and improve resilience.

### Activities

- Restore backups
- Rebuild systems
- Recover data
- Restore services
- Validate system security

### Outputs

- Business services restored
- Improvement actions identified

---

# INCIDENT CATEGORIES

---

## Category 1: Phishing

### Description

Attempts to deceive users into revealing credentials, transferring funds, sharing information, or installing malware.

### Examples

- Fake Microsoft 365 login pages
- Fake invoices
- CEO fraud
- Supplier impersonation
- Credential harvesting

### Typical Severity

Low to Critical

### Associated Playbook

- phishing.md

---

## Category 2: Unauthorized Access

### Description

An individual gains access to systems, applications, accounts, or information without authorization.

### Examples

- Unknown account login
- Privilege escalation
- Shared credential misuse
- Former employee access

### Typical Severity

Medium to Critical

### Associated Playbook

- unauthorized-access.md

---

## Category 3: Data Breach

### Description

Information is accessed, disclosed, altered, lost, destroyed, or stolen without authorization.

### Examples

- Exposed database
- Cloud storage misconfiguration
- Unauthorized file access
- Accidental disclosure

### Typical Severity

High to Critical

### Associated Playbook

- data-breach.md

---

## Category 4: Ransomware

### Description

Malware encrypts, disrupts, locks, or steals information while demanding payment.

### Examples

- Encrypted files
- Ransom notes
- Locked devices
- Data exfiltration

### Typical Severity

Critical

### Associated Playbook

- ransomware.md

---

## Category 5: Lost or Stolen Device

### Description

A device used for business purposes cannot be located or is believed to have been stolen.

### Examples

- Laptop
- Smartphone
- Tablet
- USB storage device

### Typical Severity

Medium to High

### Associated Playbook

- lost-device.md

---

# BUSINESS IMPACT CLASSIFICATION

## Severity 1: Low

### Characteristics

- Minimal impact
- No sensitive information involved
- Quickly contained
- Single user affected

### Examples

- Phishing email reported before interaction
- Suspicious login blocked

### Response Priority

Normal

### Target Response

Within 1 business day

---

## Severity 2: Medium

### Characteristics

- Limited business disruption
- Potential credential exposure
- Small number of users affected

### Examples

- Link clicked without compromise
- Lost encrypted device

### Response Priority

High

### Target Response

Same business day

---

## Severity 3: High

### Characteristics

- Sensitive information involved
- Significant operational impact
- Multiple users or systems affected

### Examples

- Customer information exposed
- Account compromise confirmed

### Response Priority

Very High

### Target Response

Immediate

---

## Severity 4: Critical

### Characteristics

- Major business disruption
- Widespread compromise
- Significant privacy risks
- Critical systems affected

### Examples

- Ransomware outbreak
- Administrator compromise
- Large-scale data breach

### Response Priority

Emergency

### Target Response

Immediate

---

# BELIZE DATA PROTECTION IMPACT ASSESSMENT

## Purpose

Every incident should be assessed not only for cybersecurity impact but also for privacy impact.

Organizations should determine whether the incident may involve a personal data breach under the Belize Data Protection Act, 2021. The Act includes provisions relating to security of processing, records of processing activities, notification of personal data breaches, and communication of certain breaches to affected individuals. 【1-ef3315】【2-d8ceb6】

---

## Personal Data Categories

### Customer Information

- Names
- Addresses
- Telephone numbers
- Email addresses
- Account information

### Employee Information

- Personnel records
- Payroll data
- Contact details
- Employment records

### Financial Information

- Payment records
- Banking information
- Billing information

### Sensitive Personal Data

Examples include:

- Health information
- Biometric data
- Religious beliefs
- Political opinions
- Trade union membership

Sensitive personal data should be treated as elevated risk. 【2-d8ceb6】

---

# PRIVACY IMPACT CLASSIFICATION

## Privacy Impact: Low

- No personal data involved
- No unauthorized disclosure

## Privacy Impact: Medium

- Limited personal data exposure possible
- No evidence of misuse

## Privacy Impact: High

- Personal data accessed or exposed
- Customer or employee information involved

## Privacy Impact: Critical

- Large-scale personal data exposure
- Sensitive personal data involved
- Significant risk to affected individuals

---

# MANDATORY PRIVACY REVIEW TRIGGERS

Perform a privacy assessment whenever:

- Customer information is involved.
- Employee information is involved.
- Sensitive personal data is involved.
- A data breach 
