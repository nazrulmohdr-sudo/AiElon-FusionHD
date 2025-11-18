"""
System Monitoring and Health Checks
Real-time metrics, alerting, and health monitoring
"""

import logging
from typing import Dict, Any, List
from datetime import datetime
import time


class MonitoringSystem:
    """System monitoring and health check manager"""
    
    def __init__(self, config: Dict[str, Any]):
        self.logger = logging.getLogger('Monitoring')
        self.health_check_config = config.get('healthCheck', {})
        self.metrics_config = config.get('metrics', {})
        self.alerting_config = config.get('alerting', {})
        
        self.metrics = {
            'cpu_usage': [],
            'memory_usage': [],
            'response_time': [],
            'error_rate': []
        }
        self.alerts = []
        self.health_status = {}
        
    def initialize(self) -> bool:
        """Initialize monitoring system"""
        self.logger.info("Initializing monitoring system")
        self.logger.info(f"Health check interval: {self.health_check_config.get('interval')}s")
        self.logger.info(f"Real-time metrics: {self.metrics_config.get('enabled')}")
        self.logger.info(f"Alerting enabled: {self.alerting_config.get('enabled')}")
        return True
    
    def record_metric(self, metric_name: str, value: float):
        """Record a metric value"""
        if metric_name not in self.metrics:
            self.metrics[metric_name] = []
        
        self.metrics[metric_name].append({
            'timestamp': datetime.now().isoformat(),
            'value': value
        })
        
        # Keep only last 1000 entries per metric
        if len(self.metrics[metric_name]) > 1000:
            self.metrics[metric_name] = self.metrics[metric_name][-1000:]
        
        # Check for alerts
        self._check_thresholds(metric_name, value)
    
    def _check_thresholds(self, metric_name: str, value: float):
        """Check if metric exceeds thresholds"""
        thresholds = {
            'cpu_usage': 80,
            'memory_usage': 85,
            'response_time': 1000,
            'error_rate': 5
        }
        
        if metric_name in thresholds and value > thresholds[metric_name]:
            self._create_alert(
                severity='warning',
                message=f"{metric_name} exceeded threshold: {value}"
            )
    
    def _create_alert(self, severity: str, message: str):
        """Create system alert"""
        if not self.alerting_config.get('enabled', False):
            return
        
        alert = {
            'id': f"alert_{len(self.alerts) + 1}",
            'timestamp': datetime.now().isoformat(),
            'severity': severity,
            'message': message,
            'status': 'active'
        }
        
        self.alerts.append(alert)
        self.logger.warning(f"Alert created: {message}")
        
        # Send to configured channels
        channels = self.alerting_config.get('channels', [])
        for channel in channels:
            self.logger.info(f"Sending alert via {channel}")
    
    def health_check(self, subsystems: Dict[str, Any]) -> Dict[str, Any]:
        """Perform health check on all subsystems"""
        self.logger.info("Performing health check")
        
        results = {
            'timestamp': datetime.now().isoformat(),
            'overall_health': 100,
            'subsystems': {}
        }
        
        for name, subsystem in subsystems.items():
            health = subsystem.get('health', 100)
            results['subsystems'][name] = {
                'health': health,
                'status': 'healthy' if health == 100 else 'degraded'
            }
            
            if health < 100:
                results['overall_health'] = min(results['overall_health'], health)
        
        self.health_status = results
        return results
    
    def get_metrics(self, metric_name: str = None, limit: int = 100) -> Dict[str, Any]:
        """Get recorded metrics"""
        if metric_name:
            return {metric_name: self.metrics.get(metric_name, [])[-limit:]}
        
        return {
            name: values[-limit:]
            for name, values in self.metrics.items()
        }
    
    def get_alerts(self, status: str = 'active', limit: int = 50) -> List[Dict[str, Any]]:
        """Get system alerts"""
        filtered = [
            alert for alert in self.alerts
            if alert['status'] == status
        ]
        return filtered[-limit:]
    
    def get_status(self) -> Dict[str, Any]:
        """Get monitoring system status"""
        return {
            'health_checks_enabled': self.health_check_config.get('enabled'),
            'metrics_collected': sum(len(values) for values in self.metrics.values()),
            'active_alerts': len([a for a in self.alerts if a['status'] == 'active']),
            'health': 100
        }
