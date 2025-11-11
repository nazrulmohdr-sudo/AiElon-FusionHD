"""
AiElon Living OS - User Interface Module

This module provides intuitive UI components and dashboard framework:
- Dashboard management
- Widget system
- Responsive design utilities
- Theme support
"""

from typing import Dict, Any, List, Optional
from datetime import datetime


class Widget:
    """Base widget class for UI components"""
    
    def __init__(self, widget_id: str, widget_type: str, config: Dict[str, Any] = None):
        """
        Initialize widget
        
        Args:
            widget_id: Unique widget identifier
            widget_type: Type of widget
            config: Widget configuration
        """
        self.widget_id = widget_id
        self.widget_type = widget_type
        self.config = config or {}
        self.visible = True
        self.position = {"x": 0, "y": 0}
        self.size = {"width": 300, "height": 200}
        self.data = {}
    
    def render(self) -> Dict[str, Any]:
        """
        Render widget data
        
        Returns:
            dict: Widget render data
        """
        return {
            "widget_id": self.widget_id,
            "widget_type": self.widget_type,
            "visible": self.visible,
            "position": self.position,
            "size": self.size,
            "config": self.config,
            "data": self.data
        }
    
    def update_data(self, data: Dict[str, Any]) -> None:
        """Update widget data"""
        self.data.update(data)
    
    def set_position(self, x: int, y: int) -> None:
        """Set widget position"""
        self.position = {"x": x, "y": y}
    
    def set_size(self, width: int, height: int) -> None:
        """Set widget size"""
        self.size = {"width": width, "height": height}


class Dashboard:
    """Dashboard container for widgets"""
    
    def __init__(self, dashboard_id: str, title: str, config: Dict[str, Any] = None):
        """
        Initialize dashboard
        
        Args:
            dashboard_id: Unique dashboard identifier
            title: Dashboard title
            config: Dashboard configuration
        """
        self.dashboard_id = dashboard_id
        self.title = title
        self.config = config or {}
        self.widgets: Dict[str, Widget] = {}
        self.layout = "grid"
        self.theme = "light"
        self.created_at = datetime.now().isoformat()
    
    def add_widget(self, widget: Widget) -> bool:
        """
        Add widget to dashboard
        
        Args:
            widget: Widget to add
            
        Returns:
            bool: True if widget added successfully
        """
        if widget.widget_id in self.widgets:
            return False
        
        self.widgets[widget.widget_id] = widget
        return True
    
    def remove_widget(self, widget_id: str) -> bool:
        """
        Remove widget from dashboard
        
        Args:
            widget_id: Widget identifier
            
        Returns:
            bool: True if widget removed successfully
        """
        if widget_id in self.widgets:
            del self.widgets[widget_id]
            return True
        return False
    
    def get_widget(self, widget_id: str) -> Optional[Widget]:
        """Get widget by ID"""
        return self.widgets.get(widget_id)
    
    def render(self) -> Dict[str, Any]:
        """
        Render dashboard
        
        Returns:
            dict: Dashboard render data
        """
        return {
            "dashboard_id": self.dashboard_id,
            "title": self.title,
            "layout": self.layout,
            "theme": self.theme,
            "widgets": [widget.render() for widget in self.widgets.values()],
            "created_at": self.created_at
        }
    
    def set_theme(self, theme: str) -> None:
        """Set dashboard theme"""
        self.theme = theme
    
    def set_layout(self, layout: str) -> None:
        """Set dashboard layout"""
        self.layout = layout


