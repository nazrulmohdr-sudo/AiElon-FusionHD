"""
AiElon FusionHD Integrated System
Main orchestrator integrating all subsystems with communication, security, and monitoring
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import json
import logging
from typing import Dict, Any

from core.system import SystemCore
from core.communication.layer import CommunicationLayer
from core.security.manager import SecurityManager
from core.monitoring.system import MonitoringSystem

# Import subsystems with proper path handling
import importlib.util
import os

def load_module(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Get the base directory
base_dir = os.path.dirname(os.path.dirname(__file__))
subsystems_dir = os.path.join(base_dir, 'src', 'subsystems')

# Load subsystem modules
aielon_module = load_module('aielon_os', os.path.join(subsystems_dir, 'aielon', 'os.py'))
fusionui_module = load_module('fusion_ui', os.path.join(subsystems_dir, 'fusion-ui', 'ui.py'))
wallet_module = load_module('halal_wallet', os.path.join(subsystems_dir, 'halal-wallet', 'wallet.py'))
hcare_module = load_module('hcare', os.path.join(subsystems_dir, 'hcare', 'health.py'))
ummahhub_module = load_module('ummah_hub', os.path.join(subsystems_dir, 'ummah-hub', 'hub.py'))

AiElonOS = aielon_module.AiElonOS
FusionUI = fusionui_module.FusionUI
HalalWallet = wallet_module.HalalWallet
HCare = hcare_module.HCare
UmmahHub = ummahhub_module.UmmahHub


class FusionHDSystem:
    """Integrated AiElon FusionHD System"""
    
    def __init__(self, config_path: str = "config/system.json"):
        self.logger = logging.getLogger('FusionHD-System')
        self.core = SystemCore(config_path)
        
        # Initialize core systems
        comm_config = self.core.config.get('communication', {})
        security_config = self.core.config.get('security', {})
        monitoring_config = self.core.config.get('monitoring', {})
        
        self.communication = CommunicationLayer(comm_config)
        self.security = SecurityManager(security_config)
        self.monitoring = MonitoringSystem(monitoring_config)
        
        # Initialize subsystems
        self.subsystems = {
            'aielon': AiElonOS(),
            'fusion_ui': FusionUI(),
            'halal_wallet': HalalWallet(),
            'hcare': HCare(),
            'ummah_hub': UmmahHub()
        }
        
        self.initialized = False
    
    def initialize(self) -> bool:
        """Initialize entire system"""
        self.logger.info("="*60)
        self.logger.info("Initializing AiElon FusionHD Integrated System")
        self.logger.info("="*60)
        
        try:
            # Initialize core
            if not self.core.initialize():
                return False
            
            # Initialize communication layer
            if not self.communication.initialize():
                return False
            
            # Initialize security
            if not self.security.initialize():
                return False
            
            # Initialize monitoring
            if not self.monitoring.initialize():
                return False
            
            # Initialize all subsystems
            for name, subsystem in self.subsystems.items():
                self.logger.info(f"Initializing subsystem: {name}")
                if not subsystem.initialize():
                    self.logger.error(f"Failed to initialize {name}")
                    return False
            
            self.initialized = True
            self.logger.info("="*60)
            self.logger.info("System initialization complete - 100% operational")
            self.logger.info("="*60)
            
            return True
            
        except Exception as e:
            self.logger.error(f"System initialization failed: {e}")
            return False
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        if not self.initialized:
            return {'status': 'not_initialized'}
        
        status = {
            'system': self.core.get_system_status(),
            'communication': self.communication.get_status(),
            'security': self.security.get_status(),
            'monitoring': self.monitoring.get_status(),
            'subsystems': {}
        }
        
        for name, subsystem in self.subsystems.items():
            status['subsystems'][name] = subsystem.get_status()
        
        # Perform health check
        health_result = self.monitoring.health_check(self.core.subsystems)
        status['health_check'] = health_result
        
        return status
    
    def run_diagnostics(self) -> Dict[str, Any]:
        """Run full system diagnostics"""
        self.logger.info("Running system diagnostics...")
        
        diagnostics = {
            'timestamp': self.monitoring.health_status.get('timestamp', ''),
            'tests': {},
            'overall_status': 'pass'
        }
        
        # Test each subsystem
        tests = [
            ('core_system', lambda: self.core.health_check()),
            ('communication', lambda: self.communication.get_status()['health'] == 100),
            ('security', lambda: self.security.get_status()['health'] == 100),
            ('monitoring', lambda: self.monitoring.get_status()['health'] == 100)
        ]
        
        for test_name, test_func in tests:
            try:
                result = test_func()
                diagnostics['tests'][test_name] = {
                    'status': 'pass' if result else 'fail',
                    'result': result
                }
                if not result:
                    diagnostics['overall_status'] = 'fail'
            except Exception as e:
                diagnostics['tests'][test_name] = {
                    'status': 'error',
                    'error': str(e)
                }
                diagnostics['overall_status'] = 'fail'
        
        self.logger.info(f"Diagnostics complete: {diagnostics['overall_status']}")
        return diagnostics
    
    def shutdown(self):
        """Gracefully shutdown system"""
        self.logger.info("Shutting down AiElon FusionHD System...")
        self.core.shutdown()
        self.logger.info("System shutdown complete")


def main():
    """Main entry point"""
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create and initialize system
    system = FusionHDSystem()
    
    if not system.initialize():
        print("System initialization failed!")
        return 1
    
    # Get and display status
    status = system.get_system_status()
    print("\n" + "="*60)
    print("SYSTEM STATUS")
    print("="*60)
    print(json.dumps(status, indent=2))
    
    # Run diagnostics
    print("\n" + "="*60)
    print("RUNNING DIAGNOSTICS")
    print("="*60)
    diagnostics = system.run_diagnostics()
    print(json.dumps(diagnostics, indent=2))
    
    # Shutdown
    system.shutdown()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
