"""
AiElon Living OS - Plugin System

This module provides a modular plugin architecture for seamless addition of new features:
- Plugin loading and management
- Event-driven architecture
- Plugin lifecycle management
- Dependency management
"""

from typing import Dict, Any, List, Callable, Optional
from datetime import datetime
import importlib
import inspect


class PluginEvent:
    """Event object for plugin communication"""
    
    def __init__(self, event_type: str, data: Dict[str, Any] = None, source: str = None):
        """
        Initialize event
        
        Args:
            event_type: Type of event
            data: Event data
            source: Event source plugin
        """
        self.event_type = event_type
        self.data = data or {}
        self.source = source
        self.timestamp = datetime.now().isoformat()
        self.handled = False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert event to dictionary"""
        return {
            "event_type": self.event_type,
            "data": self.data,
            "source": self.source,
            "timestamp": self.timestamp,
            "handled": self.handled
        }


class Plugin:
    """Base plugin class that all plugins should inherit from"""
    
    def __init__(self, plugin_id: str, name: str, version: str):
        """
        Initialize plugin
        
        Args:
            plugin_id: Unique plugin identifier
            name: Plugin name
            version: Plugin version
        """
        self.plugin_id = plugin_id
        self.name = name
        self.version = version
        self.enabled = False
        self.dependencies: List[str] = []
        self.event_handlers: Dict[str, List[Callable]] = {}
        self.config: Dict[str, Any] = {}
    
    def initialize(self, config: Dict[str, Any] = None) -> bool:
        """
        Initialize the plugin
        
        Args:
            config: Plugin configuration
            
        Returns:
            bool: True if initialization successful
        """
        self.config = config or {}
        self.enabled = True
        return True
    
    def shutdown(self) -> None:
        """Shutdown the plugin"""
        self.enabled = False
    
    def on_event(self, event: PluginEvent) -> None:
        """
        Handle an event
        
        Args:
            event: Event to handle
        """
        if event.event_type in self.event_handlers:
            for handler in self.event_handlers[event.event_type]:
                handler(event)
    
    def register_event_handler(self, event_type: str, handler: Callable) -> None:
        """
        Register an event handler
        
        Args:
            event_type: Type of event to handle
            handler: Handler function
        """
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        self.event_handlers[event_type].append(handler)
    
    def get_info(self) -> Dict[str, Any]:
        """Get plugin information"""
        return {
            "plugin_id": self.plugin_id,
            "name": self.name,
            "version": self.version,
            "enabled": self.enabled,
            "dependencies": self.dependencies,
            "event_handlers": list(self.event_handlers.keys())
        }


class PluginManager:
    """Manager for plugin lifecycle and orchestration"""
    
    def __init__(self):
        """Initialize plugin manager"""
        self.plugins: Dict[str, Plugin] = {}
        self.event_queue: List[PluginEvent] = []
        self.event_history: List[PluginEvent] = []
    
    def initialize(self) -> None:
        """Initialize plugin manager"""
        self.plugins.clear()
        self.event_queue.clear()
        self.event_history.clear()
    
    def register_plugin(self, plugin: Plugin) -> bool:
        """
        Register a plugin
        
        Args:
            plugin: Plugin to register
            
        Returns:
            bool: True if registration successful
        """
        if plugin.plugin_id in self.plugins:
            return False
        
        # Check dependencies
        for dep in plugin.dependencies:
            if dep not in self.plugins or not self.plugins[dep].enabled:
                return False
        
        self.plugins[plugin.plugin_id] = plugin
        return True
    
    def unregister_plugin(self, plugin_id: str) -> bool:
        """
        Unregister a plugin
        
        Args:
            plugin_id: Plugin identifier
            
        Returns:
            bool: True if unregistration successful
        """
        if plugin_id not in self.plugins:
            return False
        
        # Check if other plugins depend on this
        for other_plugin in self.plugins.values():
            if plugin_id in other_plugin.dependencies and other_plugin.enabled:
                return False
        
        plugin = self.plugins[plugin_id]
        plugin.shutdown()
        del self.plugins[plugin_id]
        return True
    
    def enable_plugin(self, plugin_id: str, config: Dict[str, Any] = None) -> bool:
        """
        Enable a plugin
        
        Args:
            plugin_id: Plugin identifier
            config: Plugin configuration
            
        Returns:
            bool: True if enabled successfully
        """
        if plugin_id not in self.plugins:
            return False
        
        plugin = self.plugins[plugin_id]
        
        # Check dependencies are enabled
        for dep in plugin.dependencies:
            if dep not in self.plugins or not self.plugins[dep].enabled:
                return False
        
        return plugin.initialize(config)
    
    def disable_plugin(self, plugin_id: str) -> bool:
        """
        Disable a plugin
        
        Args:
            plugin_id: Plugin identifier
            
        Returns:
            bool: True if disabled successfully
        """
        if plugin_id not in self.plugins:
            return False
        
        # Check if other enabled plugins depend on this
        for other_plugin in self.plugins.values():
            if plugin_id in other_plugin.dependencies and other_plugin.enabled:
                return False
        
        plugin = self.plugins[plugin_id]
        plugin.shutdown()
        return True
    
    def emit_event(self, event: PluginEvent) -> None:
        """
        Emit an event to all plugins
        
        Args:
            event: Event to emit
        """
        self.event_queue.append(event)
        self.process_events()
    
    def process_events(self) -> None:
        """Process queued events"""
        while self.event_queue:
            event = self.event_queue.pop(0)
            
            # Send to all enabled plugins
            for plugin in self.plugins.values():
                if plugin.enabled:
                    plugin.on_event(event)
            
            # Add to history
            event.handled = True
            self.event_history.append(event)
            
            # Keep only last 100 events
            if len(self.event_history) > 100:
                self.event_history = self.event_history[-100:]
    
    def get_plugin(self, plugin_id: str) -> Optional[Plugin]:
        """Get plugin by ID"""
        return self.plugins.get(plugin_id)
    
    def list_plugins(self) -> List[Dict[str, Any]]:
        """List all plugins"""
        return [plugin.get_info() for plugin in self.plugins.values()]
    
    def get_enabled_plugins(self) -> List[str]:
        """Get list of enabled plugin IDs"""
        return [
            plugin_id for plugin_id, plugin in self.plugins.items()
            if plugin.enabled
        ]
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get plugin system statistics"""
        return {
            "total_plugins": len(self.plugins),
            "enabled_plugins": len(self.get_enabled_plugins()),
            "events_processed": len(self.event_history),
            "queued_events": len(self.event_queue)
        }
    
    def health_check(self) -> bool:
        """Check plugin manager health"""
        return True
    
    def shutdown(self) -> None:
        """Shutdown all plugins"""
        for plugin in self.plugins.values():
            if plugin.enabled:
                plugin.shutdown()


