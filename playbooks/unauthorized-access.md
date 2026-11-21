# Unauthorized Access Incident Playbook

## Overview

An unauthorized access incident occurs when an individual gains access to a system, account, application, network resource, or data without proper authorization.

Examples:

- Unknown Microsoft 365 login
- Suspicious VPN connection
- Unauthorized password changes
- New administrator account creation
- Unexpected file access
- Former employee account still active

---

## Incident Objectives

1. Stop unauthorized activity.
2. Prevent additional access.
3. Preserve evidence.
4. Determine what was accessed.
5. Restore secure operations.
6. Document all actions.

---

## Initial Assessment

Gather the following information:

| Question | Response |
|-----------|------------|
| Who discovered the incident? | |
| Date and time discovered? | |
| Affected account(s)? | |
| Affected systems? | |
| Sensitive data involved? | |
| Is access ongoing? | |
| Is business operation affected? | |

---

## Immediate Containment Actions

### Step 1: Secure Affected Accounts

- Disable compromised accounts.
- Force password reset.
- Enable MFA if not already enabled.
- Revoke active sessions.

Microsoft 365:

- Sign out user from all sessions.
- Review recent sign-ins.
- Review mailbox rules.

---

### Step 2: Isolate Affected Systems

If malware or remote access is suspected:

- Disconnect system from network.
- Leave the device powered on.
- Do not delete files.
- Do not reformat the device.

---

### Step 3: Preserve Evidence

Collect:

- Screenshots
- Login records
- Security alerts
- Email notifications
- User statements
- File access logs

Record all times in local Belize time.

---

## Investigation

### Determine:

#### How Access Occurred

Possible causes:

- Weak password
- Password reuse
- Phishing
- Shared credentials
- Misconfigured permissions

#### What Was Accessed

Review:

- Email inboxes
- Shared drives
- Financial records
- Customer databases
- Cloud services

#### What Was Changed

Identify:

- Password changes
- New accounts
- New forwarding rules
- Deleted files
- Modified permissions

---

## Severity Classification

### Medium

- Single user account compromised
- No sensitive information accessed

### High

- Multiple accounts affected
- Confidential data accessed
- Financial systems involved

### Critical

- Administrator account compromised
- Customer data exposed
- Major operational disruption

---

## Recovery Actions

### Account Security

- Reset passwords
- Enable MFA
- Remove unauthorized accounts
- Remove unauthorized permissions

### System Validation

- Perform malware scan
- Review installed software
- Review security logs

### Monitoring

Monitor for at least:

- Failed logins
- New administrator accounts
- Unusual file access
- Unusual email activity

---

## Communication

Notify:

- Management
- IT Support Provider
- Business Owner

If personal information may have been exposed:

- Assess reporting obligations.
- Document all decisions.

---

## Lessons Learned

Identify:

- Why access was possible
- Missing controls
- Training opportunities
- Required security improvements

Examples:

- MFA was not enabled.
- Password policy was weak.
- Excessive permissions existed.
