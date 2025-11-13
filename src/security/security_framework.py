"""
AiElon Living OS - Security Framework

This module provides comprehensive security features:
- Authentication and authorization
- Encryption utilities
- Rate limiting and DDoS protection
- Security auditing and logging
"""

import hashlib
import secrets
import time
import jwt
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta


class Encryption:
    """Encryption utilities for secure data handling"""
    
    @staticmethod
    def hash_password(password: str, salt: str = None) -> Dict[str, str]:
        """
        Hash a password with salt
        
        Args:
            password: Password to hash
            salt: Salt value (generated if not provided)
            
        Returns:
            dict: Hash and salt
        """
        if salt is None:
            salt = secrets.token_hex(32)
        
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000
        )
        
        return {
            "hash": password_hash.hex(),
            "salt": salt
        }
    
    @staticmethod
    def verify_password(password: str, password_hash: str, salt: str) -> bool:
        """
        Verify a password against a hash
        
        Args:
            password: Password to verify
            password_hash: Stored password hash
            salt: Salt used for hashing
            
        Returns:
            bool: True if password matches
        """
        new_hash = Encryption.hash_password(password, salt)
        return new_hash["hash"] == password_hash
    
    @staticmethod
    def encrypt_data(data: str, key: str = None) -> Dict[str, str]:
        """
        Encrypt data (simplified implementation)
        
        Args:
            data: Data to encrypt
            key: Encryption key
            
        Returns:
            dict: Encrypted data and key
        """
        if key is None:
            key = secrets.token_hex(32)
        
        # Simple XOR encryption for demonstration
        encrypted = ''.join(
            chr(ord(c) ^ ord(key[i % len(key)])) 
            for i, c in enumerate(data)
        )
        
        return {
            "encrypted": encrypted.encode('utf-8').hex(),
            "key": key
        }
    
    @staticmethod
    def decrypt_data(encrypted_data: str, key: str) -> str:
        """
        Decrypt data
        
        Args:
            encrypted_data: Encrypted data (hex string)
            key: Encryption key
            
        Returns:
            str: Decrypted data
        """
        encrypted_bytes = bytes.fromhex(encrypted_data)
        encrypted = encrypted_bytes.decode('utf-8')
        
        decrypted = ''.join(
            chr(ord(c) ^ ord(key[i % len(key)])) 
            for i, c in enumerate(encrypted)
        )
        
        return decrypted


