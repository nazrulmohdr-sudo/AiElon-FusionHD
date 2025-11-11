#!/usr/bin/env python3
"""
Basic tests for AiElon FusionHD system
Validates all subsystems are operational
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.aielon_living_os import AiElonLivingOS, SystemStatus
from modules.aielon_chain338 import AiElonChain338
from modules.trade138 import Trade138, OrderType
from modules.bank_compliance import BankCompliance, ComplianceStatus
from modules.quantum_memory_field import QuantumMemoryField
from modules.firewall import FirewallLayer, ThreatLevel
from modules.hcare_stability import HCareStability, MetricType
from decimal import Decimal


def test_living_os():
    """Test AiElon Living OS"""
    print("Testing AiElon Living OS...")
    os_instance = AiElonLivingOS()
    assert os_instance.version == "1.0.0"
    assert os_instance.status == SystemStatus.INITIALIZING
    print("✓ AiElon Living OS tests passed")


def test_blockchain():
    """Test AiElonChain338"""
    print("Testing AiElonChain338...")
    blockchain = AiElonChain338()
    assert len(blockchain.chain) == 1  # Genesis block
    
    blockchain.add_transaction({'from': 'Alice', 'to': 'Bob', 'amount': 50})
    blockchain.mine_pending_transactions('Miner1')
    assert len(blockchain.chain) == 2
    assert blockchain.is_chain_valid()
    print("✓ AiElonChain338 tests passed")


def test_trading():
    """Test Trade138"""
    print("Testing Trade138...")
    trading = Trade138()
    trading.create_portfolio('user001')
    
    order_id = trading.place_order('user001', OrderType.MARKET, 'AEC', Decimal('5.0'))
    assert order_id is not None
    
    stats = trading.get_trade_statistics()
    assert stats['total_orders'] == 1
    assert stats['executed_orders'] == 1
    print("✓ Trade138 tests passed")


def test_compliance():
    """Test Bank Compliance"""
    print("Testing Bank Compliance...")
    compliance = BankCompliance()
    
    status = compliance.register_user_kyc('user001', {
        'full_name': 'Test User',
        'date_of_birth': '1990-01-01',
        'address': '123 Test St',
        'id_number': 'TEST001',
        'country': 'USA'
    })
    assert status == ComplianceStatus.COMPLIANT
    
    transaction = {'user_id': 'user001', 'amount': 5000.0, 'type': 'transfer'}
    compliant, risk_level = compliance.verify_transaction(transaction)
    assert compliant == True
    print("✓ Bank Compliance tests passed")


def test_memory():
    """Test Quantum Memory Field"""
    print("Testing Quantum Memory Field...")
    memory = QuantumMemoryField(capacity_mb=512)
    
    assert memory.store('test_key', {'data': 'test_value'})
    data = memory.retrieve('test_key')
    assert data == {'data': 'test_value'}
    
    stats = memory.get_memory_statistics()
    assert stats['total_blocks'] == 1
    print("✓ Quantum Memory Field tests passed")


def test_firewall():
    """Test Firewall Layer"""
    print("Testing Firewall Layer...")
    firewall = FirewallLayer()
    
    # Test normal request
    request = {
        'source_ip': '192.168.1.100',
        'endpoint': '/api/test',
        'payload': 'normal request'
    }
    allowed, threat, reason = firewall.validate_request(request)
    assert allowed == True
    assert threat == ThreatLevel.NONE
    
    # Test malicious request
    malicious_request = {
        'source_ip': '192.168.1.200',
        'endpoint': '/api/test',
        'payload': '<script>alert("xss")</script>'
    }
    allowed, threat, reason = firewall.validate_request(malicious_request)
    assert allowed == False
    print("✓ Firewall Layer tests passed")


def test_hcare():
    """Test HCare Stability"""
    print("Testing HCare Stability...")
    hcare = HCareStability()
    
    assert hcare.record_metric(MetricType.CPU, 50.0, 'test_component')
    assert hcare.record_metric(MetricType.MEMORY, 60.0, 'test_component')
    
    health = hcare.perform_health_check('test_component')
    assert 'status' in health
    
    summary = hcare.get_system_health_summary()
    assert 'overall_status' in summary
    print("✓ HCare Stability tests passed")


def test_integration():
    """Test system integration"""
    print("Testing System Integration...")
    from core.system_integration import AiElonFusionHD
    
    fusion_hd = AiElonFusionHD()
    assert fusion_hd.living_os is not None
    assert len(fusion_hd.living_os.subsystems) == 6
    
    # Start system
    result = fusion_hd.start()
    assert result == True
    
    # Check status
    status = fusion_hd.living_os.get_system_status()
    assert status['operational_readiness'] == 100.0
    assert status['error_count'] == 0
    assert status['eternal_truth_lock'] == True
    
    print("✓ System Integration tests passed")


def run_all_tests():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("AiElon FusionHD Test Suite")
    print("=" * 60 + "\n")
    
    try:
        test_living_os()
        test_blockchain()
        test_trading()
        test_compliance()
        test_memory()
        test_firewall()
        test_hcare()
        test_integration()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED")
        print("=" * 60)
        return 0
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ TEST ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(run_all_tests())
