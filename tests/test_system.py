"""
Unit tests for AiElon FusionHD System
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.system import SystemCore
from src.core.communication.layer import CommunicationLayer
from src.core.security.manager import SecurityManager
from src.core.monitoring.system import MonitoringSystem


class TestSystemCore(unittest.TestCase):
    """Test core system functionality"""
    
    def setUp(self):
        self.system = SystemCore('config/system.json')
    
    def test_initialization(self):
        """Test system initialization"""
        result = self.system.initialize()
        self.assertTrue(result)
        self.assertEqual(self.system.operational_capacity, 100)
        self.assertEqual(self.system.error_count, 0)
    
    def test_system_status(self):
        """Test system status retrieval"""
        self.system.initialize()
        status = self.system.get_system_status()
        self.assertIn('name', status)
        self.assertIn('operational_capacity', status)
        self.assertEqual(status['status'], 'operational')
    
    def test_health_check(self):
        """Test health check"""
        self.system.initialize()
        result = self.system.health_check()
        self.assertTrue(result)


class TestCommunication(unittest.TestCase):
    """Test communication layer"""
    
    def setUp(self):
        config = {
            'protocol': 'WebSocket',
            'encryption': 'TLS 1.3',
            'rateLimit': 10000,
            'timeout': 30000
        }
        self.comm = CommunicationLayer(config)
        self.comm.initialize()
    
    def test_send_message(self):
        """Test message sending"""
        result = self.comm.send_message(
            'subsystem1',
            'subsystem2',
            {'type': 'test', 'data': 'hello'}
        )
        self.assertEqual(result['status'], 'success')
        self.assertIn('message_id', result)
    
    def test_broadcast(self):
        """Test message broadcasting"""
        # Subscribe multiple subsystems
        self.comm.subscribe('sub1', lambda msg: None)
        self.comm.subscribe('sub2', lambda msg: None)
        
        result = self.comm.broadcast('sender', {'type': 'broadcast'})
        self.assertEqual(result['status'], 'success')


class TestSecurity(unittest.TestCase):
    """Test security manager"""
    
    def setUp(self):
        config = {
            'authentication': 'multi-factor',
            'authorization': 'role-based',
            'encryption': {
                'dataAtRest': 'AES-256-GCM',
                'dataInTransit': 'TLS 1.3'
            },
            'audit': {'enabled': True}
        }
        self.security = SecurityManager(config)
        self.security.initialize()
    
    def test_user_registration(self):
        """Test user registration"""
        result = self.security.register_user('testuser', 'password123', 'user')
        self.assertEqual(result['status'], 'success')
    
    def test_authentication(self):
        """Test user authentication"""
        self.security.register_user('testuser', 'password123', 'user')
        result = self.security.authenticate('testuser', 'password123')
        self.assertEqual(result['status'], 'success')
        self.assertIn('session_token', result)
    
    def test_authorization(self):
        """Test role-based authorization"""
        self.security.register_user('admin', 'admin123', 'admin')
        auth_result = self.security.authenticate('admin', 'admin123')
        token = auth_result['session_token']
        
        # Admin can delete
        self.assertTrue(self.security.authorize(token, 'delete'))
        
        # Register regular user
        self.security.register_user('user', 'user123', 'user')
        auth_result = self.security.authenticate('user', 'user123')
        token = auth_result['session_token']
        
        # User cannot delete
        self.assertFalse(self.security.authorize(token, 'delete'))


class TestMonitoring(unittest.TestCase):
    """Test monitoring system"""
    
    def setUp(self):
        config = {
            'healthCheck': {'enabled': True, 'interval': 30},
            'metrics': {'enabled': True, 'aggregation': 'real-time'},
            'alerting': {'enabled': True, 'channels': ['email', 'sms']}
        }
        self.monitoring = MonitoringSystem(config)
        self.monitoring.initialize()
    
    def test_record_metric(self):
        """Test metric recording"""
        self.monitoring.record_metric('cpu_usage', 50.0)
        metrics = self.monitoring.get_metrics('cpu_usage')
        self.assertIn('cpu_usage', metrics)
        self.assertEqual(len(metrics['cpu_usage']), 1)
    
    def test_alert_creation(self):
        """Test alert creation on threshold breach"""
        # Record high CPU usage
        self.monitoring.record_metric('cpu_usage', 95.0)
        alerts = self.monitoring.get_alerts()
        self.assertGreater(len(alerts), 0)


def run_tests():
    """Run all tests"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestSystemCore))
    suite.addTests(loader.loadTestsFromTestCase(TestCommunication))
    suite.addTests(loader.loadTestsFromTestCase(TestSecurity))
    suite.addTests(loader.loadTestsFromTestCase(TestMonitoring))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
