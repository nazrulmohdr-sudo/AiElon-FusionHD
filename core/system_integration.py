#!/usr/bin/env python3
"""
System Integration Layer
Integrates all AiElon FusionHD subsystems
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.aielon_living_os import AiElonLivingOS
from modules.aielon_chain338 import AiElonChain338
from modules.trade138 import Trade138
from modules.bank_compliance import BankCompliance
from modules.quantum_memory_field import QuantumMemoryField
from modules.firewall import FirewallLayer
from modules.hcare_stability import HCareStability, MetricType

import logging
import json
from typing import Dict, Any


class AiElonFusionHD:
    """
    AiElon FusionHD Integration Layer
    Integrates all subsystems for unified operation
    """
    
    def __init__(self):
        self.logger = logging.getLogger('AiElonFusionHD')
        
        # Initialize Living OS
        self.living_os = AiElonLivingOS()
        
        # Initialize all subsystems
        self.blockchain = AiElonChain338()
        self.trading = Trade138()
        self.compliance = BankCompliance()
        self.memory = QuantumMemoryField(capacity_mb=2048)
        self.firewall = FirewallLayer()
        self.hcare = HCareStability()
        
        # Register subsystems with Living OS
        self._register_all_subsystems()
        
        self.logger.info("AiElon FusionHD Integration Layer initialized")
    
    def _register_all_subsystems(self):
        """Register all subsystems with the Living OS"""
        self.living_os.register_subsystem('AiElonChain338', self.blockchain)
        self.living_os.register_subsystem('Trade138', self.trading)
        self.living_os.register_subsystem('BankCompliance', self.compliance)
        self.living_os.register_subsystem('QuantumMemoryField', self.memory)
        self.living_os.register_subsystem('FirewallLayer', self.firewall)
        self.living_os.register_subsystem('HCareStability', self.hcare)
        
        self.logger.info("All subsystems registered")
    
    def start(self) -> bool:
        """Start the complete AiElon FusionHD system"""
        self.logger.info("=" * 60)
        self.logger.info("Starting AiElon FusionHD System")
        self.logger.info("=" * 60)
        
        # Start Living OS (initializes all subsystems)
        if self.living_os.start():
            self.logger.info("✓ AiElon FusionHD started successfully")
            self._display_system_status()
            return True
        else:
            self.logger.error("✗ Failed to start AiElon FusionHD")
            return False
    
    def _display_system_status(self):
        """Display comprehensive system status"""
        status = self.living_os.get_system_status()
        
        self.logger.info("")
        self.logger.info("System Status:")
        self.logger.info(f"  Version: {status['version']}")
        self.logger.info(f"  Status: {status['status']}")
        self.logger.info(f"  Operational Readiness: {status['operational_readiness']}%")
        self.logger.info(f"  Error Count: {status['error_count']}")
        self.logger.info(f"  Eternal Truth Lock: {status['eternal_truth_lock']}")
        self.logger.info("")
        self.logger.info("Subsystems:")
        for name, subsystem_status in status['subsystems'].items():
            self.logger.info(f"  ✓ {name}: {subsystem_status}")
        self.logger.info("")
    
    def perform_integrated_health_check(self) -> Dict[str, Any]:
        """Perform integrated health check across all systems"""
        self.logger.info("Performing integrated health check...")
        
        # Get Living OS health report
        os_health = self.living_os.health_check()
        
        # Get HCare system health summary
        hcare_summary = self.hcare.get_system_health_summary()
        
        # Record metrics for all subsystems
        for subsystem_name, subsystem_data in os_health['subsystems'].items():
            # Record operational status as a metric
            operational_metric = 100.0 if subsystem_data.get('status') == 'operational' else 0.0
            self.hcare.record_metric(
                MetricType.ERROR_RATE,
                100.0 - operational_metric,
                subsystem_name
            )
        
        integrated_report = {
            'living_os': os_health,
            'hcare_summary': hcare_summary,
            'timestamp': os_health['timestamp']
        }
        
        self.logger.info("Health check completed")
        return integrated_report
    
    def demonstrate_integrated_operations(self):
        """Demonstrate integrated operations across subsystems"""
        self.logger.info("")
        self.logger.info("=" * 60)
        self.logger.info("Demonstrating Integrated Operations")
        self.logger.info("=" * 60)
        
        # 1. Blockchain Operation
        self.logger.info("\n1. Blockchain Transaction:")
        self.blockchain.add_transaction({
            'from': 'Alice',
            'to': 'Bob',
            'amount': 100,
            'asset': 'AEC'
        })
        self.blockchain.mine_pending_transactions('System')
        chain_info = self.blockchain.get_chain_info()
        self.logger.info(f"   Chain length: {chain_info['length']}")
        self.logger.info(f"   Chain valid: {chain_info['valid']}")
        
        # 2. Compliance Check
        self.logger.info("\n2. Bank Compliance:")
        from modules.bank_compliance import ComplianceStatus
        kyc_status = self.compliance.register_user_kyc('user001', {
            'full_name': 'Alice Johnson',
            'date_of_birth': '1990-01-01',
            'address': '123 Blockchain Ave',
            'id_number': 'KYC001',
            'country': 'USA'
        })
        self.logger.info(f"   KYC Status: {kyc_status.value}")
        
        # 3. Trading Operation
        self.logger.info("\n3. Trading Operation:")
        from decimal import Decimal
        from modules.trade138 import OrderType
        order_id = self.trading.place_order(
            'user001',
            OrderType.MARKET,
            'AEC',
            Decimal('10.0')
        )
        self.logger.info(f"   Order placed: {order_id}")
        stats = self.trading.get_trade_statistics()
        self.logger.info(f"   Total orders: {stats['total_orders']}")
        
        # 4. Memory Storage
        self.logger.info("\n4. Quantum Memory Field:")
        self.memory.store('user001_data', {
            'user_id': 'user001',
            'portfolio': self.trading.get_portfolio('user001')
        })
        mem_stats = self.memory.get_memory_statistics()
        self.logger.info(f"   Total blocks: {mem_stats['total_blocks']}")
        self.logger.info(f"   Cache hit rate: {mem_stats['cache_hit_rate']}")
        
        # 5. Firewall Protection
        self.logger.info("\n5. Firewall Security:")
        test_request = {
            'source_ip': '192.168.1.100',
            'endpoint': '/api/trade',
            'payload': 'normal trading request'
        }
        allowed, threat, reason = self.firewall.validate_request(test_request)
        self.logger.info(f"   Request allowed: {allowed}")
        self.logger.info(f"   Threat level: {threat.value}")
        
        # 6. Health Monitoring
        self.logger.info("\n6. System Health:")
        health_summary = self.hcare.get_system_health_summary()
        self.logger.info(f"   Overall health: {health_summary['overall_status']}")
        self.logger.info(f"   Total alerts: {health_summary['total_alerts']}")
        
        self.logger.info("")
        self.logger.info("=" * 60)
    
    def get_comprehensive_report(self) -> Dict[str, Any]:
        """Generate comprehensive system report"""
        return {
            'system_status': self.living_os.get_system_status(),
            'blockchain': self.blockchain.get_chain_info(),
            'trading': self.trading.get_trade_statistics(),
            'compliance': self.compliance.get_compliance_report(),
            'memory': self.memory.get_memory_statistics(),
            'security': self.firewall.get_security_statistics(),
            'health': self.hcare.get_diagnostics()
        }
    
    def save_report(self, filename: str = 'system_report.json'):
        """Save comprehensive report to file"""
        try:
            report = self.get_comprehensive_report()
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2, default=str)
            self.logger.info(f"Report saved to {filename}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to save report: {e}")
            return False


def main():
    """Main entry point"""
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Initialize and start AiElon FusionHD
    fusion_hd = AiElonFusionHD()
    
    if fusion_hd.start():
        # Demonstrate integrated operations
        fusion_hd.demonstrate_integrated_operations()
        
        # Perform health check
        fusion_hd.perform_integrated_health_check()
        
        # Save comprehensive report
        fusion_hd.save_report('/home/runner/work/AiElon-FusionHD/AiElon-FusionHD/system_report.json')
        
        # Display final status
        status = fusion_hd.living_os.get_system_status()
        
        print("\n" + "=" * 60)
        print("AiElon FusionHD System - Final Status")
        print("=" * 60)
        print(f"Operational Readiness: {status['operational_readiness']}%")
        print(f"Error Count: {status['error_count']}")
        print(f"Eternal Truth Lock: {'✓ ENGAGED' if status['eternal_truth_lock'] else '✗ NOT ENGAGED'}")
        print("=" * 60)
        
        return 0 if status['operational_readiness'] == 100.0 and status['error_count'] == 0 else 1
    else:
        print("Failed to start AiElon FusionHD")
        return 1


if __name__ == "__main__":
    exit(main())
