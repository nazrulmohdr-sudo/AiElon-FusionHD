"""
Unit Tests for Plugin System
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from plugins.plugin_system import Plugin, PluginEvent, PluginManager, ModularityFramework


class TestPluginEvent(unittest.TestCase):
    """Test cases for PluginEvent"""
    
    def test_event_creation(self):
        """Test event creation"""
        event = PluginEvent("test_event", {"data": "value"}, "test_plugin")
        
        self.assertEqual(event.event_type, "test_event")
        self.assertEqual(event.data["data"], "value")
        self.assertEqual(event.source, "test_plugin")
        self.assertFalse(event.handled)
    
    def test_event_to_dict(self):
        """Test event to dictionary conversion"""
        event = PluginEvent("test_event", {"data": "value"})
        event_dict = event.to_dict()
        
        self.assertIn("event_type", event_dict)
        self.assertIn("data", event_dict)
        self.assertIn("timestamp", event_dict)


class TestPlugin(unittest.TestCase):
    """Test cases for Plugin"""
    
    def test_plugin_creation(self):
        """Test plugin creation"""
        plugin = Plugin("test_plugin", "Test Plugin", "1.0.0")
        
        self.assertEqual(plugin.plugin_id, "test_plugin")
        self.assertEqual(plugin.name, "Test Plugin")
        self.assertEqual(plugin.version, "1.0.0")
        self.assertFalse(plugin.enabled)
    
    def test_plugin_initialization(self):
        """Test plugin initialization"""
        plugin = Plugin("test_plugin", "Test Plugin", "1.0.0")
        result = plugin.initialize({"setting": "value"})
        
        self.assertTrue(result)
        self.assertTrue(plugin.enabled)
        self.assertEqual(plugin.config["setting"], "value")
    
    def test_plugin_event_handler(self):
        """Test plugin event handler registration"""
        plugin = Plugin("test_plugin", "Test Plugin", "1.0.0")
        
        def test_handler(event):
            event.data["handled_by"] = "test_handler"
        
        plugin.register_event_handler("test_event", test_handler)
        
        self.assertIn("test_event", plugin.event_handlers)
        
        # Test handling
        event = PluginEvent("test_event", {})
        plugin.on_event(event)
        
        self.assertEqual(event.data["handled_by"], "test_handler")
    
    def test_plugin_info(self):
        """Test getting plugin info"""
        plugin = Plugin("test_plugin", "Test Plugin", "1.0.0")
        info = plugin.get_info()
        
        self.assertIn("plugin_id", info)
        self.assertIn("name", info)
        self.assertIn("version", info)


class TestPluginManager(unittest.TestCase):
    """Test cases for PluginManager"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.manager = PluginManager()
        self.manager.initialize()
    
    def test_register_plugin(self):
        """Test registering plugin"""
        plugin = Plugin("test_plugin", "Test Plugin", "1.0.0")
        result = self.manager.register_plugin(plugin)
        
        self.assertTrue(result)
        self.assertIn("test_plugin", self.manager.plugins)
    
    def test_enable_plugin(self):
        """Test enabling plugin"""
        plugin = Plugin("test_plugin", "Test Plugin", "1.0.0")
        self.manager.register_plugin(plugin)
        
        result = self.manager.enable_plugin("test_plugin")
        
        self.assertTrue(result)
        self.assertTrue(plugin.enabled)
    
    def test_disable_plugin(self):
        """Test disabling plugin"""
        plugin = Plugin("test_plugin", "Test Plugin", "1.0.0")
        self.manager.register_plugin(plugin)
        self.manager.enable_plugin("test_plugin")
        
        result = self.manager.disable_plugin("test_plugin")
        
        self.assertTrue(result)
        self.assertFalse(plugin.enabled)
    
    def test_unregister_plugin(self):
        """Test unregistering plugin"""
        plugin = Plugin("test_plugin", "Test Plugin", "1.0.0")
        self.manager.register_plugin(plugin)
        
        result = self.manager.unregister_plugin("test_plugin")
        
        self.assertTrue(result)
        self.assertNotIn("test_plugin", self.manager.plugins)
    
    def test_plugin_dependencies(self):
        """Test plugin dependency management"""
        plugin1 = Plugin("plugin1", "Plugin 1", "1.0.0")
        plugin2 = Plugin("plugin2", "Plugin 2", "1.0.0")
        plugin2.dependencies = ["plugin1"]
        
        # Register and enable plugin1
        self.manager.register_plugin(plugin1)
        self.manager.enable_plugin("plugin1")
        
        # Register plugin2 (depends on plugin1)
        result = self.manager.register_plugin(plugin2)
        self.assertTrue(result)
        
        # Enable plugin2
        result = self.manager.enable_plugin("plugin2")
        self.assertTrue(result)
        
        # Cannot disable plugin1 while plugin2 is enabled
        result = self.manager.disable_plugin("plugin1")
        self.assertFalse(result)
    
    def test_event_emission(self):
        """Test event emission and processing"""
        plugin = Plugin("test_plugin", "Test Plugin", "1.0.0")
        
        handled = []
        
        def handler(event):
            handled.append(event.event_type)
        
        plugin.register_event_handler("test_event", handler)
        self.manager.register_plugin(plugin)
        self.manager.enable_plugin("test_plugin")
        
        event = PluginEvent("test_event", {})
        self.manager.emit_event(event)
        
        self.assertIn("test_event", handled)
        self.assertTrue(event.handled)
    
    def test_list_plugins(self):
        """Test listing plugins"""
        plugin1 = Plugin("plugin1", "Plugin 1", "1.0.0")
        plugin2 = Plugin("plugin2", "Plugin 2", "1.0.0")
        
        self.manager.register_plugin(plugin1)
        self.manager.register_plugin(plugin2)
        
        plugins = self.manager.list_plugins()
        
        self.assertEqual(len(plugins), 2)
    
    def test_statistics(self):
        """Test getting statistics"""
        stats = self.manager.get_statistics()
        
        self.assertIn("total_plugins", stats)
        self.assertIn("enabled_plugins", stats)
        self.assertIn("events_processed", stats)


class TestModularityFramework(unittest.TestCase):
    """Test cases for ModularityFramework"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.framework = ModularityFramework()
        self.framework.initialize()
    
    def test_initialization(self):
        """Test framework initialization"""
        # Should have core plugins registered
        stats = self.framework.plugin_manager.get_statistics()
        self.assertGreater(stats["total_plugins"], 0)
    
    def test_api_hooks(self):
        """Test API hook registration and execution"""
        results = []
        
        def hook_callback(value):
            results.append(value * 2)
            return value * 2
        
        self.framework.register_api_hook("test_hook", hook_callback)
        
        hook_results = self.framework.execute_hook("test_hook", 5)
        
        self.assertEqual(len(hook_results), 1)
        self.assertEqual(hook_results[0], 10)
    
    def test_create_plugin_from_spec(self):
        """Test creating plugin from specification"""
        spec = {
            "plugin_id": "spec_plugin",
            "name": "Spec Plugin",
            "version": "1.0.0",
            "dependencies": []
        }
        
        plugin = self.framework.create_plugin_from_spec(spec)
        
        self.assertIsNotNone(plugin)
        self.assertEqual(plugin.plugin_id, "spec_plugin")
    
    def test_framework_info(self):
        """Test getting framework info"""
        info = self.framework.get_framework_info()
        
        self.assertIn("plugin_statistics", info)
        self.assertIn("registered_hooks", info)


if __name__ == '__main__':
    unittest.main()
