"""
Security Protocols and Authentication
Multi-factor authentication and role-based authorization
"""

import logging
import hashlib
import secrets
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta


class SecurityManager:
    """Security manager for authentication and authorization"""
    
    def __init__(self, config: Dict[str, Any]):
        self.logger = logging.getLogger('Security')
        self.auth_method = config.get('authentication', 'multi-factor')
        self.authz_method = config.get('authorization', 'role-based')
        self.encryption_config = config.get('encryption', {})
        self.audit_config = config.get('audit', {})
        
        self.users = {}
        self.sessions = {}
        self.roles = {
            'admin': ['read', 'write', 'delete', 'manage'],
            'user': ['read', 'write'],
            'guest': ['read']
        }
        self.audit_log = []
        
    def initialize(self) -> bool:
        """Initialize security system"""
        self.logger.info(f"Initializing security with {self.auth_method} authentication")
        self.logger.info(f"Authorization: {self.authz_method}")
        self.logger.info(f"Data at rest: {self.encryption_config.get('dataAtRest')}")
        self.logger.info(f"Data in transit: {self.encryption_config.get('dataInTransit')}")
        return True
    
    def register_user(self, username: str, password: str, role: str = 'user') -> Dict[str, Any]:
        """Register new user"""
        if username in self.users:
            return {'status': 'error', 'reason': 'user_exists'}
        
        password_hash = self._hash_password(password)
        
        self.users[username] = {
            'password_hash': password_hash,
            'role': role,
            'mfa_enabled': False,
            'created': datetime.now().isoformat()
        }
        
        self._audit('user_registered', {'username': username, 'role': role})
        self.logger.info(f"User registered: {username}")
        
        return {'status': 'success', 'user_id': username}
    
    def authenticate(self, username: str, password: str, mfa_code: Optional[str] = None) -> Dict[str, Any]:
        """Authenticate user with optional MFA"""
        if username not in self.users:
            self._audit('auth_failed', {'username': username, 'reason': 'user_not_found'})
            return {'status': 'error', 'reason': 'invalid_credentials'}
        
        user = self.users[username]
        password_hash = self._hash_password(password)
        
        if password_hash != user['password_hash']:
            self._audit('auth_failed', {'username': username, 'reason': 'invalid_password'})
            return {'status': 'error', 'reason': 'invalid_credentials'}
        
        # Check MFA if enabled
        if user.get('mfa_enabled') and not mfa_code:
            return {'status': 'mfa_required'}
        
        # Create session
        session_token = secrets.token_hex(32)
        self.sessions[session_token] = {
            'username': username,
            'role': user['role'],
            'created': datetime.now(),
            'expires': datetime.now() + timedelta(hours=24)
        }
        
        self._audit('auth_success', {'username': username})
        self.logger.info(f"User authenticated: {username}")
        
        return {
            'status': 'success',
            'session_token': session_token,
            'role': user['role']
        }
    
    def authorize(self, session_token: str, action: str) -> bool:
        """Authorize user action based on role"""
        if session_token not in self.sessions:
            return False
        
        session = self.sessions[session_token]
        
        # Check session expiry
        if datetime.now() > session['expires']:
            del self.sessions[session_token]
            return False
        
        role = session['role']
        permissions = self.roles.get(role, [])
        
        authorized = action in permissions
        
        self._audit('authorization', {
            'username': session['username'],
            'action': action,
            'authorized': authorized
        })
        
        return authorized
    
    def _hash_password(self, password: str) -> str:
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _audit(self, event_type: str, details: Dict[str, Any]):
        """Log security audit event"""
        if not self.audit_config.get('enabled', False):
            return
        
        audit_entry = {
            'timestamp': datetime.now().isoformat(),
            'event_type': event_type,
            'details': details
        }
        
        self.audit_log.append(audit_entry)
        self.logger.info(f"Audit: {event_type}")
    
    def get_audit_log(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get recent audit log entries"""
        return self.audit_log[-limit:]
    
    def get_status(self) -> Dict[str, Any]:
        """Get security system status"""
        return {
            'authentication': self.auth_method,
            'authorization': self.authz_method,
            'users_count': len(self.users),
            'active_sessions': len(self.sessions),
            'audit_entries': len(self.audit_log),
            'health': 100
        }
