"""
Unit Tests for Security Framework
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from security.security_framework import (
    Encryption, Authentication, RateLimiter, SecurityFramework
)


class TestEncryption(unittest.TestCase):
    """Test cases for Encryption"""
    
    def test_hash_password(self):
        """Test password hashing"""
        password = "secure_password123"
        result = Encryption.hash_password(password)
        
        self.assertIn("hash", result)
        self.assertIn("salt", result)
        self.assertIsNotNone(result["hash"])
        self.assertIsNotNone(result["salt"])
    
    def test_verify_password(self):
        """Test password verification"""
        password = "secure_password123"
        hashed = Encryption.hash_password(password)
        
        # Correct password
        self.assertTrue(
            Encryption.verify_password(password, hashed["hash"], hashed["salt"])
        )
        
        # Incorrect password
        self.assertFalse(
            Encryption.verify_password("wrong_password", hashed["hash"], hashed["salt"])
        )
    
    def test_encrypt_decrypt_data(self):
        """Test data encryption and decryption"""
        data = "sensitive information"
        encrypted = Encryption.encrypt_data(data)
        
        self.assertIn("encrypted", encrypted)
        self.assertIn("key", encrypted)
        
        # Decrypt
        decrypted = Encryption.decrypt_data(encrypted["encrypted"], encrypted["key"])
        self.assertEqual(decrypted, data)


class TestAuthentication(unittest.TestCase):
    """Test cases for Authentication"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.auth = Authentication()
        self.auth.initialize()
    
    def test_user_registration(self):
        """Test user registration"""
        result = self.auth.register_user(
            "testuser", "password123", "test@example.com", "user"
        )
        
        self.assertTrue(result)
        self.assertIn("testuser", self.auth.users)
        
        # Try to register same user again
        result = self.auth.register_user(
            "testuser", "password123", "test@example.com", "user"
        )
        self.assertFalse(result)
    
    def test_authentication(self):
        """Test user authentication"""
        self.auth.register_user("testuser", "password123", "test@example.com")
        
        # Correct credentials
        token = self.auth.authenticate("testuser", "password123")
        self.assertIsNotNone(token)
        
        # Incorrect credentials
        token = self.auth.authenticate("testuser", "wrong_password")
        self.assertIsNone(token)
    
    def test_token_verification(self):
        """Test JWT token verification"""
        self.auth.register_user("testuser", "password123", "test@example.com")
        token = self.auth.authenticate("testuser", "password123")
        
        payload = self.auth.verify_token(token)
        self.assertIsNotNone(payload)
        self.assertEqual(payload["username"], "testuser")
    
    def test_account_lockout(self):
        """Test account lockout after failed attempts"""
        self.auth.register_user("testuser", "password123", "test@example.com")
        
        # Make multiple failed attempts
        for _ in range(self.auth.max_attempts):
            self.auth.authenticate("testuser", "wrong_password")
        
        # Account should be locked
        self.assertTrue(self.auth._is_account_locked("testuser"))
        
        # Even correct password should fail
        token = self.auth.authenticate("testuser", "password123")
        self.assertIsNone(token)
    
    def test_change_password(self):
        """Test password change"""
        self.auth.register_user("testuser", "old_password", "test@example.com")
        
        result = self.auth.change_password("testuser", "old_password", "new_password")
        self.assertTrue(result)
        
        # Should be able to login with new password
        token = self.auth.authenticate("testuser", "new_password")
        self.assertIsNotNone(token)
        
        # Old password should not work
        token = self.auth.authenticate("testuser", "old_password")
        self.assertIsNone(token)


class TestRateLimiter(unittest.TestCase):
    """Test cases for RateLimiter"""
    
    def test_rate_limiting(self):
        """Test rate limiting"""
        limiter = RateLimiter(max_requests=3, window_seconds=60)
        
        # First 3 requests should be allowed
        self.assertTrue(limiter.is_allowed("user1"))
        self.assertTrue(limiter.is_allowed("user1"))
        self.assertTrue(limiter.is_allowed("user1"))
        
        # 4th request should be blocked
        self.assertFalse(limiter.is_allowed("user1"))
    
    def test_remaining_requests(self):
        """Test getting remaining requests"""
        limiter = RateLimiter(max_requests=5, window_seconds=60)
        
        self.assertEqual(limiter.get_remaining_requests("user1"), 5)
        
        limiter.is_allowed("user1")
        self.assertEqual(limiter.get_remaining_requests("user1"), 4)


class TestSecurityFramework(unittest.TestCase):
    """Test cases for SecurityFramework"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.security = SecurityFramework()
        self.security.initialize()
    
    def test_security_event_logging(self):
        """Test security event logging"""
        self.security.log_security_event("login_attempt", {"username": "testuser"})
        
        self.assertEqual(len(self.security.audit_log), 1)
        self.assertEqual(self.security.audit_log[0]["event_type"], "login_attempt")
    
    def test_security_report(self):
        """Test security report generation"""
        report = self.security.get_security_report()
        
        self.assertIn("total_users", report)
        self.assertIn("active_sessions", report)
        self.assertIn("audit_events", report)


if __name__ == '__main__':
    unittest.main()
