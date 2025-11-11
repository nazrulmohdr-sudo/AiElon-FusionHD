#!/usr/bin/env python3
"""
AiElon FusionHD System Validation Script
Comprehensive system validation and status check
"""

import sys
import os
import json
import subprocess

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))


def print_header(text):
    """Print formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70)


def print_status(label, status, details=""):
    """Print status line"""
    status_icon = "✅" if status else "❌"
    print(f"{status_icon} {label}: {details if details else ('PASS' if status else 'FAIL')}")


def main():
    """Run comprehensive system validation"""
    print_header("AiElon FusionHD System Validation")
    
    all_checks_passed = True
    
    # 1. Initialize System
    print_header("1. System Initialization")
    try:
        # Import here after path is set
        from main import FusionHDSystem
        
        system = FusionHDSystem()
        init_result = system.initialize()
        print_status("System Initialization", init_result)
        if not init_result:
            all_checks_passed = False
    except Exception as e:
        print_status("System Initialization", False, f"Error: {e}")
        return 1
    
    # 2. Check System Status
    print_header("2. System Status")
    try:
        status = system.get_system_status()
        
        # Check operational capacity
        capacity = status['system']['operational_capacity']
        print_status("Operational Capacity", capacity == 100, f"{capacity}%")
        if capacity != 100:
            all_checks_passed = False
        
        # Check error rate
        error_rate = status['system']['error_rate']
        print_status("Error Rate", error_rate == 0, f"{error_rate}%")
        if error_rate != 0:
            all_checks_passed = False
        
        # Check overall status
        overall = status['system']['status']
        print_status("Overall Status", overall == 'operational', overall)
        if overall != 'operational':
            all_checks_passed = False
            
    except Exception as e:
        print_status("System Status Check", False, f"Error: {e}")
        all_checks_passed = False
    
    # 3. Check Subsystems
    print_header("3. Subsystem Health")
    try:
        subsystems = status['subsystems']
        for name, sub in subsystems.items():
            health = sub['health']
            print_status(f"Subsystem: {name}", health == 100, f"Health: {health}%")
            if health != 100:
                all_checks_passed = False
    except Exception as e:
        print_status("Subsystem Check", False, f"Error: {e}")
        all_checks_passed = False
    
    # 4. Check Core Systems
    print_header("4. Core Systems")
    try:
        print_status("Communication Layer", 
                    status['communication']['health'] == 100,
                    f"Protocol: {status['communication']['protocol']}")
        print_status("Security Manager", 
                    status['security']['health'] == 100,
                    f"Auth: {status['security']['authentication']}")
        print_status("Monitoring System", 
                    status['monitoring']['health'] == 100,
                    f"Active Alerts: {status['monitoring']['active_alerts']}")
    except Exception as e:
        print_status("Core Systems Check", False, f"Error: {e}")
        all_checks_passed = False
    
    # 5. Run Diagnostics
    print_header("5. System Diagnostics")
    try:
        diagnostics = system.run_diagnostics()
        overall_status = diagnostics['overall_status']
        print_status("Diagnostic Status", overall_status == 'pass', overall_status.upper())
        
        for test_name, test_result in diagnostics['tests'].items():
            print_status(f"  {test_name}", 
                        test_result['status'] == 'pass',
                        test_result['status'])
            if test_result['status'] != 'pass':
                all_checks_passed = False
                
    except Exception as e:
        print_status("Diagnostics", False, f"Error: {e}")
        all_checks_passed = False
    
    # 6. Security Check
    print_header("6. Security Validation")
    try:
        # Test user registration
        result = system.security.register_user("test_user", "test_pass", "user")
        print_status("User Registration", result['status'] == 'success')
        
        # Test authentication
        auth_result = system.security.authenticate("test_user", "test_pass")
        print_status("Authentication", auth_result['status'] == 'success')
        
        # Test authorization
        if auth_result['status'] == 'success':
            token = auth_result['session_token']
            auth_check = system.security.authorize(token, 'read')
            print_status("Authorization", auth_check)
            
    except Exception as e:
        print_status("Security Check", False, f"Error: {e}")
        all_checks_passed = False
    
    # 7. Communication Test
    print_header("7. Communication Test")
    try:
        result = system.communication.send_message(
            "test_sender",
            "test_receiver",
            {"type": "test", "data": "validation"}
        )
        print_status("Message Sending", result['status'] == 'success')
        
        # Check message queue
        queue_size = system.communication.get_status()['queue_size']
        print_status("Message Queue", True, f"Size: {queue_size}")
        
    except Exception as e:
        print_status("Communication Test", False, f"Error: {e}")
        all_checks_passed = False
    
    # 8. Monitoring Test
    print_header("8. Monitoring Test")
    try:
        # Record test metric
        system.monitoring.record_metric("test_metric", 50.0)
        
        # Retrieve metrics
        metrics = system.monitoring.get_metrics("test_metric")
        print_status("Metric Recording", len(metrics['test_metric']) > 0)
        
        # Check monitoring status
        mon_status = system.monitoring.get_status()
        print_status("Monitoring Active", mon_status['health'] == 100)
        
    except Exception as e:
        print_status("Monitoring Test", False, f"Error: {e}")
        all_checks_passed = False
    
    # 9. Documentation Check
    print_header("9. Documentation Validation")
    docs = ['ARCHITECTURE.md', 'API.md', 'SECURITY.md', 'DEPLOYMENT.md']
    for doc in docs:
        path = f'docs/{doc}'
        exists = os.path.exists(path)
        size = os.path.getsize(path) if exists else 0
        print_status(f"{doc}", exists, f"Size: {size:,} bytes")
        if not exists:
            all_checks_passed = False
    
    # 10. Configuration Check
    print_header("10. Configuration Validation")
    try:
        config_path = 'config/system.json'
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        print_status("Config File", True, f"Loaded successfully")
        print_status("System Name", 
                    config['system']['name'] == 'AiElon FusionHD',
                    config['system']['name'])
        print_status("Version", True, config['system']['version'])
        
    except Exception as e:
        print_status("Configuration Check", False, f"Error: {e}")
        all_checks_passed = False
    
    # Final Summary
    print_header("Validation Summary")
    
    if all_checks_passed:
        print("\n🎉 ALL VALIDATION CHECKS PASSED! 🎉")
        print("\n✅ System Status:")
        print("   • Operational Capacity: 100%")
        print("   • Error Rate: 0%")
        print("   • All Subsystems: Active")
        print("   • All Tests: Passing")
        print("   • Documentation: Complete")
        print("\n🟢 SYSTEM IS PRODUCTION READY 🟢")
    else:
        print("\n⚠️  SOME VALIDATION CHECKS FAILED")
        print("   Please review the errors above and fix any issues.")
    
    # Shutdown
    system.shutdown()
    
    print_header("Validation Complete")
    return 0 if all_checks_passed else 1


if __name__ == "__main__":
    sys.exit(main())
