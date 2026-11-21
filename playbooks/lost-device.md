# Lost Device Incident Playbook

## Overview

A lost device incident occurs when a business-owned or business-used device cannot be located or is suspected to have been stolen.

Examples:

- Lost laptop
- Stolen mobile phone
- Missing USB drive
- Missing tablet
- Missing external hard drive

---

## Incident Objectives

1. Protect business information.
2. Prevent unauthorized access.
3. Preserve evidence.
4. Determine potential impact.
5. Restore business operations.

---

## Initial Assessment

Document:

| Information | Value |
|-------------|---------|
| Device Type | |
| Owner/User | |
| Serial Number | |
| Last Known Location | |
| Date Lost | |
| Date Reported | |

---

## Immediate Actions

### Step 1: Confirm Loss

Verify:

- Device is not misplaced on-site.
- Device is not with another employee.
- Device is not currently checked out.

---

### Step 2: Report Incident

Notify:

- Business owner
- IT administrator
- Security manager (if applicable)

Record:

- When loss was discovered
- Who reported it
- Circumstances

---

### Step 3: Secure Accounts

Immediately:

- Change password
- Revoke active sessions
- Reset business application access
- Enable MFA

Accounts to review:

- Microsoft 365
- Email
- Banking systems
- CRM systems
- Accounting software

---

### Step 4: Remote Protection

If supported:

- Lock device remotely
- Locate device remotely
- Wipe device remotely

Document actions taken.

---

## Exposure Assessment

Determine:

### Was Device Encrypted?

Yes / No

### Was MFA Enabled?

Yes / No

### Did Device Contain:

- Customer data
- Employee records
- Financial information
- Contracts
- Passwords

---

## Investigation

Review:

- Login records
- Cloud access logs
- Email activity
- VPN activity

Look for:

- Access after loss occurred
- New locations
- Suspicious sign-ins

---

## Severity Classification

### Low

- Device encrypted
- No sensitive information saved

### Medium

- Email access available
- Business applications installed

### High

- Sensitive business information stored locally
- Financial systems accessible

### Critical

- Device belonged to administrator
- Highly sensitive data present
- Active unauthorized usage detected

---

## Recovery Actions

### Replace Device

- Issue replacement hardware
- Reinstall approved software
- Apply security settings

### Restore Data

- Restore from backup
- Validate integrity

### Strengthen Protections

- Enable encryption
- Require MFA
- Maintain device inventory

---

## Communication

Provide management with:

- Incident summary
- Potential impact
- Actions taken
- Current status
- Recommendations

---

## Lessons Learned

Review:

- Asset management process
- Device inventory records
- Backup procedures
- Remote wipe capability
- User awareness training

Recommended Controls:

- Microsoft Intune
- Device encryption
- MFA
- Endpoint protection
- Asset tracking
