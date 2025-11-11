"""
Unit Tests for UI Framework
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from ui.ui_framework import Widget, Dashboard, UIFramework


class TestWidget(unittest.TestCase):
    """Test cases for Widget"""
    
    def test_widget_creation(self):
        """Test widget creation"""
        widget = Widget("widget1", "status_display")
        
        self.assertEqual(widget.widget_id, "widget1")
        self.assertEqual(widget.widget_type, "status_display")
        self.assertTrue(widget.visible)
    
    def test_widget_render(self):
        """Test widget rendering"""
        widget = Widget("widget1", "status_display")
        render_data = widget.render()
        
        self.assertIn("widget_id", render_data)
        self.assertIn("widget_type", render_data)
        self.assertIn("visible", render_data)
    
    def test_widget_position_and_size(self):
        """Test setting widget position and size"""
        widget = Widget("widget1", "status_display")
        widget.set_position(100, 200)
        widget.set_size(400, 300)
        
        self.assertEqual(widget.position, {"x": 100, "y": 200})
        self.assertEqual(widget.size, {"width": 400, "height": 300})


class TestDashboard(unittest.TestCase):
    """Test cases for Dashboard"""
    
    def test_dashboard_creation(self):
        """Test dashboard creation"""
        dashboard = Dashboard("dash1", "Test Dashboard")
        
        self.assertEqual(dashboard.dashboard_id, "dash1")
        self.assertEqual(dashboard.title, "Test Dashboard")
        self.assertEqual(len(dashboard.widgets), 0)
    
    def test_add_widget(self):
        """Test adding widget to dashboard"""
        dashboard = Dashboard("dash1", "Test Dashboard")
        widget = Widget("widget1", "status_display")
        
        result = dashboard.add_widget(widget)
        
        self.assertTrue(result)
        self.assertEqual(len(dashboard.widgets), 1)
        
        # Try adding same widget again
        result = dashboard.add_widget(widget)
        self.assertFalse(result)
    
    def test_remove_widget(self):
        """Test removing widget from dashboard"""
        dashboard = Dashboard("dash1", "Test Dashboard")
        widget = Widget("widget1", "status_display")
        dashboard.add_widget(widget)
        
        result = dashboard.remove_widget("widget1")
        
        self.assertTrue(result)
        self.assertEqual(len(dashboard.widgets), 0)
    
    def test_dashboard_render(self):
        """Test dashboard rendering"""
        dashboard = Dashboard("dash1", "Test Dashboard")
        widget = Widget("widget1", "status_display")
        dashboard.add_widget(widget)
        
        render_data = dashboard.render()
        
        self.assertIn("dashboard_id", render_data)
        self.assertIn("title", render_data)
        self.assertIn("widgets", render_data)
        self.assertEqual(len(render_data["widgets"]), 1)


class TestUIFramework(unittest.TestCase):
    """Test cases for UIFramework"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.ui = UIFramework()
        self.ui.initialize()
    
    def test_initialization(self):
        """Test UI framework initialization"""
        # Should have default dashboard
        self.assertGreater(len(self.ui.dashboards), 0)
        self.assertIn("main", self.ui.dashboards)
    
    def test_create_dashboard(self):
        """Test creating dashboard"""
        dashboard = self.ui.create_dashboard("custom", "Custom Dashboard")
        
        self.assertIsNotNone(dashboard)
        self.assertEqual(dashboard.dashboard_id, "custom")
        self.assertIn("custom", self.ui.dashboards)
    
    def test_get_dashboard(self):
        """Test getting dashboard"""
        dashboard = self.ui.get_dashboard("main")
        
        self.assertIsNotNone(dashboard)
        self.assertEqual(dashboard.dashboard_id, "main")
    
    def test_delete_dashboard(self):
        """Test deleting dashboard"""
        self.ui.create_dashboard("temp", "Temporary Dashboard")
        
        result = self.ui.delete_dashboard("temp")
        
        self.assertTrue(result)
        self.assertNotIn("temp", self.ui.dashboards)
    
    def test_list_dashboards(self):
        """Test listing dashboards"""
        dashboards = self.ui.list_dashboards()
        
        self.assertIsInstance(dashboards, list)
        self.assertGreater(len(dashboards), 0)
    
    def test_themes(self):
        """Test theme management"""
        # Get existing theme
        light_theme = self.ui.get_theme("light")
        self.assertIsNotNone(light_theme)
        self.assertIn("background", light_theme)
        
        # Add custom theme
        custom_theme = {"background": "#123456", "foreground": "#fedcba"}
        self.ui.add_theme("custom", custom_theme)
        
        retrieved_theme = self.ui.get_theme("custom")
        self.assertEqual(retrieved_theme, custom_theme)
    
    def test_create_widget(self):
        """Test creating widget"""
        widget = self.ui.create_widget("chart", "chart1", {"type": "line"})
        
        self.assertIsNotNone(widget)
        self.assertEqual(widget.widget_id, "chart1")
        self.assertEqual(widget.widget_type, "chart")
    
    def test_ui_statistics(self):
        """Test getting UI statistics"""
        stats = self.ui.get_ui_statistics()
        
        self.assertIn("total_dashboards", stats)
        self.assertIn("total_widgets", stats)
        self.assertGreater(stats["total_dashboards"], 0)


if __name__ == '__main__':
    unittest.main()
