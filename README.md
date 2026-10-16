## Secure Coding Review & Static Application Security Testing (SAST) Audit Report

## Executive Summary
This repository presents a comprehensive security code review and static application security testing (SAST) demonstration targeting critical web and system vulnerability classes defined in the **OWASP Top 10 (A03:2021 – Injection)**. The project showcases vulnerable implementation patterns alongside defensive programming remediation strategies, complete with automated unit tests and SAST scan results using **Bandit**.



## Technical Audit Findings

### 1. SQL Injection (OWASP A03:2021)
* **Vulnerability Type:** CWE-89 (Improper Neutralization of Special Elements used in an SQL Command)
* **Risk Severity:** High
* **Root Cause:** Direct string interpolation (`f"..."`) inside database query construction, allowing arbitrary SQL logic execution via user input.
* **Vulnerable Code Pattern:**
  query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
* **Remediation Strategy:** Parameterized queries / prepared statements using placeholders (`?`), ensuring strict separation between execution instructions and user data.
* **Remediated Code Pattern:**
  query = "SELECT * FROM users WHERE username = ? AND password = ?"
  cursor.execute(query, (username, password))



### 2. Command Injection (OWASP A03:2021)
* **Vulnerability Type:** CWE-78 (Improper Neutralization of Special Elements used in an OS Command)
* **Risk Severity:** Critical
* **Root Cause:** Passing unvalidated user input directly to system command shells, enabling arbitrary command chaining (`|`, `;`, `&`).
* **Vulnerable Code Pattern:**
  command = "ping -c 1 " + hostname
  os.system(command)
* **Remediation Strategy:** Strict regex validation (`^[a-zA-Z0-9.-]+$`) and bypassing system shells by passing command arguments as explicit arrays via `subprocess.run()`.
* **Remediated Code Pattern:**
  if not re.match(r"^[a-zA-Z0-9.-]+$", hostname):
      raise ValueError("Invalid target format")
  subprocess.run(["ping", "-c", "1", hostname], check=True)



## Static Application Security Testing (SAST)

Automated code analysis was performed using **Bandit**, a Python security linter.

### Running the SAST Scan
bandit -r vulnerable_app.py

### Key SAST Findings
[main] INFO scanned Python files: 1

>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string formatting
   Severity: Medium   Confidence: Low
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   Location: ./vulnerable_app.py:18:14
   17        # DANGEROUS: String formatting in SQL query
   18        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
   19        print(f"[UNSAFE QUERY Executed]: {query}")

Code scanned:
    Total lines of code: 49
    Total lines skipped (#nosec): 0

Run metrics:
    Total issues (by severity):
        Low: 1
        Medium: 1
        High: 0



## Dynamic Testing & Verification

### 1. Core Script Execution
Run the application script to view dynamic injection payloads and remediation output:
python3 vulnerable_app.py

### 2. Automated Security Unit Tests
Execute the security control test suite to verify defense mechanics:
python3 test_security.py



## Repository Structure

secure-code_review/
│
├── vulnerable_app.py       # Vulnerable vs. safe implementation logic
├── test_security.py        # Automated unit tests for security controls
├── README.md               # Executive security audit report & documentation
└── .gitignore              # Git environment exclusion rules
