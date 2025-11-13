#!/usr/bin/env python3
"""
AiElon FusionHD System Status Check
Quick status verification for all subsystems
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.system_integration import AiElonFusionHD
import json


def print_banner():
    """Print status check banner"""
    print("\n" + "=" * 70)
    print("AiElon FusionHD - System Status Check")
    print("=" * 70 + "\n")


def check_system_status():
    """Check and display system status"""
    try:
        # Initialize system
        fusion_hd = AiElonFusionHD()
        
        # Start system
        print("Initializing system...")
        if not fusion_hd.start():
            print("❌ System failed to start")
            return False
        
        print("\n" + "-" * 70)
        print("SYSTEM STATUS")
        print("-" * 70)
        
        # Get system status
        status = fusion_hd.living_os.get_system_status()
        
        # Display key metrics
        print(f"Version:              {status['version']}")
        print(f"Status:               {status['status'].upper()}")
        print(f"Operational Readiness: {status['operational_readiness']}%")
        print(f"Error Count:          {status['error_count']}")
        print(f"Eternal Truth Lock:   {'✓ ENGAGED' if status['eternal_truth_lock'] else '✗ NOT ENGAGED'}")
        
        print("\n" + "-" * 70)
        print("SUBSYSTEM STATUS")
        print("-" * 70)
        
        for name, subsystem_status in status['subsystems'].items():
            status_symbol = "✓" if subsystem_status == "operational" else "✗"
            print(f"{status_symbol} {name:25s} {subsystem_status.upper()}")
        
        # Get comprehensive report
        report = fusion_hd.get_comprehensive_report()
        
        print("\n" + "-" * 70)
        print("DETAILED METRICS")
        print("-" * 70)
        
        print(f"\nBlockchain:")
        print(f"  Chain Length:       {report['blockchain']['length']}")
        print(f"  Chain Valid:        {report['blockchain']['valid']}")
        print(f"  Difficulty:         {report['blockchain']['difficulty']}")
        
        print(f"\nTrading:")
        print(f"  Total Orders:       {report['trading']['total_orders']}")
        print(f"  Executed Orders:    {report['trading']['executed_orders']}")
        print(f"  Active Users:       {report['trading']['active_users']}")
        
        print(f"\nCompliance:")
        print(f"  KYC Records:        {report['compliance']['total_kyc_records']}")
        print(f"  Compliant Users:    {report['compliance']['compliant_users']}")
        print(f"  Flagged Trans:      {report['compliance']['flagged_transactions']}")
        
        print(f"\nMemory:")
        print(f"  Total Blocks:       {report['memory']['total_blocks']}")
        print(f"  Cache Hit Rate:     {report['memory']['cache_hit_rate']}")
        print(f"  Capacity:           {report['memory']['capacity_mb']}MB")
        
        print(f"\nSecurity:")
        print(f"  Firewall Rules:     {report['security']['firewall_rules']}")
        print(f"  Blocked IPs:        {report['security']['blocked_ips']}")
        print(f"  Intrusion Attempts: {report['security']['intrusion_attempts']}")
        
        print(f"\nHealth:")
        print(f"  Total Metrics:      {report['health']['total_metrics']}")
        print(f"  Total Alerts:       {report['health']['total_alerts']}")
        print(f"  Auto Recovery:      {'Enabled' if report['health']['auto_recovery_enabled'] else 'Disabled'}")
        
        print("\n" + "=" * 70)
        
        # Final verdict
        if status['operational_readiness'] == 100.0 and status['error_count'] == 0:
            print("✅ SYSTEM STATUS: FULLY OPERATIONAL")
            print("✅ ETERNAL TRUTH LOCK: ENGAGED")
            print("✅ READY FOR PRODUCTION")
        else:
            print("⚠️  SYSTEM STATUS: OPERATIONAL WITH WARNINGS")
            print(f"   Readiness: {status['operational_readiness']}%")
            print(f"   Errors: {status['error_count']}")
        
        print("=" * 70 + "\n")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error during status check: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print_banner()
    success = check_system_status()
    exit(0 if success else 1)
