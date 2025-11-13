"""
Unit Tests for AiElon Living OS Core System
"""

import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from core.system import AiElonLivingOS


class TestAiElonLivingOS(unittest.TestCase):
    """Test cases for AiElon Living OS core system"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.system = AiElonLivingOS({"test_mode": True})
    
    def test_initialization(self):
        """Test system initialization"""
        self.assertEqual(self.system.version, "2.0.0")
        self.assertEqual(self.system.status, "initialized")
        self.assertIsNotNone(self.system.logger)
        self.assertEqual(len(self.system.modules), 0)
    
    def test_module_registration(self):
        """Test module registration"""
        class MockModule:
            def initialize(self):
                pass
        
        module = MockModule()
        self.system.register_module("test_module", module)
        
        self.assertIn("test_module", self.system.modules)
        self.assertEqual(self.system.modules["test_module"], module)
    
    def test_system_start(self):
        """Test system start"""
        class MockModule:
            def initialize(self):
                self.initialized = True
        
        module = MockModule()
        self.system.register_module("test_module", module)
        
        result = self.system.start()
        
        self.assertTrue(result)
        self.assertEqual(self.system.status, "running")
        self.assertTrue(module.initialized)
    
    def test_system_stop(self):
        """Test system stop"""
        class MockModule:
            def shutdown(self):
                self.shut_down = True
        
        module = MockModule()
        self.system.register_module("test_module", module)
        self.system.start()
        self.system.stop()
        
        self.assertEqual(self.system.status, "stopped")
        self.assertTrue(module.shut_down)
    
    def test_get_status(self):
        """Test get status"""
        self.system.start()
        status = self.system.get_status()
        
        self.assertIn("version", status)
        self.assertIn("status", status)
        self.assertIn("uptime_seconds", status)
        self.assertIn("modules", status)
        self.assertEqual(status["version"], "2.0.0")
    
    def test_health_check(self):
        """Test health check"""
        self.system.start()
        health = self.system.health_check()
        
        self.assertIn("system", health)
        self.assertIn("modules", health)
        self.assertTrue(health["system"])


if __name__ == '__main__':
    unittest.main()
