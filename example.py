"""
AiElon Living OS - Complete System Example

This example demonstrates how to initialize and use all components
of the AiElon Living OS platform.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from core.system import AiElonLivingOS
from ai.ai_engine import AIEngine
from blockchain.aielonchain338 import AielonChain338
from security.security_framework import SecurityFramework
from ui.ui_framework import UIFramework
from plugins.plugin_system import ModularityFramework, Plugin, PluginEvent
from api.api_gateway import APIGateway, APIRequest


def main():
    """Main example demonstrating AiElon Living OS features"""
    
    print("=" * 60)
    print("AiElon Living OS v2.0 - Comprehensive Example")
    print("=" * 60)
    print()
    
    # ========================================================================
    # 1. Initialize Core System
    # ========================================================================
    print("1. Initializing Core System...")
    system = AiElonLivingOS({"environment": "production"})
    
    # Initialize all components
    ai_engine = AIEngine()
    blockchain = AielonChain338(difficulty=2)
    security = SecurityFramework()
    ui = UIFramework()
    plugins = ModularityFramework()
    api_gateway = APIGateway()
    
    # Register modules with system
    system.register_module("ai", ai_engine)
    system.register_module("blockchain", blockchain)
    system.register_module("security", security)
    system.register_module("ui", ui)
    system.register_module("plugins", plugins)
    system.register_module("api", api_gateway)
    
    # Start system
    system.start()
    
    status = system.get_status()
    print(f"   ✓ System Status: {status['status']}")
    print(f"   ✓ Version: {status['version']}")
    print(f"   ✓ Modules Loaded: {status['module_count']}")
    print()
    
    # ========================================================================
    # 2. AI Engine - Natural Language Processing
    # ========================================================================
    print("2. Testing AI Engine...")
    
    # Process natural language
    queries = [
        "What is the current blockchain status?",
        "Show me security settings",
        "Create a new transaction"
    ]
    
    for query in queries:
        result = ai_engine.process_natural_language(query)
        print(f"   Query: '{query}'")
        print(f"   Intent: {result['intent']}, Confidence: {result['confidence']}")
    
    # Get recommendations
    recommendations = ai_engine.get_contextual_recommendation({})
    print(f"   ✓ AI Recommendations: {len(recommendations)} suggestions")
    print()
    
    # ========================================================================
    # 3. Security - User Management
    # ========================================================================
    print("3. Testing Security Framework...")
    
    # Register users
    security.authentication.register_user("alice", "AlicePass123!", "alice@example.com")
    security.authentication.register_user("bob", "BobPass456!", "bob@example.com")
    security.authentication.register_user("miner1", "MinerPass789!", "miner@example.com")
    
    # Authenticate Alice
    alice_token = security.authentication.authenticate("alice", "AlicePass123!")
    print(f"   ✓ Alice authenticated: {alice_token[:20]}...")
    
    # Verify token
    payload = security.authentication.verify_token(alice_token)
    print(f"   ✓ Token verified for user: {payload['username']}")
    
    # Test encryption
    sensitive_data = "This is sensitive information"
    encrypted = security.encryption.encrypt_data(sensitive_data)
    decrypted = security.encryption.decrypt_data(encrypted["encrypted"], encrypted["key"])
    print(f"   ✓ Encryption/Decryption: {'Success' if decrypted == sensitive_data else 'Failed'}")
    
    # Test rate limiting
    allowed = security.rate_limiter.is_allowed("192.168.1.100")
    print(f"   ✓ Rate limiter: {'Request allowed' if allowed else 'Rate limit exceeded'}")
    print()
    
    # ========================================================================
    # 4. Blockchain - Transactions
    # ========================================================================
    print("4. Testing AielonChain338 Blockchain...")
    
    # Create transactions
    tx1 = blockchain.create_transaction("alice", "bob", 50.0, metadata={"note": "Payment"})
    tx2 = blockchain.create_transaction("bob", "alice", 20.0, metadata={"note": "Refund"})
    print(f"   ✓ Transaction 1 created: {tx1[:16]}...")
    print(f"   ✓ Transaction 2 created: {tx2[:16]}...")
    
    # Mine block
    print("   ⛏️  Mining block (this may take a moment)...")
    block = blockchain.mine_pending_transactions("miner1")
    print(f"   ✓ Block #{block.index} mined: {block.hash[:20]}...")
    
    # Check balances
    alice_balance = blockchain.get_balance("alice")
    bob_balance = blockchain.get_balance("bob")
    miner_balance = blockchain.get_balance("miner1")
    
    print(f"   ✓ Alice's balance: {alice_balance}")
    print(f"   ✓ Bob's balance: {bob_balance}")
    print(f"   ✓ Miner's balance: {miner_balance}")
    
    # Validate chain
    is_valid = blockchain.is_chain_valid()
    print(f"   ✓ Blockchain valid: {is_valid}")
    
    # Get chain info
    chain_info = blockchain.get_chain_info()
    print(f"   ✓ Chain length: {chain_info['chain_length']} blocks")
    print()
    
    # ========================================================================
    # 5. UI Framework - Dashboards
    # ========================================================================
    print("5. Testing UI Framework...")
    
    # Get main dashboard
    main_dashboard = ui.get_dashboard("main")
    print(f"   ✓ Main dashboard loaded: {main_dashboard.title}")
    print(f"   ✓ Widgets: {len(main_dashboard.widgets)}")
    
    # Create custom dashboard
    custom_dashboard = ui.create_dashboard("trading", "Trading Dashboard")
    
    # Add custom widget
    price_widget = ui.create_widget("chart", "price_chart")
    price_widget.set_position(0, 0)
    price_widget.set_size(600, 400)
    price_widget.update_data({
        "title": "Price Chart",
        "data": [100, 105, 103, 108, 112, 115, 118, 120],
        "labels": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    })
    
    custom_dashboard.add_widget(price_widget)
    custom_dashboard.set_theme("dark")
    
    print(f"   ✓ Custom dashboard created: {custom_dashboard.title}")
    print(f"   ✓ Theme: {custom_dashboard.theme}")
    
    # List all dashboards
    all_dashboards = ui.list_dashboards()
    print(f"   ✓ Total dashboards: {len(all_dashboards)}")
    print()
    
    # ========================================================================
    # 6. Plugin System - Custom Plugin
    # ========================================================================
    print("6. Testing Plugin System...")
    
    # Create custom plugin
    class AnalyticsPlugin(Plugin):
        def __init__(self):
            super().__init__("analytics", "Analytics Plugin", "1.0.0")
            self.events_processed = 0
        
        def initialize(self, config=None):
            super().initialize(config)
            self.register_event_handler("transaction_created", self.on_transaction)
            return True
        
        def on_event(self, event):
            super().on_event(event)
            self.events_processed += 1
    
    # Register and enable plugin
    analytics_plugin = AnalyticsPlugin()
    plugins.plugin_manager.register_plugin(analytics_plugin)
    plugins.plugin_manager.enable_plugin("analytics")
    
    print(f"   ✓ Analytics plugin registered and enabled")
    
    # Emit test event
    event = PluginEvent("transaction_created", {
        "transaction_id": tx1,
        "amount": 50.0
    })
    plugins.plugin_manager.emit_event(event)
    
    print(f"   ✓ Event emitted and processed")
    
    # Get plugin stats
    plugin_stats = plugins.plugin_manager.get_statistics()
    print(f"   ✓ Total plugins: {plugin_stats['total_plugins']}")
    print(f"   ✓ Enabled plugins: {plugin_stats['enabled_plugins']}")
    print()
    
    # ========================================================================
    # 7. API Gateway - API Calls
    # ========================================================================
    print("7. Testing API Gateway...")
    
    # System status endpoint
    request = APIRequest("GET", "/system/status")
    response = api_gateway.handle_request(request)
    print(f"   ✓ GET /system/status: {response.status_code} {response.data['status']}")
    
    # AI processing endpoint
    request = APIRequest("POST", "/ai/process", {
        "text": "What is the blockchain status?"
    })
    response = api_gateway.handle_request(request)
    print(f"   ✓ POST /ai/process: {response.status_code}")
    
    # Blockchain info endpoint
    request = APIRequest("GET", "/blockchain/info")
    response = api_gateway.handle_request(request)
    print(f"   ✓ GET /blockchain/info: {response.status_code}")
    
    # List endpoints
    endpoints = api_gateway.get_endpoints()
    print(f"   ✓ Total API endpoints: {len(endpoints)}")
    
    # API statistics
    api_stats = api_gateway.get_statistics()
    print(f"   ✓ Total requests processed: {api_stats['total_requests']}")
    print()
    
    # ========================================================================
    # 8. System Health Check
    # ========================================================================
    print("8. Performing System Health Check...")
    
    health = system.health_check()
    print(f"   System Health: {'✓ Healthy' if health['system'] else '✗ Unhealthy'}")
    
    for module_name, module_health in health["modules"].items():
        status_icon = "✓" if module_health else "✗"
        print(f"   {status_icon} Module '{module_name}': {'Healthy' if module_health else 'Unhealthy'}")
    
    print()
    
    # ========================================================================
    # 9. Statistics Summary
    # ========================================================================
    print("9. System Statistics Summary...")
    
    # Get statistics from all modules
    ai_stats = ai_engine.get_statistics()
    blockchain_stats = blockchain.get_chain_info()
    security_report = security.get_security_report()
    ui_stats = ui.get_ui_statistics()
    
    print(f"   AI Engine:")
    print(f"     - Queries processed: {ai_stats['queries_processed']}")
    print(f"     - Accuracy score: {ai_stats['accuracy_score']}")
    
    print(f"   Blockchain:")
    print(f"     - Chain length: {blockchain_stats['chain_length']} blocks")
    print(f"     - Pending transactions: {blockchain_stats['pending_transactions']}")
    
    print(f"   Security:")
    print(f"     - Total users: {security_report['total_users']}")
    print(f"     - Active sessions: {security_report['active_sessions']}")
    
    print(f"   UI:")
    print(f"     - Total dashboards: {ui_stats['total_dashboards']}")
    print(f"     - Total widgets: {ui_stats['total_widgets']}")
    
    print()
    
    # ========================================================================
    # 10. Graceful Shutdown
    # ========================================================================
    print("10. Shutting down system...")
    system.stop()
    print(f"   ✓ System stopped gracefully")
    print()
    
    print("=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
