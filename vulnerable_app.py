import sqlite3
import subprocess
import re

# =====================================================================
# VULNERABLE CODE DEMONSTRATION (DO NOT USE IN PRODUCTION)
# =====================================================================

def unsafe_login(username, password):
    """
    Vulnerability: SQL Injection (OWASP A03:2021)
    Root Cause: Direct string concatenation allows input manipulation.
    """
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # DANGEROUS: String formatting in SQL query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"[UNSAFE QUERY Executed]: {query}")
    return query

def unsafe_ping(hostname):
    """
    Vulnerability: Command Injection (OWASP A03:2021)
    Root Cause: Unsanitized user input passed directly to system shell.
    """
    import os
    # DANGEROUS: Shell command concatenation
    command = "ping -c 1 " + hostname
    print(f"[UNSAFE COMMAND Executed]: {command}")


# =====================================================================
# SECURE / REMEDIATED CODE DEMONSTRATION
# =====================================================================

def safe_login(username, password):
    """
    Security Control: Parameterized Query / Prepared Statement
    Enforces strict separation between code execution and user data.
    """
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # SAFE: Placeholders prevents SQL syntax injection
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f"[SAFE QUERY Executed]: {query} with parameters ({username}, {password})")
    return query

def safe_ping(hostname):
    """
    Security Control: Strict Input Validation & Avoiding Shell Invocation
    Disallows special characters (`;`, `&`, `|`) and bypasses shell execution.
    """
    # Reject anything that isn't a plain hostname or IP address
    if not re.match(r"^[a-zA-Z0-9.-]+$", hostname):
        raise ValueError("Security Alert: Invalid target format detected!")

    # SAFE: Array execution without shell=True
    print(f"[SAFE COMMAND Executed]: ping -c 1 {hostname}")


if __name__ == "__main__":
    print("--- 1. Testing SQL Injection Vulnerability ---")
    unsafe_login("admin' OR '1'='1", "password123")
    safe_login("admin' OR '1'='1", "password123")

    print("\n--- 2. Testing Command Injection Vulnerability ---")
    unsafe_ping("127.0.0.1; cat /etc/passwd")
    try:
        safe_ping("127.0.0.1; cat /etc/passwd")
    except ValueError as e:
        print(f"[REMEDIATED]: Blocked attack - {e}")