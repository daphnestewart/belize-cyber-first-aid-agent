# Phishing Incident Playbook

## Overview

A phishing incident occurs when an attacker attempts to deceive users into revealing sensitive information, transferring funds, approving fraudulent requests, or downloading malicious software.

Phishing may be delivered through:

- Email
- SMS messages (Smishing)
- Phone calls (Vishing)
- Social media messages
- Collaboration platforms such as Teams or Slack
- Fake websites

Common objectives include:

- Credential theft
- Business Email Compromise (BEC)
- Malware installation
- Financial fraud
- Data theft

---

## Incident Objectives

1. Stop the attack from spreading.
2. Secure affected accounts and systems.
3. Preserve evidence.
4. Determine whether credentials or data were compromised.
5. Recover affected systems.
6. Reduce future phishing risk.

---

## Initial Assessment

Gather the following information:

| Question | Response |
|-----------|------------|
| Who reported the incident? | |
| Date and time reported? | |
| Was the email opened? | |
| Was a link clicked? | |
| Was an attachment opened? | |
| Were credentials entered? | |
| Was money transferred? | |
| Are multiple users affected? | |

---

## Identify the Type of Phishing

### Credential Harvesting

Examples:

- Fake Microsoft 365 login page
- Fake banking portal
- Fake payroll portal

### Malware Delivery

Examples:

- Malicious attachment
- Fake invoice
- Fake shipping document

### Business Email Compromise (BEC)

Examples:

- CEO fraud
- Fake supplier request
- Urgent wire transfer request

### Data Collection

Examples:

- Request for employee information
- Request for customer records
- Request for financial data

---

## Immediate Containment Actions

### Scenario 1: Suspicious Email Received But Not Opened

1. Do not interact with the email.
2. Report the email internally.
3. Move the email to quarantine or junk.
4. Preserve a copy for investigation.
5. Check whether other employees received the same message.

---

### Scenario 2: User Opened Email Only

1. Preserve the email.
2. Review sender information.
3. Scan attachments if applicable.
4. Monitor for additional suspicious activity.

---

### Scenario 3: User Clicked a Link

1. Disconnect the device from the network if suspicious activity occurs.
2. Identify the website visited.
3. Review browser history.
4. Determine whether credentials were entered.
5. Collect screenshots if possible.

---

### Scenario 4: User Entered Credentials

Immediate actions:

- Change passwords immediately.
- Revoke active sessions.
- Enable Multi-Factor Authentication (MFA).
- Review recent sign-in activity.
- Monitor for unauthorized access.
- Check for mailbox rule changes.

Microsoft 365 checks:

- Unknown logins
- Foreign login locations
- Suspicious MFA requests
- Email forwarding rules
- Newly created inbox rules

---

### Scenario 5: Attachment Opened

1. Disconnect affected device from the network.
2. Leave the device powered on.
3. Do not delete files.
4. Preserve suspicious files.
5. Run approved malware detection tools.
6. Escalate immediately if ransomware or malware is suspected.

---

## Evidence Collection

Preserve:

### Email Information

- Sender address
- Subject line
- Email headers
- Message content

### Screenshots

- Phishing email
- Login pages
- Error messages
- Security alerts

### System Information

- Device name
- User account
- Browser history
- Security logs

### Timeline

Record:

- Email received
- Email opened
- Link clicked
- Credentials entered
- Incident reported

---

## Investigation

### Determine Scope

Identify:

- Number of affected users
- Number of affected systems
- Business functions impacted
- Potentially exposed accounts

---

### Review Account Activity

Look for:

- Failed logins
- Unusual locations
- New devices
- Password changes
- MFA changes

---

### Check Email Security

Look for:

- Automatic forwarding rules
- Suspicious inbox rules
- Deleted emails
- Email sent from compromised accounts

---

### Assess Data Exposure

Determine whether the attacker may have accessed:

- Customer information
- Employee records
- Financial information
- Internal documents
- Shared drives

---

## Severity Classification

### Low

- Phishing email reported before interaction
- No links clicked
- No attachment opened

### Medium

- Link clicked
- No credentials entered
- No malware detected

### High

- Credentials entered
- Email account compromised
- Multiple users affected

### Critical

- Administrator account compromised
- Malware installed
- Customer data exposed
- Financial fraud occurred
- Business operations disrupted

---

## Recovery Actions

### Account Recovery

- Reset passwords
- Enable MFA
- Remove unauthorized access
- Review permissions

### Email Recovery

- Remove phishing emails from mailboxes
- Remove unauthorized forwarding rules
- Verify mailbox integrity

### System Recovery

- Scan affected systems
- Remove malware
- Restore systems if required
- Apply missing security updates

---

## Communication

Notify:

- Management
- IT support provider
- Business owner
- Affected departments

Document:

- What occurred
- Number of users affected
- Actions taken
- Current risk level

---

## Lessons Learned

Review:

### Human Factors

- Was the email convincing?
- Were employees trained to identify phishing?

### Technical Controls

- Was MFA enabled?
- Was email filtering sufficient?
- Were security alerts generated?

### Process Improvements

- Improve reporting procedures
- Conduct awareness training
- Update incident response procedures

---

## Recommended Security Controls

### Preventive Controls

- Multi-Factor Authentication (MFA)
- Security awareness training
- Email filtering
- Strong password policy
- Device protection

### Detective Controls

- Login monitoring
- Security alerts
- Mailbox auditing
- Endpoint detection monitoring

### Corrective Controls

- Incident response plan
- Backup procedures
- Access reviews
- User awareness programs

---

## Playbook Completion Checklist

- [ ] Incident reported
- [ ] Email preserved
- [ ] Evidence collected
- [ ] Affected users identified
- [ ] Credentials secured
- [ ] Systems reviewed
- [ ] Malware assessment completed
- [ ] Management notified
- [ ] Recovery completed
- [ ] Lessons learned documented
- [ ] Follow-up training scheduled
