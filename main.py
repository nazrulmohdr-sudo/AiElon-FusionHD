#!/usr/bin/env python3
"""
AiElon-FusionHD Main Entry Point
Unified command-line interface for system management
"""

import sys
import json
from typing import Optional
from aielon_living_os import get_living_os, ComponentType
from system_monitor import validate_system, monitor_health, HealthMonitor, WorkflowValidator
from unified_config import get_config


def print_banner():
    """Print AiElon-FusionHD banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                   AiElon-FusionHD v1.0.0                    ║
║              Unified Living OS • 100% Efficiency            ║
║                                                              ║
║  • Fusion HD UI  • Halal Wallet  • HCare  • Ummah Hub      ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def cmd_status(args):
    """Show system status"""
    living_os = get_living_os()
    status = living_os.get_system_health()
    
    print("\n=== System Status ===\n")
    print(f"Operating System: {status['os']} v{status['version']}")
    print(f"Overall Efficiency: {status['overall_efficiency'] * 100:.2f}%")
    print(f"Operational: {'✓ YES' if status['operational'] else '✗ NO'}")
    
    print("\n=== FusionCore Status ===")
    fc = status['fusion_core']
    print(f"Efficiency Rate: {fc['efficiency_rate'] * 100:.2f}%")
    print(f"Operations Processed: {fc['operations_processed']}")
    print(f"Error Count: {fc['error_count']}")
    
    print("\n=== Subsystems ===")
    for subsystem, details in fc['subsystems'].items():
        print(f"  {subsystem}:")
        for key, value in details.items():
            print(f"    {key}: {value}")
    
    print("\n=== Components ===")
    for comp_name, comp_status in status['components'].items():
        print(f"  {comp_name}: {comp_status['status']}")
    
    print()


def cmd_validate(args):
    """Run full system validation"""
    print("\n=== Running Full System Validation ===\n")
    print("This may take a few moments...\n")
    
    result = validate_system()
    
    print(f"Validation Complete: {'✓ PASSED' if result['all_tests_passed'] else '✗ FAILED'}")
    print(f"Validation Time: {result['validation_time_seconds']:.2f} seconds\n")
    
    # FusionCore tests
    print("=== FusionCore Validation ===")
    fc_result = result['results']['fusion_core']
    print(f"Status: {'✓ PASSED' if fc_result['all_tests_passed'] else '✗ FAILED'}")
    print(f"Efficiency: {fc_result['efficiency'] * 100:.2f}%")
    for test in fc_result['tests']:
        status = '✓' if test['passed'] else '✗'
        print(f"  {status} {test['test']}: {test['details']}")
    
    # Component tests
    print("\n=== Component Validation ===")
    comp_result = result['results']['components']
    print(f"Status: {'✓ PASSED' if comp_result['all_components_passed'] else '✗ FAILED'}")
    for comp_name, test in comp_result['component_tests'].items():
        status = '✓' if test['passed'] else '✗'
        print(f"  {status} {comp_name}: {test['details']}")
    
    # Integration tests
    print("\n=== Integration Validation ===")
    int_result = result['results']['integration']
    print(f"Status: {'✓ PASSED' if int_result['integration_validated'] else '✗ FAILED'}")
    for test in int_result['tests']:
        status = '✓' if test['passed'] else '✗'
        print(f"  {status} {test['test']}: {test['details']}")
    
    print()


def cmd_health(args):
    """Check system health"""
    print("\n=== System Health Check ===\n")
    
    health = monitor_health()
    
    print(f"Health Status: {health['alert']}")
    print(f"Efficiency Rate: {health['efficiency_percentage']}")
    print(f"Healthy: {'✓ YES' if health['healthy'] else '✗ NO'}")
    print(f"Operations Processed: {health['operations_processed']}")
    print(f"Error Count: {health['error_count']}")
    print(f"Threshold: {health['threshold'] * 100}%")
    print()


def cmd_optimize(args):
    """Optimize all systems"""
    print("\n=== Optimizing All Systems ===\n")
    
    living_os = get_living_os()
    result = living_os.optimize_all_systems()
    
    print(f"Optimization Complete: {'✓ YES' if result['optimization_complete'] else '✗ NO'}")
    print(f"Current Efficiency: {result['current_efficiency'] * 100:.2f}%")
    print(f"Target Efficiency: {result['efficiency_target'] * 100:.2f}%")
    
    print("\n=== AI Optimization ===")
    ai_opt = result['ai_optimization']
    print(f"Models Optimized: {ai_opt['models_optimized']}")
    print(f"Performance Gain: {ai_opt['performance_gain']}")
    
    print("\n=== Scaling ===")
    scaling = result['scaling']
    print(f"Scaling Enabled: {scaling['scaling_enabled']}")
    print(f"Scaling Factor: {scaling['scaling_factor']:.2f}x")
    print(f"Regions Active: {scaling['regions_active']}")
    print()


def cmd_config(args):
    """Show configuration"""
    config = get_config()
    
    if args and args[0] == '--validate':
        print("\n=== Validating Configuration ===\n")
        validation = config.validate()
        
        print(f"Valid: {'✓ YES' if validation['valid'] else '✗ NO'}")
        if validation['issues']:
            print("\nIssues Found:")
            for issue in validation['issues']:
                print(f"  ✗ {issue}")
        else:
            print("No issues found.")
        print()
    else:
        print("\n=== System Configuration ===\n")
        print(json.dumps(config.get_all(), indent=2))
        print()


def cmd_component(args):
    """Test specific component"""
    if not args or len(args) < 1:
        print("\nError: Please specify a component (ui, wallet, hcare, hub)")
        print("Example: python main.py component ui\n")
        return
    
    component_map = {
        'ui': ComponentType.UI,
        'wallet': ComponentType.WALLET,
        'hcare': ComponentType.HEALTHCARE,
        'hub': ComponentType.COMMUNITY
    }
    
    comp_name = args[0].lower()
    if comp_name not in component_map:
        print(f"\nError: Unknown component '{comp_name}'")
        print("Available: ui, wallet, hcare, hub\n")
        return
    
    print(f"\n=== Testing {comp_name.upper()} Component ===\n")
    
    living_os = get_living_os()
    result = living_os.execute_unified_operation(
        f"test_{comp_name}",
        component_map[comp_name],
        {"test": "data"}
    )
    
    print(f"Component: {result['component']}")
    print(f"Operation: {result['operation']}")
    print(f"Efficiency: {result['efficiency'] * 100:.2f}%")
    print(f"Status: {result['result'].get('status', 'N/A')}")
    print()


def cmd_help(args):
    """Show help message"""
    help_text = """
Usage: python main.py [command] [options]

Commands:
  status      Show system status
  validate    Run full system validation
  health      Check system health
  optimize    Optimize all systems
  config      Show configuration (use --validate to validate)
  component   Test specific component (ui, wallet, hcare, hub)
  help        Show this help message

Examples:
  python main.py status
  python main.py validate
  python main.py health
  python main.py optimize
  python main.py config --validate
  python main.py component wallet

For more information, visit the documentation.
    """
    print(help_text)


def main():
    """Main entry point"""
    commands = {
        'status': cmd_status,
        'validate': cmd_validate,
        'health': cmd_health,
        'optimize': cmd_optimize,
        'config': cmd_config,
        'component': cmd_component,
        'help': cmd_help
    }
    
    print_banner()
    
    if len(sys.argv) < 2:
        cmd_status([])
        print("Run 'python main.py help' for available commands.\n")
        return
    
    command = sys.argv[1].lower()
    args = sys.argv[2:] if len(sys.argv) > 2 else []
    
    if command not in commands:
        print(f"\nError: Unknown command '{command}'")
        print("Run 'python main.py help' for available commands.\n")
        return
    
    try:
        commands[command](args)
    except Exception as e:
        print(f"\nError executing command: {e}\n")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
