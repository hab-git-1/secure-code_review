import unittest
from vulnerable_app import safe_login, safe_ping

class TestSecurityControls(unittest.TestCase):

    def test_sql_injection_remediation(self):
        """Verify parameterized queries use place-holders instead of raw values."""
        result = safe_login("admin' OR '1'='1", "password123")
        self.assertIn("?", result)
        self.assertNotIn("OR '1'='1'", result.split("WHERE")[1])

    def test_command_injection_remediation(self):
        """Verify command injection payloads trigger validation errors."""
        with self.assertRaises(ValueError):
            safe_ping("127.0.0.1; cat /etc/passwd")

if __name__ == "__main__":
    unittest.main()