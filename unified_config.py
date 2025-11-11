"""
Unified Configuration System
Centralized configuration management for all AiElon-FusionHD components
"""

import json
from typing import Dict, Any, Optional
from pathlib import Path


class UnifiedConfig:
    """
    Unified configuration manager for entire AiElon-FusionHD ecosystem
    Ensures consistent configuration across all components
    """
    
    DEFAULT_CONFIG = {
        "system": {
            "version": "1.0.0",
            "environment": "production",
            "debug_mode": False,
            "efficiency_target": 1.0
        },
        "fusion_core": {
            "quantum_processor": {
                "enabled": True,
                "coherence_time": 1000,
                "fidelity": 0.999
            },
            "security": {
                "encryption_level": "quantum-resistant",
                "protocols": ["AES-256", "RSA-4096", "SHA-3"],
                "multi_factor_auth": True
            },
            "scalability": {
                "regions": ["us-east", "us-west", "eu-central", "asia-pacific", "middle-east"],
                "auto_scaling": True,
                "load_balancing": "intelligent-distribution"
            },
            "ai_orchestrator": {
                "mode": "unified",
                "learning_rate": 0.001,
                "optimization_enabled": True
            }
        },
        "components": {
            "fusion_hd_ui": {
                "enabled": True,
                "resolution": "8K",
                "refresh_rate": 120,
                "features": ["adaptive_ui", "responsive_design", "multi_language"]
            },
            "halal_wallet": {
                "enabled": True,
                "compliance_standard": "AAOIFI",
                "supported_currencies": ["USD", "EUR", "GBP", "SAR", "AED"],
                "transaction_limit": 1000000
            },
            "hcare": {
                "enabled": True,
                "privacy_standard": "HIPAA",
                "ai_diagnostics": True,
                "telemedicine": True
            },
            "ummah_hub": {
                "enabled": True,
                "global_reach": True,
                "supported_languages": ["ar", "en", "ur", "tr", "id", "ms"],
                "features": [
                    "prayer_times",
                    "qibla_finder", 
                    "islamic_calendar",
                    "community_forum",
                    "charity_platform"
                ]
            }
        },
        "monitoring": {
            "enabled": True,
            "metrics_collection": True,
            "health_checks": True,
            "alert_thresholds": {
                "efficiency_min": 0.99,
                "error_rate_max": 0.01,
                "response_time_max": 1000
            }
        },
        "deployment": {
            "mode": "global",
            "regions_active": 5,
            "disaster_recovery": True,
            "backup_frequency": "hourly"
        }
    }
    
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self.config = self.DEFAULT_CONFIG.copy()
        
        if config_path and Path(config_path).exists():
            self.load_from_file(config_path)
    
    def load_from_file(self, filepath: str):
        """Load configuration from JSON file"""
        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                self._merge_configs(self.config, user_config)
        except Exception as e:
            print(f"Warning: Could not load config from {filepath}: {e}")
    
    def save_to_file(self, filepath: str):
        """Save configuration to JSON file"""
        with open(filepath, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def _merge_configs(self, base: Dict, override: Dict):
        """Recursively merge override config into base config"""
        for key, value in override.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge_configs(base[key], value)
            else:
                base[key] = value
    
    def get(self, key_path: str, default: Any = None) -> Any:
        """
        Get configuration value by dot-separated path
        Example: get("fusion_core.quantum_processor.enabled")
        """
        keys = key_path.split('.')
        value = self.config
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def set(self, key_path: str, value: Any):
        """
        Set configuration value by dot-separated path
        Example: set("fusion_core.quantum_processor.enabled", True)
        """
        keys = key_path.split('.')
        config = self.config
        
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
        
        config[keys[-1]] = value
    
    def validate(self) -> Dict[str, Any]:
        """Validate configuration for correctness"""
        issues = []
        
        # Validate efficiency target
        efficiency_target = self.get("system.efficiency_target", 1.0)
        if not 0.0 <= efficiency_target <= 1.0:
            issues.append("system.efficiency_target must be between 0.0 and 1.0")
        
        # Validate quantum fidelity
        fidelity = self.get("fusion_core.quantum_processor.fidelity", 0.999)
        if not 0.0 <= fidelity <= 1.0:
            issues.append("quantum_processor.fidelity must be between 0.0 and 1.0")
        
        # Validate regions
        regions = self.get("fusion_core.scalability.regions", [])
        if not regions or len(regions) == 0:
            issues.append("At least one region must be configured")
        
        # Validate transaction limit
        tx_limit = self.get("components.halal_wallet.transaction_limit", 0)
        if tx_limit <= 0:
            issues.append("transaction_limit must be positive")
        
        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "config": self.config
        }
    
    def get_all(self) -> Dict[str, Any]:
        """Get entire configuration"""
        return self.config.copy()


# Global configuration instance
_config_instance = None


def get_config(config_path: Optional[str] = None) -> UnifiedConfig:
    """Get or create global configuration instance"""
    global _config_instance
    if _config_instance is None:
        _config_instance = UnifiedConfig(config_path)
    return _config_instance
