"""
AiElon Living OS - Core System Module

This module provides the main system orchestration and lifecycle management
for the AiElon Living OS platform.
"""

import logging
from typing import Dict, Any, List
from datetime import datetime


class AiElonLivingOS:
    """
    Main system class for AiElon Living OS
    Orchestrates all components and manages system lifecycle
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize AiElon Living OS
        
        Args:
            config: Configuration dictionary for system initialization
        """
        self.config = config or {}
        self.version = "2.0.0"
        self.status = "initialized"
        self.modules: Dict[str, Any] = {}
        self.logger = self._setup_logging()
        self.start_time = datetime.now()
        
    def _setup_logging(self) -> logging.Logger:
        """Setup system-wide logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger('AiElonOS')
    
    def register_module(self, name: str, module: Any) -> None:
        """
        Register a module with the system
        
        Args:
            name: Module name
            module: Module instance
        """
        self.modules[name] = module
        self.logger.info(f"Module '{name}' registered successfully")
    
    def start(self) -> bool:
        """
        Start the AiElon Living OS system
        
        Returns:
            bool: True if system started successfully
        """
        try:
            self.logger.info("Starting AiElon Living OS v" + self.version)
            
            # Initialize all registered modules
            for name, module in self.modules.items():
                if hasattr(module, 'initialize'):
                    module.initialize()
                    self.logger.info(f"Module '{name}' initialized")
            
            self.status = "running"
            self.logger.info("AiElon Living OS started successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to start system: {str(e)}")
            self.status = "error"
            return False
    
    def stop(self) -> None:
        """Stop the AiElon Living OS system"""
        self.logger.info("Stopping AiElon Living OS")
        
        # Shutdown all modules
        for name, module in self.modules.items():
            if hasattr(module, 'shutdown'):
                module.shutdown()
                self.logger.info(f"Module '{name}' shut down")
        
        self.status = "stopped"
        self.logger.info("AiElon Living OS stopped")
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get current system status
        
        Returns:
            dict: System status information
        """
        uptime = (datetime.now() - self.start_time).total_seconds()
        
        return {
            "version": self.version,
            "status": self.status,
            "uptime_seconds": uptime,
            "modules": list(self.modules.keys()),
            "module_count": len(self.modules)
        }
    
    def health_check(self) -> Dict[str, Any]:
        """
        Perform system health check
        
        Returns:
            dict: Health status of system and modules
        """
        health = {
            "system": self.status == "running",
            "modules": {}
        }
        
        for name, module in self.modules.items():
            if hasattr(module, 'health_check'):
                health["modules"][name] = module.health_check()
            else:
                health["modules"][name] = True
        
        return health
