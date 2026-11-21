# Unauthorized Access Incident Playbook

## Description

An unauthorized access incident occurs when an individual gains access to a system, application, account, or resource without proper authorization.

Examples include:

- Unknown account login
- Compromised credentials
- Shared account misuse
- Suspicious administrator activity
- Unauthorized access to files or databases

## Immediate Actions

1. Identify affected accounts and systems.
2. Disable or lock compromised accounts.
3. Reset passwords immediately.
4. Enable or enforce Multi-Factor Authentication (MFA).
5. Terminate suspicious active sessions.
6. Preserve logs and audit records.
7. Notify management and relevant stakeholders.

## Evidence Collection

- Login timestamps
- User account information
- Source IP addresses
- Authentication logs
- Screenshots of suspicious activity
- System audit records

## Severity Assessment

### Medium

- Single user account affected
- No evidence of data access

### High

- Sensitive information accessed
- Multiple accounts affected

### Critical

- Administrative or privileged account compromised
- Significant business impact
- Evidence of data theft or destruction

## Recovery

1. Verify compromised accounts are secured.
2. Review recent account activity.
3. Remove unauthorized access permissions.
4. Update security controls.
5. Monitor systems for recurring activity.

## Lessons Learned

- Enforce strong password policies.
- Require Multi-Factor Authentication (MFA).
- Conduct regular access reviews.
- Implement account monitoring and alerting.
- Follow the principle of least privilege.
