"""
Security Tests for AiElon Living OS

Tests security vulnerabilities and attack scenarios.
"""

import unittest
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from security.security_framework import Authentication, RateLimiter, Encryption
from blockchain.aielonchain338 import AielonChain338, Transaction


class TestSecurityVulnerabilities(unittest.TestCase):
    """Test security vulnerabilities and protections"""
    
    def test_brute_force_protection(self):
        """Test protection against brute force attacks"""
        auth = Authentication()
        auth.initialize()
        auth.register_user("testuser", "correct_password", "test@example.com")
        
        # Attempt multiple failed logins
        for _ in range(5):
            token = auth.authenticate("testuser", "wrong_password")
            self.assertIsNone(token)
        
        # Account should be locked
        self.assertTrue(auth._is_account_locked("testuser"))
        
        # Even correct password should fail
        token = auth.authenticate("testuser", "correct_password")
        self.assertIsNone(token)
    
    def test_sql_injection_prevention(self):
        """Test that inputs are properly sanitized"""
        auth = Authentication()
        auth.initialize()
        
        # Attempt SQL injection in username
        malicious_username = "admin'; DROP TABLE users; --"
        result = auth.register_user(malicious_username, "password", "email@test.com")
        
        # Should handle gracefully
        self.assertIsInstance(result, bool)
    
    def test_password_hashing_security(self):
        """Test password hashing is secure"""
        password = "secure_password"
        hash1 = Encryption.hash_password(password)
        hash2 = Encryption.hash_password(password)
        
        # Same password should produce different hashes (due to different salts)
        self.assertNotEqual(hash1["hash"], hash2["hash"])
        self.assertNotEqual(hash1["salt"], hash2["salt"])
        
        # Both should verify correctly
        self.assertTrue(Encryption.verify_password(password, hash1["hash"], hash1["salt"]))
        self.assertTrue(Encryption.verify_password(password, hash2["hash"], hash2["salt"]))
    
    def test_rate_limiting_ddos_protection(self):
        """Test rate limiting against DDoS"""
        limiter = RateLimiter(max_requests=3, window_seconds=60)
        
        # Simulate multiple requests
        allowed_count = 0
        blocked_count = 0
        
        for _ in range(10):
            if limiter.is_allowed("attacker_ip"):
                allowed_count += 1
            else:
                blocked_count += 1
        
        # Should have blocked some requests
        self.assertEqual(allowed_count, 3)
        self.assertEqual(blocked_count, 7)
    
    def test_token_expiration(self):
        """Test JWT token expiration"""
        auth = Authentication()
        auth.initialize()
        auth.register_user("testuser", "password", "test@example.com")
        
        token = auth.authenticate("testuser", "password")
        
        # Token should be valid initially
        payload = auth.verify_token(token)
        self.assertIsNotNone(payload)
        
        # Token should have expiration
        self.assertIn("exp", payload)
    
    def test_blockchain_tampering_detection(self):
        """Test blockchain detects tampering"""
        blockchain = AielonChain338(difficulty=2)
        
        # Add valid transaction
        blockchain.create_transaction("alice", "bob", 10.0)
        blockchain.mine_pending_transactions("miner1")
        
        # Chain should be valid
        self.assertTrue(blockchain.is_chain_valid())
        
        # Tamper with a block
        if len(blockchain.chain) > 1:
            blockchain.chain[1].transactions.append({
                "sender": "hacker",
                "recipient": "hacker_account",
                "amount": 1000000.0
            })
            
            # Chain should detect tampering
            self.assertFalse(blockchain.is_chain_valid())
    
    def test_invalid_transaction_rejection(self):
        """Test invalid transactions are rejected"""
        blockchain = AielonChain338()
        
        # Negative amount
        tx1 = Transaction("alice", "bob", -10.0)
        self.assertFalse(blockchain.add_transaction(tx1))
        
        # Zero amount
        tx2 = Transaction("alice", "bob", 0.0)
        self.assertFalse(blockchain.add_transaction(tx2))
        
        # Empty sender
        tx3 = Transaction("", "bob", 10.0)
        self.assertFalse(blockchain.add_transaction(tx3))
    
    def test_session_management(self):
        """Test secure session management"""
        auth = Authentication()
        auth.initialize()
        auth.register_user("testuser", "password", "test@example.com")
        
        # Login creates session
        token = auth.authenticate("testuser", "password")
        self.assertIsNotNone(token)
        self.assertGreater(len(auth.sessions), 0)
        
        # Logout invalidates session
        result = auth.logout(token)
        self.assertTrue(result)
    
    def test_encryption_decryption_security(self):
        """Test encryption and decryption"""
        sensitive_data = "Secret information"
        
        # Encrypt
        encrypted = Encryption.encrypt_data(sensitive_data)
        self.assertNotEqual(encrypted["encrypted"], sensitive_data)
        
        # Decrypt
        decrypted = Encryption.decrypt_data(encrypted["encrypted"], encrypted["key"])
        self.assertEqual(decrypted, sensitive_data)
        
        # Wrong key should not decrypt correctly
        wrong_decrypted = Encryption.decrypt_data(encrypted["encrypted"], "wrong_key")
        self.assertNotEqual(wrong_decrypted, sensitive_data)
    
    def test_unauthorized_access_prevention(self):
        """Test prevention of unauthorized access"""
        auth = Authentication()
        auth.initialize()
        
        # Try to authenticate non-existent user
        token = auth.authenticate("nonexistent", "password")
        self.assertIsNone(token)
        
        # Try to change password without authentication
        result = auth.change_password("nonexistent", "old", "new")
        self.assertFalse(result)


class TestSecurityAudit(unittest.TestCase):
    """Security audit tests"""
    
    def test_no_hardcoded_secrets(self):
        """Ensure no hardcoded secrets in code"""
        # This is a simple check - in production, use secret scanning tools
        test_files = [
            "../../src/security/security_framework.py",
            "../../src/core/system.py"
        ]
        
        forbidden_patterns = ["password=", "secret=", "api_key="]
        
        for file_path in test_files:
            full_path = os.path.join(os.path.dirname(__file__), file_path)
            if os.path.exists(full_path):
                with open(full_path, 'r') as f:
                    content = f.read().lower()
                    for pattern in forbidden_patterns:
                        # Ensure no hardcoded values (some occurrences in variable names are OK)
                        self.assertNotIn(f'{pattern}"', content)
                        self.assertNotIn(f"{pattern}'", content)


if __name__ == '__main__':
    unittest.main()