class ModularityFramework:
    """Main modularity framework integrating plugin system and event-driven architecture"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize modularity framework
        
        Args:
            config: Configuration dictionary
        """
        self.config = config or {}
        self.plugin_manager = PluginManager()
        self.api_hooks: Dict[str, List[Callable]] = {}
    
    def initialize(self) -> None:
        """Initialize modularity framework"""
        self.plugin_manager.initialize()
        self._register_core_plugins()
    
    def _register_core_plugins(self) -> None:
        """Register core system plugins"""
        # Example: Analytics plugin
        analytics_plugin = Plugin("analytics", "Analytics Plugin", "1.0.0")
        analytics_plugin.initialize()
        self.plugin_manager.register_plugin(analytics_plugin)
        
        # Example: Logging plugin
        logging_plugin = Plugin("logging", "Logging Plugin", "1.0.0")
        logging_plugin.initialize()
        self.plugin_manager.register_plugin(logging_plugin)
    
    def register_api_hook(self, hook_name: str, callback: Callable) -> None:
        """
        Register an API hook for extensibility
        
        Args:
            hook_name: Name of the hook
            callback: Callback function
        """
        if hook_name not in self.api_hooks:
            self.api_hooks[hook_name] = []
        self.api_hooks[hook_name].append(callback)
    
    def execute_hook(self, hook_name: str, *args, **kwargs) -> List[Any]:
        """
        Execute all callbacks for a hook
        
        Args:
            hook_name: Name of the hook
            *args: Positional arguments
            **kwargs: Keyword arguments
            
        Returns:
            list: Results from all callbacks
        """
        results = []
        
        if hook_name in self.api_hooks:
            for callback in self.api_hooks[hook_name]:
                try:
                    result = callback(*args, **kwargs)
                    results.append(result)
                except Exception as e:
                    results.append({"error": str(e)})
        
        return results
    
    def create_plugin_from_spec(self, spec: Dict[str, Any]) -> Optional[Plugin]:
        """
        Create a plugin from specification
        
        Args:
            spec: Plugin specification dictionary
            
        Returns:
            Plugin: Created plugin or None
        """
        required_fields = ["plugin_id", "name", "version"]
        if not all(field in spec for field in required_fields):
            return None
        
        plugin = Plugin(
            spec["plugin_id"],
            spec["name"],
            spec["version"]
        )
        
        if "dependencies" in spec:
            plugin.dependencies = spec["dependencies"]
        
        return plugin
    
    def get_framework_info(self) -> Dict[str, Any]:
        """Get framework information"""
        return {
            "plugin_statistics": self.plugin_manager.get_statistics(),
            "registered_hooks": list(self.api_hooks.keys()),
            "core_plugins": self.plugin_manager.get_enabled_plugins()
        }
    
    def health_check(self) -> bool:
        """Check framework health"""
        return self.plugin_manager.health_check()
    
    def shutdown(self) -> None:
        """Shutdown modularity framework"""
        self.plugin_manager.shutdown()
