"""
Integration Tests for AiElon Living OS

Tests the integration of all system components working together.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from core.system import AiElonLivingOS
from ai.ai_engine import AIEngine
from blockchain.aielonchain338 import AielonChain338
from security.security_framework import SecurityFramework
from ui.ui_framework import UIFramework
from plugins.plugin_system import ModularityFramework
from api.api_gateway import APIGateway, APIRequest


class TestSystemIntegration(unittest.TestCase):
    """Integration tests for full system"""
    
    def setUp(self):
        """Set up integrated system"""
        self.system = AiElonLivingOS()
        
        # Initialize all components
        self.ai_engine = AIEngine()
        self.blockchain = AielonChain338(difficulty=2)
        self.security = SecurityFramework()
        self.ui = UIFramework()
        self.plugins = ModularityFramework()
        self.api_gateway = APIGateway()
        
        # Register modules
        self.system.register_module("ai", self.ai_engine)
        self.system.register_module("blockchain", self.blockchain)
        self.system.register_module("security", self.security)
        self.system.register_module("ui", self.ui)
        self.system.register_module("plugins", self.plugins)
        self.system.register_module("api", self.api_gateway)
    
    def test_full_system_startup(self):
        """Test starting the full integrated system"""
        result = self.system.start()
        
        self.assertTrue(result)
        self.assertEqual(self.system.status, "running")
        
        # Verify all modules initialized
        for module_name in ["ai", "blockchain", "security", "ui", "plugins", "api"]:
            self.assertIn(module_name, self.system.modules)
    
    def test_ai_blockchain_integration(self):
        """Test AI engine integrated with blockchain"""
        self.system.start()
        
        # Process AI query about blockchain
        result = self.ai_engine.process_natural_language(
            "What is the blockchain status?"
        )
        
        self.assertEqual(result["intent"], "query")
        self.assertTrue(any(e["type"] == "blockchain" for e in result["entities"]))
        
        # Get blockchain info
        chain_info = self.blockchain.get_chain_info()
        self.assertGreater(chain_info["chain_length"], 0)
    
    def test_security_authentication_flow(self):
        """Test complete authentication flow with security"""
        self.system.start()
        
        # Register user
        registered = self.security.authentication.register_user(
            "testuser", "password123", "test@example.com"
        )
        self.assertTrue(registered)
        
        # Authenticate
        token = self.security.authentication.authenticate("testuser", "password123")
        self.assertIsNotNone(token)
        
        # Verify token
        payload = self.security.authentication.verify_token(token)
        self.assertIsNotNone(payload)
        self.assertEqual(payload["username"], "testuser")
        
        # Log security event
        self.security.log_security_event("login_success", {"username": "testuser"})
        report = self.security.get_security_report()
        self.assertGreater(report["audit_events"], 0)
    
    def test_api_with_all_components(self):
        """Test API gateway integrating all components"""
        self.system.start()
        
        # Test system status
        request = APIRequest("GET", "/system/status")
        response = self.api_gateway.handle_request(request)
        self.assertEqual(response.status_code, 200)
        
        # Test AI endpoint
        request = APIRequest("POST", "/ai/process", {"text": "test query"})
        response = self.api_gateway.handle_request(request)
        self.assertEqual(response.status_code, 200)
        
        # Test blockchain endpoint
        request = APIRequest("GET", "/blockchain/info")
        response = self.api_gateway.handle_request(request)
        self.assertEqual(response.status_code, 200)
    
    def test_ui_dashboard_integration(self):
        """Test UI framework with system data"""
        self.system.start()
        
        # Get main dashboard
        dashboard = self.ui.get_dashboard("main")
        self.assertIsNotNone(dashboard)
        
        # Verify widgets are populated
        self.assertGreater(len(dashboard.widgets), 0)
        
        # Update widget with real data
        widget = dashboard.get_widget("system_status")
        if widget:
            widget.update_data({
                "system_status": self.system.get_status()
            })
            
            render_data = widget.render()
            self.assertIn("data", render_data)
    
    def test_plugin_system_integration(self):
        """Test plugin system with other components"""
        self.system.start()
        
        # Get enabled plugins
        enabled = self.plugins.plugin_manager.get_enabled_plugins()
        self.assertGreater(len(enabled), 0)
        
        # Plugin statistics
        stats = self.plugins.plugin_manager.get_statistics()
        self.assertIn("total_plugins", stats)
    
    def test_end_to_end_transaction_flow(self):
        """Test complete transaction flow through system"""
        self.system.start()
        
        # Register users
        self.security.authentication.register_user("alice", "pass1", "alice@example.com")
        self.security.authentication.register_user("bob", "pass2", "bob@example.com")
        
        # Authenticate Alice
        token = self.security.authentication.authenticate("alice", "pass1")
        self.assertIsNotNone(token)
        
        # Create blockchain transaction
        tx_id = self.blockchain.create_transaction("alice", "bob", 10.0)
        self.assertIsNotNone(tx_id)
        
        # Mine transaction
        block = self.blockchain.mine_pending_transactions("miner1")
        self.assertIsNotNone(block)
        
        # Verify chain
        self.assertTrue(self.blockchain.is_chain_valid())
        
        # Check balances
        alice_balance = self.blockchain.get_balance("alice")
        bob_balance = self.blockchain.get_balance("bob")
        
        self.assertEqual(bob_balance, 10.0)
        self.assertEqual(alice_balance, -10.0)
    
    def test_system_health_check(self):
        """Test health check across all components"""
        self.system.start()
        
        health = self.system.health_check()
        
        self.assertTrue(health["system"])
        self.assertIn("modules", health)
        
        # All modules should be healthy
        for module_name, module_health in health["modules"].items():
            self.assertTrue(module_health, f"Module {module_name} is not healthy")
    
    def test_system_shutdown(self):
        """Test graceful system shutdown"""
        self.system.start()
        self.system.stop()
        
        self.assertEqual(self.system.status, "stopped")


if __name__ == '__main__':
    unittest.main()
