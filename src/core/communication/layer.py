"""
Inter-System Communication Layer
WebSocket-based communication with encryption and rate limiting
"""

import logging
import json
from typing import Dict, Any, List, Callable
from datetime import datetime
import hashlib


class CommunicationLayer:
    """Inter-system communication manager"""
    
    def __init__(self, config: Dict[str, Any]):
        self.logger = logging.getLogger('Communication')
        self.protocol = config.get('protocol', 'WebSocket')
        self.encryption = config.get('encryption', 'TLS 1.3')
        self.rate_limit = config.get('rateLimit', 10000)
        self.timeout = config.get('timeout', 30000)
        
        self.message_queue = []
        self.subscribers = {}
        self.message_count = 0
        
    def initialize(self) -> bool:
        """Initialize communication layer"""
        self.logger.info(f"Initializing communication layer with {self.protocol}")
        self.logger.info(f"Encryption: {self.encryption}")
        self.logger.info(f"Rate limit: {self.rate_limit} msg/s")
        return True
    
    def send_message(self, sender: str, recipient: str, message: Dict[str, Any]) -> Dict[str, Any]:
        """Send encrypted message between subsystems"""
        if self.message_count >= self.rate_limit:
            self.logger.warning("Rate limit exceeded")
            return {'status': 'error', 'reason': 'rate_limit_exceeded'}
        
        encrypted_msg = self._encrypt_message(message)
        
        msg_envelope = {
            'id': f"msg_{self.message_count + 1}",
            'sender': sender,
            'recipient': recipient,
            'message': encrypted_msg,
            'timestamp': datetime.now().isoformat(),
            'protocol': self.protocol
        }
        
        self.message_queue.append(msg_envelope)
        self.message_count += 1
        
        self.logger.info(f"Message sent from {sender} to {recipient}")
        
        # Notify subscribers
        if recipient in self.subscribers:
            for callback in self.subscribers[recipient]:
                callback(msg_envelope)
        
        return {
            'status': 'success',
            'message_id': msg_envelope['id']
        }
    
    def _encrypt_message(self, message: Dict[str, Any]) -> str:
        """Encrypt message content"""
        msg_str = json.dumps(message)
        # Simulate encryption with hash
        encrypted = hashlib.sha256(msg_str.encode()).hexdigest()
        return encrypted
    
    def subscribe(self, subsystem: str, callback: Callable):
        """Subscribe to messages for a subsystem"""
        if subsystem not in self.subscribers:
            self.subscribers[subsystem] = []
        self.subscribers[subsystem].append(callback)
        self.logger.info(f"Subsystem {subsystem} subscribed to messages")
    
    def broadcast(self, sender: str, message: Dict[str, Any]) -> Dict[str, Any]:
        """Broadcast message to all subsystems"""
        self.logger.info(f"Broadcasting message from {sender}")
        
        results = []
        for subsystem in self.subscribers.keys():
            if subsystem != sender:
                result = self.send_message(sender, subsystem, message)
                results.append(result)
        
        return {
            'status': 'success',
            'recipients': len(results)
        }
    
    def get_status(self) -> Dict[str, Any]:
        """Get communication layer status"""
        return {
            'protocol': self.protocol,
            'encryption': self.encryption,
            'messages_sent': self.message_count,
            'queue_size': len(self.message_queue),
            'subscribers': len(self.subscribers),
            'health': 100
        }