class UIFramework:
    """Main UI framework managing dashboards and widgets"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize UI framework
        
        Args:
            config: Configuration dictionary
        """
        self.config = config or {}
        self.dashboards: Dict[str, Dashboard] = {}
        self.themes = {
            "light": {
                "background": "#ffffff",
                "foreground": "#000000",
                "primary": "#007bff",
                "secondary": "#6c757d",
                "success": "#28a745",
                "warning": "#ffc107",
                "danger": "#dc3545"
            },
            "dark": {
                "background": "#1a1a1a",
                "foreground": "#ffffff",
                "primary": "#0d6efd",
                "secondary": "#6c757d",
                "success": "#198754",
                "warning": "#ffc107",
                "danger": "#dc3545"
            }
        }
    
    def initialize(self) -> None:
        """Initialize UI framework"""
        # Create default dashboard
        self.create_default_dashboard()
    
    def create_default_dashboard(self) -> None:
        """Create default dashboard with essential widgets"""
        main_dashboard = Dashboard("main", "AiElon Living OS - Main Dashboard")
        
        # System status widget
        status_widget = Widget("system_status", "status_display")
        status_widget.set_position(0, 0)
        status_widget.set_size(400, 200)
        status_widget.update_data({
            "title": "System Status",
            "metrics": {
                "cpu_usage": "45%",
                "memory_usage": "62%",
                "disk_usage": "38%",
                "network_status": "Online"
            }
        })
        main_dashboard.add_widget(status_widget)
        
        # AI Analytics widget
        ai_widget = Widget("ai_analytics", "analytics")
        ai_widget.set_position(420, 0)
        ai_widget.set_size(400, 200)
        ai_widget.update_data({
            "title": "AI Analytics",
            "stats": {
                "queries_processed": 1250,
                "accuracy": "95%",
                "active_models": 3
            }
        })
        main_dashboard.add_widget(ai_widget)
        
        # Blockchain status widget
        blockchain_widget = Widget("blockchain_status", "blockchain_display")
        blockchain_widget.set_position(0, 220)
        blockchain_widget.set_size(400, 200)
        blockchain_widget.update_data({
            "title": "AielonChain338 Status",
            "info": {
                "blocks": 1254,
                "transactions": 3421,
                "pending": 5
            }
        })
        main_dashboard.add_widget(blockchain_widget)
        
        # Security overview widget
        security_widget = Widget("security_overview", "security_display")
        security_widget.set_position(420, 220)
        security_widget.set_size(400, 200)
        security_widget.update_data({
            "title": "Security Overview",
            "status": {
                "threat_level": "Low",
                "active_sessions": 12,
                "failed_attempts": 0
            }
        })
        main_dashboard.add_widget(security_widget)
        
        self.dashboards["main"] = main_dashboard
    
    def create_dashboard(self, dashboard_id: str, title: str, 
                        config: Dict[str, Any] = None) -> Dashboard:
        """
        Create a new dashboard
        
        Args:
            dashboard_id: Unique identifier
            title: Dashboard title
            config: Configuration
            
        Returns:
            Dashboard: Created dashboard
        """
        dashboard = Dashboard(dashboard_id, title, config)
        self.dashboards[dashboard_id] = dashboard
        return dashboard
    
    def get_dashboard(self, dashboard_id: str) -> Optional[Dashboard]:
        """Get dashboard by ID"""
        return self.dashboards.get(dashboard_id)
    
    def delete_dashboard(self, dashboard_id: str) -> bool:
        """
        Delete dashboard
        
        Args:
            dashboard_id: Dashboard identifier
            
        Returns:
            bool: True if deleted successfully
        """
        if dashboard_id in self.dashboards:
            del self.dashboards[dashboard_id]
            return True
        return False
    
    def list_dashboards(self) -> List[Dict[str, Any]]:
        """List all dashboards"""
        return [
            {
                "dashboard_id": dashboard.dashboard_id,
                "title": dashboard.title,
                "widget_count": len(dashboard.widgets),
                "theme": dashboard.theme
            }
            for dashboard in self.dashboards.values()
        ]
    
    def get_theme(self, theme_name: str) -> Optional[Dict[str, str]]:
        """Get theme by name"""
        return self.themes.get(theme_name)
    
    def add_theme(self, theme_name: str, theme_config: Dict[str, str]) -> None:
        """Add custom theme"""
        self.themes[theme_name] = theme_config
    
    def create_widget(self, widget_type: str, widget_id: str, 
                     config: Dict[str, Any] = None) -> Widget:
        """
        Create a new widget
        
        Args:
            widget_type: Type of widget
            widget_id: Unique identifier
            config: Widget configuration
            
        Returns:
            Widget: Created widget
        """
        return Widget(widget_id, widget_type, config)
    
    def get_ui_statistics(self) -> Dict[str, Any]:
        """Get UI framework statistics"""
        total_widgets = sum(len(d.widgets) for d in self.dashboards.values())
        
        return {
            "total_dashboards": len(self.dashboards),
            "total_widgets": total_widgets,
            "available_themes": list(self.themes.keys())
        }
    
    def health_check(self) -> bool:
        """Check UI framework health"""
        return True
    
    def shutdown(self) -> None:
        """Shutdown UI framework"""
        pass