class Authentication:
    """Authentication system for user management"""
    
    def __init__(self, secret_key: str = None):
        """
        Initialize authentication system
        
        Args:
            secret_key: Secret key for JWT tokens
        """
        self.secret_key = secret_key or secrets.token_hex(32)
        self.users: Dict[str, Dict[str, Any]] = {}
        self.sessions: Dict[str, Dict[str, Any]] = {}
        self.failed_attempts: Dict[str, List[float]] = {}
        self.max_attempts = 5
        self.lockout_duration = 300  # 5 minutes
    
    def initialize(self) -> None:
        """Initialize authentication system"""
        self.users.clear()
        self.sessions.clear()
        self.failed_attempts.clear()
    
    def register_user(self, username: str, password: str, 
                      email: str, role: str = "user") -> bool:
        """
        Register a new user
        
        Args:
            username: Username
            password: Password
            email: Email address
            role: User role
            
        Returns:
            bool: True if registration successful
        """
        if username in self.users:
            return False
        
        # Hash password
        password_data = Encryption.hash_password(password)
        
        self.users[username] = {
            "username": username,
            "password_hash": password_data["hash"],
            "password_salt": password_data["salt"],
            "email": email,
            "role": role,
            "created_at": datetime.now().isoformat(),
            "last_login": None,
            "is_active": True,
            "two_factor_enabled": False
        }
        
        return True
    
    def authenticate(self, username: str, password: str) -> Optional[str]:
        """
        Authenticate a user and return JWT token
        
        Args:
            username: Username
            password: Password
            
        Returns:
            str: JWT token if successful, None otherwise
        """
        # Check if account is locked
        if self._is_account_locked(username):
            return None
        
        # Verify user exists
        if username not in self.users:
            self._record_failed_attempt(username)
            return None
        
        user = self.users[username]
        
        # Check if user is active
        if not user.get("is_active", False):
            return None
        
        # Verify password
        if not Encryption.verify_password(
            password, 
            user["password_hash"], 
            user["password_salt"]
        ):
            self._record_failed_attempt(username)
            return None
        
        # Clear failed attempts on successful login
        if username in self.failed_attempts:
            del self.failed_attempts[username]
        
        # Update last login
        user["last_login"] = datetime.now().isoformat()
        
        # Generate JWT token
        token = self._generate_token(username, user["role"])
        
        # Create session
        session_id = secrets.token_hex(16)
        self.sessions[session_id] = {
            "username": username,
            "token": token,
            "created_at": datetime.now().isoformat(),
            "expires_at": (datetime.now() + timedelta(hours=24)).isoformat()
        }
        
        return token
    
    def _generate_token(self, username: str, role: str) -> str:
        """Generate JWT token"""
        payload = {
            "username": username,
            "role": role,
            "exp": datetime.utcnow() + timedelta(hours=24),
            "iat": datetime.utcnow()
        }
        
        return jwt.encode(payload, self.secret_key, algorithm="HS256")
    
    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """
        Verify JWT token
        
        Args:
            token: JWT token
            
        Returns:
            dict: Token payload if valid, None otherwise
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
    
    def _record_failed_attempt(self, username: str) -> None:
        """Record failed login attempt"""
        if username not in self.failed_attempts:
            self.failed_attempts[username] = []
        
        self.failed_attempts[username].append(time.time())
        
        # Keep only recent attempts
        cutoff_time = time.time() - self.lockout_duration
        self.failed_attempts[username] = [
            t for t in self.failed_attempts[username] 
            if t > cutoff_time
        ]
    
    def _is_account_locked(self, username: str) -> bool:
        """Check if account is locked due to failed attempts"""
        if username not in self.failed_attempts:
            return False
        
        recent_attempts = [
            t for t in self.failed_attempts[username]
            if t > time.time() - self.lockout_duration
        ]
        
        return len(recent_attempts) >= self.max_attempts
    
    def logout(self, token: str) -> bool:
        """
        Logout user and invalidate session
        
        Args:
            token: JWT token
            
        Returns:
            bool: True if logout successful
        """
        # Find and remove session
        for session_id, session in list(self.sessions.items()):
            if session["token"] == token:
                del self.sessions[session_id]
                return True
        
        return False
    
    def change_password(self, username: str, old_password: str, 
                       new_password: str) -> bool:
        """
        Change user password
        
        Args:
            username: Username
            old_password: Current password
            new_password: New password
            
        Returns:
            bool: True if password changed successfully
        """
        if username not in self.users:
            return False
        
        user = self.users[username]
        
        # Verify old password
        if not Encryption.verify_password(
            old_password,
            user["password_hash"],
            user["password_salt"]
        ):
            return False
        
        # Hash new password
        password_data = Encryption.hash_password(new_password)
        user["password_hash"] = password_data["hash"]
        user["password_salt"] = password_data["salt"]
        
        return True


class RateLimiter:
    """Rate limiter for DDoS protection"""
    
    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        """
        Initialize rate limiter
        
        Args:
            max_requests: Maximum requests per window
            window_seconds: Time window in seconds
        """
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests: Dict[str, List[float]] = {}
    
    def is_allowed(self, identifier: str) -> bool:
        """
        Check if request is allowed
        
        Args:
            identifier: Unique identifier (e.g., IP address, user ID)
            
        Returns:
            bool: True if request is allowed
        """
        current_time = time.time()
        
        if identifier not in self.requests:
            self.requests[identifier] = []
        
        # Remove old requests
        cutoff_time = current_time - self.window_seconds
        self.requests[identifier] = [
            t for t in self.requests[identifier] 
            if t > cutoff_time
        ]
        
        # Check if under limit
        if len(self.requests[identifier]) < self.max_requests:
            self.requests[identifier].append(current_time)
            return True
        
        return False
    
    def get_remaining_requests(self, identifier: str) -> int:
        """Get remaining requests for identifier"""
        if identifier not in self.requests:
            return self.max_requests
        
        current_time = time.time()
        cutoff_time = current_time - self.window_seconds
        
        recent_requests = [
            t for t in self.requests[identifier] 
            if t > cutoff_time
        ]
        
        return max(0, self.max_requests - len(recent_requests))


class SecurityFramework:
    """Main security framework integrating all security components"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize security framework
        
        Args:
            config: Configuration dictionary
        """
        self.config = config or {}
        self.encryption = Encryption()
        self.authentication = Authentication()
        self.rate_limiter = RateLimiter()
        self.audit_log: List[Dict[str, Any]] = []
    
    def initialize(self) -> None:
        """Initialize security framework"""
        self.authentication.initialize()
        self.audit_log.clear()
    
    def log_security_event(self, event_type: str, details: Dict[str, Any]) -> None:
        """
        Log security event
        
        Args:
            event_type: Type of security event
            details: Event details
        """
        self.audit_log.append({
            "event_type": event_type,
            "details": details,
            "timestamp": datetime.now().isoformat()
        })
        
        # Keep only last 1000 events
        if len(self.audit_log) > 1000:
            self.audit_log = self.audit_log[-1000:]
    
    def get_security_report(self) -> Dict[str, Any]:
        """Generate security report"""
        return {
            "total_users": len(self.authentication.users),
            "active_sessions": len(self.authentication.sessions),
            "failed_login_attempts": len(self.authentication.failed_attempts),
            "audit_events": len(self.audit_log),
            "recent_events": self.audit_log[-10:]
        }
    
    def health_check(self) -> bool:
        """Check security framework health"""
        return True
    
    def shutdown(self) -> None:
        """Shutdown security framework"""
        pass
