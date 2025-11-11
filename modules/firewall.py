#!/usr/bin/env python3
"""
Firewall Security Layers
Multi-layered security system for AiElon ecosystem
"""

import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Set
from enum import Enum
import re
import hashlib


class ThreatLevel(Enum):
    """Threat level enumeration"""
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ActionType(Enum):
    """Firewall action types"""
    ALLOW = "allow"
    BLOCK = "block"
    QUARANTINE = "quarantine"
    LOG = "log"


class FirewallLayer:
    """
    Multi-layered Firewall Security System
    Provides comprehensive protection with intrusion detection
    """
    
    def __init__(self):
        self.blocked_ips: Set[str] = set()
        self.whitelisted_ips: Set[str] = set()
        self.firewall_rules: List[Dict[str, Any]] = []
        self.intrusion_attempts: List[Dict[str, Any]] = []
        self.access_log: List[Dict[str, Any]] = []
        self.rate_limits: Dict[str, List[datetime]] = {}
        self.logger = logging.getLogger('FirewallLayer')
        
        # Configuration
        self.max_requests_per_minute = 60
        self.max_failed_attempts = 5
        self.block_duration_minutes = 30
        self.ddos_threshold = 100
        
        # Initialize default rules
        self._initialize_default_rules()
        
        self.logger.info("Firewall Security Layers initialized")
    
    def _initialize_default_rules(self):
        """Initialize default firewall rules"""
        default_rules = [
            {
                'name': 'Block known malicious patterns',
                'pattern': r'(script|alert|onerror|eval|exec)',
                'action': ActionType.BLOCK,
                'threat_level': ThreatLevel.HIGH
            },
            {
                'name': 'SQL Injection protection',
                'pattern': r'(\bSELECT\b|\bUNION\b|\bDROP\b|\bINSERT\b).*(\bFROM\b|\bWHERE\b)',
                'action': ActionType.BLOCK,
                'threat_level': ThreatLevel.CRITICAL
            },
            {
                'name': 'XSS protection',
                'pattern': r'<script[^>]*>.*?</script>',
                'action': ActionType.BLOCK,
                'threat_level': ThreatLevel.HIGH
            },
            {
                'name': 'Path traversal protection',
                'pattern': r'\.\./|\.\.',
                'action': ActionType.BLOCK,
                'threat_level': ThreatLevel.HIGH
            }
        ]
        
        self.firewall_rules.extend(default_rules)
        self.logger.info(f"Loaded {len(default_rules)} default firewall rules")
    
    def validate_request(self, request: Dict[str, Any]) -> tuple[bool, ThreatLevel, str]:
        """
        Validate incoming request through firewall layers
        Returns (is_allowed, threat_level, reason)
        """
        try:
            source_ip = request.get('source_ip', 'unknown')
            payload = request.get('payload', '')
            endpoint = request.get('endpoint', '')
            
            # Layer 1: IP Blacklist/Whitelist Check
            if source_ip in self.blocked_ips:
                self._log_access(request, ActionType.BLOCK, "Blocked IP")
                return False, ThreatLevel.HIGH, "IP address is blocked"
            
            if source_ip in self.whitelisted_ips:
                self._log_access(request, ActionType.ALLOW, "Whitelisted IP")
                return True, ThreatLevel.NONE, "Whitelisted"
            
            # Layer 2: Rate Limiting
            if not self._check_rate_limit(source_ip):
                self._log_intrusion(request, "Rate limit exceeded")
                self._temporary_block(source_ip, "Rate limit violation")
                return False, ThreatLevel.MEDIUM, "Rate limit exceeded"
            
            # Layer 3: Pattern Matching (Attack Signatures)
            for rule in self.firewall_rules:
                pattern = rule['pattern']
                combined_input = f"{payload} {endpoint}"
                
                if re.search(pattern, combined_input, re.IGNORECASE):
                    threat_level = rule['threat_level']
                    self._log_intrusion(request, f"Matched rule: {rule['name']}")
                    
                    if rule['action'] == ActionType.BLOCK:
                        self._temporary_block(source_ip, rule['name'])
                        return False, threat_level, f"Blocked by rule: {rule['name']}"
            
            # Layer 4: DDoS Protection
            if self._detect_ddos_pattern(source_ip):
                self._log_intrusion(request, "DDoS pattern detected")
                self._block_ip(source_ip, "DDoS attack detected")
                return False, ThreatLevel.CRITICAL, "DDoS attack detected"
            
            # Layer 5: Anomaly Detection
            threat_level = self._detect_anomalies(request)
            if threat_level in [ThreatLevel.HIGH, ThreatLevel.CRITICAL]:
                self._log_intrusion(request, "Anomalous behavior detected")
                return False, threat_level, "Anomalous behavior detected"
            
            # Request passed all layers
            self._log_access(request, ActionType.ALLOW, "Passed all security layers")
            return True, ThreatLevel.NONE, "Request allowed"
            
        except Exception as e:
            self.logger.error(f"Request validation failed: {e}")
            return False, ThreatLevel.CRITICAL, f"Validation error: {str(e)}"
    
    def _check_rate_limit(self, source_ip: str) -> bool:
        """Check if source IP exceeds rate limits"""
        try:
            current_time = datetime.now()
            cutoff_time = current_time - timedelta(minutes=1)
            
            # Initialize if new IP
            if source_ip not in self.rate_limits:
                self.rate_limits[source_ip] = []
            
            # Clean old entries
            self.rate_limits[source_ip] = [
                timestamp for timestamp in self.rate_limits[source_ip]
                if timestamp > cutoff_time
            ]
            
            # Add current request
            self.rate_limits[source_ip].append(current_time)
            
            # Check limit
            return len(self.rate_limits[source_ip]) <= self.max_requests_per_minute
            
        except Exception as e:
            self.logger.error(f"Rate limit check failed: {e}")
            return True  # Allow on error
    
    def _detect_ddos_pattern(self, source_ip: str) -> bool:
        """Detect DDoS attack patterns"""
        try:
            if source_ip not in self.rate_limits:
                return False
            
            # Check if request rate exceeds DDoS threshold
            current_time = datetime.now()
            cutoff_time = current_time - timedelta(minutes=1)
            
            recent_requests = [
                timestamp for timestamp in self.rate_limits[source_ip]
                if timestamp > cutoff_time
            ]
            
            return len(recent_requests) > self.ddos_threshold
            
        except Exception as e:
            self.logger.error(f"DDoS detection failed: {e}")
            return False
    
    def _detect_anomalies(self, request: Dict[str, Any]) -> ThreatLevel:
        """Detect anomalous behavior"""
        try:
            payload_size = len(str(request.get('payload', '')))
            
            # Check for unusually large payloads
            if payload_size > 10000:
                return ThreatLevel.MEDIUM
            
            # Additional anomaly detection logic would go here
            return ThreatLevel.NONE
            
        except Exception as e:
            self.logger.error(f"Anomaly detection failed: {e}")
            return ThreatLevel.LOW
    
    def _block_ip(self, ip: str, reason: str):
        """Permanently block an IP address"""
        self.blocked_ips.add(ip)
        self.logger.warning(f"IP blocked: {ip}, Reason: {reason}")
    
    def _temporary_block(self, ip: str, reason: str):
        """Temporarily block an IP address"""
        # In production, this would use a time-based system
        self.blocked_ips.add(ip)
        self.logger.warning(f"IP temporarily blocked: {ip}, Reason: {reason}")
    
    def _log_access(self, request: Dict[str, Any], action: ActionType, reason: str):
        """Log access attempt"""
        self.access_log.append({
            'timestamp': datetime.now().isoformat(),
            'source_ip': request.get('source_ip', 'unknown'),
            'endpoint': request.get('endpoint', ''),
            'action': action.value,
            'reason': reason
        })
    
    def _log_intrusion(self, request: Dict[str, Any], details: str):
        """Log intrusion attempt"""
        self.intrusion_attempts.append({
            'timestamp': datetime.now().isoformat(),
            'source_ip': request.get('source_ip', 'unknown'),
            'endpoint': request.get('endpoint', ''),
            'payload': request.get('payload', ''),
            'details': details
        })
        self.logger.warning(f"Intrusion attempt logged: {details}")
    
    def whitelist_ip(self, ip: str) -> bool:
        """Add IP to whitelist"""
        try:
            self.whitelisted_ips.add(ip)
            if ip in self.blocked_ips:
                self.blocked_ips.remove(ip)
            self.logger.info(f"IP whitelisted: {ip}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to whitelist IP: {e}")
            return False
    
    def unblock_ip(self, ip: str) -> bool:
        """Remove IP from blocklist"""
        try:
            if ip in self.blocked_ips:
                self.blocked_ips.remove(ip)
                self.logger.info(f"IP unblocked: {ip}")
                return True
            return False
        except Exception as e:
            self.logger.error(f"Failed to unblock IP: {e}")
            return False
    
    def add_firewall_rule(self, rule: Dict[str, Any]) -> bool:
        """Add custom firewall rule"""
        try:
            required_fields = ['name', 'pattern', 'action', 'threat_level']
            if all(field in rule for field in required_fields):
                self.firewall_rules.append(rule)
                self.logger.info(f"Firewall rule added: {rule['name']}")
                return True
            else:
                self.logger.error("Invalid firewall rule format")
                return False
        except Exception as e:
            self.logger.error(f"Failed to add firewall rule: {e}")
            return False
    
    def get_security_statistics(self) -> Dict[str, Any]:
        """Get security statistics"""
        return {
            'blocked_ips': len(self.blocked_ips),
            'whitelisted_ips': len(self.whitelisted_ips),
            'firewall_rules': len(self.firewall_rules),
            'intrusion_attempts': len(self.intrusion_attempts),
            'access_log_entries': len(self.access_log),
            'total_blocked_requests': sum(
                1 for log in self.access_log 
                if log['action'] == ActionType.BLOCK.value
            )
        }
    
    def initialize(self):
        """Initialize Firewall"""
        self.logger.info("Firewall initialized")
    
    def health_check(self) -> Dict[str, Any]:
        """Perform health check"""
        stats = self.get_security_statistics()
        return {
            'status': 'operational',
            'blocked_ips': stats['blocked_ips'],
            'active_rules': stats['firewall_rules'],
            'intrusion_attempts': stats['intrusion_attempts']
        }


if __name__ == "__main__":
    # Test Firewall
    firewall = FirewallLayer()
    request = {
        'source_ip': '192.168.1.100',
        'endpoint': '/api/data',
        'payload': 'normal request'
    }
    allowed, threat, reason = firewall.validate_request(request)
    print(f"Request allowed: {allowed}, Threat level: {threat}, Reason: {reason}")
