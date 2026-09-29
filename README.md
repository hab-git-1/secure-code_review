# CodeAlpha Cybersecurity Internship - Task 3


## Secure Coding Review & Audit Report

### Overview
This project performs a static security code review to identify critical vulnerabilities based on OWASP Top 10 guidelines. It provides side-by-side analysis of common code flaws alongside defensive programming fixes.

---

### Audit Findings

| Vulnerability Class | Severity | OWASP Top 10 Category | Root Cause | Defense Mechanism |
| :--- | :--- | :--- | :--- | :--- |
| **SQL Injection** | High | A03:2021 - Injection | Dynamic string formatting in database queries | Parameterized Queries / Prepared Statements |
| **Command Injection** | Critical | A03:2021 - Injection | Passing unvalidated input to OS system shells | Regex Input Validation & Array Process Invocation |

---

### Key Takeaways
1. **Never Trust User Input:** Always validate, sanitize, and strictly type-check inputs.
2. **Separate Code from Data:** Parameterized queries prevent string context hijacking.
3. **Avoid System Shell Execution:** Avoid `os.system()` callouts in favor of isolated process execution like `subprocess.run()`.

---

### How to Run Verification
```bash
python3 vulnerable_app.py
