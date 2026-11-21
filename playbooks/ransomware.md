# Ransomware Incident Playbook

## Overview

Ransomware is a type of malware that prevents access to systems or data, typically by encrypting files and demanding payment for their recovery. Some ransomware groups also steal data before encryption and threaten to publish it if payment is not made.

Examples include:

- Files suddenly become inaccessible
- File extensions change unexpectedly
- Ransom notes appear on systems
- Users cannot log in
- Shared drives become encrypted
- Unusual network-wide outages occur

---

## Incident Objectives

1. Stop the spread of ransomware.
2. Protect unaffected systems.
3. Preserve evidence.
4. Determine the scope of infection.
5. Restore business operations safely.
6. Assess potential data exposure.
7. Document all actions taken.

---

## Warning Signs

Common indicators include:

- Files renamed or encrypted
- Ransom note displayed
- Unusual file extensions
- Disabled security tools
- Extremely slow systems
- Unknown administrator accounts
- Large numbers of failed backups
- Suspicious login activity
- Missing or deleted files

---

## Initial Assessment

Gather the following information:

| Question | Response |
|-----------|------------|
| Who discovered the incident? | |
| Date and time discovered? | |
| First affected system? | |
| Number of affected systems? | |
| Shared drives affected? | |
| Backups available? | |
| Sensitive data involved? | |
| Is the infection still spreading? | |

---

## Immediate Containment Actions

### Step 1: Isolate Affected Systems

Immediately:

- Disconnect infected devices from the network.
- Disable Wi-Fi connections.
- Disconnect VPN sessions.
- Disconnect affected servers from the network if possible.

If multiple systems are involved:

- Restrict access to shared drives.
- Temporarily disable unnecessary network connections.

---

### Step 2: Preserve Evidence

Do NOT:

- Reinstall systems immediately.
- Format drives.
- Delete ransom notes.
- Delete suspicious files.

Collect:

- Screenshots of ransom messages
- File extensions used by ransomware
- Dates and times of discovery
- System logs
- Security alerts
- User observations

Document all actions taken.

---

### Step 3: Notify Management

Immediately notify:

- Business owner
- Senior management
- IT support provider
- Incident response personnel

Provide:

- Number of affected systems
- Business impact
- Current containment status
- Immediate risks

---

## Investigation

### Identify Patient Zero

Determine:

- First affected device
- First affected user
- Initial infection source

Common sources:

- Phishing email
- Malicious attachment
- Fake software update
- Weak remote access security
- Compromised credentials

---

### Determine Scope

Identify:

#### Affected Systems

- Workstations
- Servers
- Cloud resources
- Shared drives

#### Affected Users

- Individual employees
- Departments
- External users

#### Affected Services

- Email
- Accounting systems
- CRM systems
- File storage
- Business applications

---

### Determine Potential Data Exposure

Some ransomware groups steal data before encryption.

Assess:

- Customer information
- Employee information
- Financial records
- Contracts
- Business documents
- Login credentials

Determine whether evidence suggests data was copied, exported, or transferred.

---

## Severity Classification

### High

- Single system affected
- Limited operational disruption
- No evidence of wider spread

### Critical

- Multiple systems infected
- Shared drives encrypted
- Critical business services unavailable
- Sensitive information potentially exposed
- Significant operational disruption

Most ransomware incidents should be treated as Critical until proven otherwise.

---

## Recovery Actions

### Verify Containment

Before recovery:

- Confirm ransomware is no longer spreading.
- Verify compromised accounts are secured.
- Remove unauthorized access.
- Validate security controls.

---

### Restore Systems

Restore only from trusted sources.

Possible recovery options:

- Restore from clean backups
- Rebuild affected systems
- Reinstall operating systems
- Restore business applications

Verify restored systems before reconnecting to production networks.

---

### Credential Security

Reset:

- User passwords
- Administrator passwords
- Service account credentials
- Remote access credentials

Enable Multi-Factor Authentication (MFA) wherever possible.

---

### Vulnerability Remediation

Address weaknesses that allowed infection:

- Apply security updates
- Remove unnecessary software
- Review remote access settings
- Review firewall rules

---

## Monitoring

Increase monitoring for:

- New ransomware activity
- Suspicious file modifications
- Failed login attempts
- Unusual administrator activity
- Unexpected network traffic

Monitor closely during recovery and after systems return to service.

---

## Communication

### Internal Communication

Provide updates to:

- Management
- Employees
- IT support teams

Include:

- Systems affected
- Business impact
- Actions underway
- Expected service availability

---

### External Communication Assessment

Determine whether communication may be necessary with:

- Customers
- Vendors
- Insurance providers
- Legal advisors

Document all decisions and communications.

---

## Business Continuity

If critical systems are unavailable:

Prioritize restoration of:

1. Email and communication systems
2. Financial systems
3. Customer-facing services
4. Operational applications
5. Non-essential business services

Use manual processes where necessary to maintain business operations.

---

## Lessons Learned Review

After recovery, document:

### Root Cause

Examples:

- Phishing email
- Insecure remote access
- Weak passwords
- Unpatched systems

### Control Gaps

Examples:

- Missing MFA
- Poor backup procedures
- Insufficient monitoring
- Lack of employee training

### Improvement Opportunities

- Security awareness training
- Backup testing
- Incident response exercises
- Access control improvements
- Vulnerability management

---

## Recommended Security Controls

### Preventive Controls

- Multi-Factor Authentication (MFA)
- Security awareness training
- Email filtering
- Endpoint protection
- Patch management
- Network segmentation

### Detective Controls

- Security monitoring
- Audit logging
- Endpoint detection tools
- Login monitoring

### Corrective Controls

- Backup and recovery procedures
- Incident response plan
- Business continuity plan
- Disaster recovery testing

---

## Recovery Validation Checklist

Before declaring the incident resolved:

- [ ] Ransomware activity stopped
- [ ] Affected systems identified
- [ ] Evidence preserved
- [ ] Scope determined
- [ ] Compromised accounts secured
- [ ] Systems restored
- [ ] Backups verified
- [ ] Monitoring increased
- [ ] Management informed
- [ ] Lessons learned completed
- [ ] Corrective actions assigned

---

## Belize SME Considerations

For small businesses with limited IT resources:

- Focus first on containment and recovery.
- Keep detailed written records of actions taken.
- Preserve evidence in case external assistance is required.
- Maintain offline or cloud backups whenever possible.
- Review whether customer, employee, or financial data may have been affected.
- Use the incident as an opportunity to strengthen cybersecurity awareness and resilience.
