#!/usr/bin/env python3
"""
HCare Stability Modules
Health monitoring and system stability management
"""

import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from enum import Enum
import time


class HealthStatus(Enum):
    """Health status enumeration"""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    CRITICAL = "critical"


class MetricType(Enum):
    """Metric type enumeration"""
    CPU = "cpu"
    MEMORY = "memory"
    DISK = "disk"
    NETWORK = "network"
    RESPONSE_TIME = "response_time"
    ERROR_RATE = "error_rate"


class HCareStability:
    """
    HCare Stability Modules
    Monitors system health, performs diagnostics, and ensures stability
    """
    
    def __init__(self):
        self.metrics: Dict[str, List[Dict[str, Any]]] = {}
        self.alerts: List[Dict[str, Any]] = []
        self.health_history: List[Dict[str, Any]] = []
        self.auto_recovery_enabled = True
        self.logger = logging.getLogger('HCareStability')
        
        # Thresholds
        self.thresholds = {
            MetricType.CPU: 80.0,
            MetricType.MEMORY: 85.0,
            MetricType.DISK: 90.0,
            MetricType.RESPONSE_TIME: 1000.0,  # milliseconds
            MetricType.ERROR_RATE: 5.0  # percentage
        }
        
        # Recovery strategies
        self.recovery_actions: Dict[str, Any] = {}
        
        self.logger.info("HCare Stability Modules initialized")
    
    def record_metric(self, metric_type: MetricType, value: float, 
                     component: str = "system") -> bool:
        """Record a system metric"""
        try:
            metric_key = f"{component}_{metric_type.value}"
            
            if metric_key not in self.metrics:
                self.metrics[metric_key] = []
            
            metric_entry = {
                'timestamp': datetime.now().isoformat(),
                'type': metric_type.value,
                'component': component,
                'value': value,
                'threshold': self.thresholds.get(metric_type)
            }
            
            self.metrics[metric_key].append(metric_entry)
            
            # Keep only last 1000 entries per metric
            if len(self.metrics[metric_key]) > 1000:
                self.metrics[metric_key] = self.metrics[metric_key][-1000:]
            
            # Check if threshold exceeded
            threshold = self.thresholds.get(metric_type)
            if threshold and value > threshold:
                self._trigger_alert(metric_type, component, value, threshold)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to record metric: {e}")
            return False
    
    def _trigger_alert(self, metric_type: MetricType, component: str, 
                      value: float, threshold: float):
        """Trigger an alert for threshold violation"""
        alert = {
            'timestamp': datetime.now().isoformat(),
            'metric_type': metric_type.value,
            'component': component,
            'value': value,
            'threshold': threshold,
            'severity': self._calculate_severity(value, threshold),
            'acknowledged': False
        }
        
        self.alerts.append(alert)
        self.logger.warning(
            f"Alert: {metric_type.value} threshold exceeded for {component}. "
            f"Value: {value}, Threshold: {threshold}"
        )
        
        # Attempt auto-recovery if enabled
        if self.auto_recovery_enabled:
            self._attempt_recovery(metric_type, component)
    
    def _calculate_severity(self, value: float, threshold: float) -> str:
        """Calculate alert severity"""
        ratio = value / threshold
        
        if ratio >= 2.0:
            return "critical"
        elif ratio >= 1.5:
            return "high"
        elif ratio >= 1.2:
            return "medium"
        else:
            return "low"
    
    def _attempt_recovery(self, metric_type: MetricType, component: str):
        """Attempt automatic recovery"""
        try:
            self.logger.info(f"Attempting recovery for {component} ({metric_type.value})")
            
            # Recovery strategies based on metric type
            if metric_type == MetricType.MEMORY:
                self._clear_caches(component)
            elif metric_type == MetricType.CPU:
                self._optimize_processes(component)
            elif metric_type == MetricType.ERROR_RATE:
                self._restart_component(component)
            
            self.logger.info(f"Recovery attempted for {component}")
            
        except Exception as e:
            self.logger.error(f"Recovery failed: {e}")
    
    def _clear_caches(self, component: str):
        """Clear component caches"""
        self.logger.info(f"Clearing caches for {component}")
        # Placeholder for actual cache clearing logic
    
    def _optimize_processes(self, component: str):
        """Optimize component processes"""
        self.logger.info(f"Optimizing processes for {component}")
        # Placeholder for actual optimization logic
    
    def _restart_component(self, component: str):
        """Restart component"""
        self.logger.info(f"Restarting component: {component}")
        # Placeholder for actual restart logic
    
    def perform_health_check(self, component: str) -> Dict[str, Any]:
        """Perform comprehensive health check on a component"""
        try:
            health_status = HealthStatus.HEALTHY
            issues = []
            metrics_summary = {}
            
            # Check recent metrics for this component
            for metric_key, metric_list in self.metrics.items():
                if component in metric_key and metric_list:
                    recent_metric = metric_list[-1]
                    value = recent_metric['value']
                    threshold = recent_metric.get('threshold')
                    
                    metrics_summary[recent_metric['type']] = {
                        'value': value,
                        'threshold': threshold,
                        'status': 'normal' if not threshold or value <= threshold else 'exceeded'
                    }
                    
                    if threshold and value > threshold:
                        issues.append(f"{recent_metric['type']} threshold exceeded")
                        health_status = HealthStatus.DEGRADED
                        
                        if value > threshold * 1.5:
                            health_status = HealthStatus.UNHEALTHY
                        if value > threshold * 2.0:
                            health_status = HealthStatus.CRITICAL
            
            health_report = {
                'component': component,
                'status': health_status.value,
                'timestamp': datetime.now().isoformat(),
                'metrics': metrics_summary,
                'issues': issues,
                'recent_alerts': self._get_recent_alerts(component, hours=1)
            }
            
            # Record health check
            self.health_history.append(health_report)
            
            return health_report
            
        except Exception as e:
            self.logger.error(f"Health check failed for {component}: {e}")
            return {
                'component': component,
                'status': HealthStatus.CRITICAL.value,
                'error': str(e)
            }
    
    def _get_recent_alerts(self, component: str, hours: int = 1) -> List[Dict[str, Any]]:
        """Get recent alerts for a component"""
        cutoff_time = datetime.now() - timedelta(hours=hours)
        
        recent_alerts = []
        for alert in self.alerts:
            if alert['component'] == component:
                alert_time = datetime.fromisoformat(alert['timestamp'])
                if alert_time > cutoff_time:
                    recent_alerts.append(alert)
        
        return recent_alerts
    
    def get_system_health_summary(self) -> Dict[str, Any]:
        """Get overall system health summary"""
        try:
            # Get unique components
            components = set()
            for metric_key in self.metrics.keys():
                component = metric_key.split('_')[0]
                components.add(component)
            
            # Check health for each component
            component_health = {}
            overall_status = HealthStatus.HEALTHY
            
            for component in components:
                health = self.perform_health_check(component)
                component_health[component] = health['status']
                
                # Update overall status
                if health['status'] == HealthStatus.CRITICAL.value:
                    overall_status = HealthStatus.CRITICAL
                elif health['status'] == HealthStatus.UNHEALTHY.value and overall_status != HealthStatus.CRITICAL:
                    overall_status = HealthStatus.UNHEALTHY
                elif health['status'] == HealthStatus.DEGRADED.value and overall_status == HealthStatus.HEALTHY:
                    overall_status = HealthStatus.DEGRADED
            
            return {
                'overall_status': overall_status.value,
                'timestamp': datetime.now().isoformat(),
                'components': component_health,
                'total_alerts': len(self.alerts),
                'unacknowledged_alerts': sum(1 for a in self.alerts if not a['acknowledged']),
                'auto_recovery_enabled': self.auto_recovery_enabled
            }
            
        except Exception as e:
            self.logger.error(f"Failed to get health summary: {e}")
            return {
                'overall_status': HealthStatus.CRITICAL.value,
                'error': str(e)
            }
    
    def acknowledge_alert(self, alert_index: int) -> bool:
        """Acknowledge an alert"""
        try:
            if 0 <= alert_index < len(self.alerts):
                self.alerts[alert_index]['acknowledged'] = True
                self.alerts[alert_index]['acknowledged_at'] = datetime.now().isoformat()
                self.logger.info(f"Alert {alert_index} acknowledged")
                return True
            return False
        except Exception as e:
            self.logger.error(f"Failed to acknowledge alert: {e}")
            return False
    
    def get_diagnostics(self) -> Dict[str, Any]:
        """Get comprehensive diagnostics"""
        return {
            'total_metrics': sum(len(m) for m in self.metrics.values()),
            'total_alerts': len(self.alerts),
            'health_checks': len(self.health_history),
            'auto_recovery_enabled': self.auto_recovery_enabled,
            'thresholds': {mt.value: th for mt, th in self.thresholds.items()}
        }
    
    def initialize(self):
        """Initialize HCare Stability"""
        self.logger.info("HCare Stability initialized")
    
    def health_check(self) -> Dict[str, Any]:
        """Perform health check"""
        summary = self.get_system_health_summary()
        return {
            'status': 'operational',
            'overall_health': summary['overall_status'],
            'total_alerts': summary['total_alerts'],
            'components_monitored': len(summary.get('components', {}))
        }


if __name__ == "__main__":
    # Test HCare Stability
    hcare = HCareStability()
    hcare.record_metric(MetricType.CPU, 45.5, "trade138")
    hcare.record_metric(MetricType.MEMORY, 70.0, "blockchain")
    summary = hcare.get_system_health_summary()
    print(f"System health: {summary}")
