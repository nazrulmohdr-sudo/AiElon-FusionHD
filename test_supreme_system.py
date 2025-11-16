"""
Unit Tests for Supreme GodMode Mutlak System
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from supreme_godmode import SupremeGodMode, ConstraintState
from aielonchain338 import AielonChain338
from supreme_command import SupremeCommand


class TestSupremeGodMode(unittest.TestCase):
    """Test cases for Supreme GodMode"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.godmode = SupremeGodMode()
    
    def test_constraint_full(self):
        """Test 100% = 1 constraint"""
        result = self.godmode.resolve_constraint_full()
        self.assertEqual(result, 1.0)
    
    def test_constraint_zero(self):
        """Test 0% = 0 constraint"""
        result = self.godmode.resolve_constraint_zero()
        self.assertEqual(result, 0.0)
    
    def test_constraint_all(self):
        """Test all = ∞ constraint"""
        result = self.godmode.resolve_constraint_all()
        self.assertEqual(result, "∞")
    
    def test_percentage_logic_boundaries(self):
        """Test percentage logic at boundaries"""
        self.assertEqual(self.godmode.apply_percentage_logic(0.0), 0.0)
        self.assertEqual(self.godmode.apply_percentage_logic(1.0), 100.0)
    
    def test_percentage_logic_midpoints(self):
        """Test percentage logic at midpoints"""
        self.assertEqual(self.godmode.apply_percentage_logic(0.5), 50.0)
        self.assertEqual(self.godmode.apply_percentage_logic(0.25), 25.0)
        self.assertEqual(self.godmode.apply_percentage_logic(0.75), 75.0)
    
    def test_percentage_logic_invalid_range(self):
        """Test percentage logic with invalid values"""
        with self.assertRaises(ValueError):
            self.godmode.apply_percentage_logic(-0.1)
        with self.assertRaises(ValueError):
            self.godmode.apply_percentage_logic(1.1)
    
    def test_godmode_formula_initialization(self):
        """Test GodMode formula initialization"""
        formula = self.godmode.godmode_formula
        self.assertEqual(formula['zero'], 0)
        self.assertEqual(formula['infinity'], float('inf'))
        self.assertTrue(formula['unified'])
    
    def test_total_solution_framework_validation(self):
        """Test Total Solution Framework validation"""
        result = self.godmode.validate_total_solution_framework()
        self.assertTrue(result)
        self.assertTrue(self.godmode.system_integrity)
    
    def test_godmode_state(self):
        """Test GodMode state retrieval"""
        state = self.godmode.get_godmode_state()
        self.assertIn('formula', state)
        self.assertIn('components', state)
        self.assertTrue(state['active'])
    
    def test_system_status(self):
        """Test system status retrieval"""
        status = self.godmode.get_system_status()
        self.assertIn('constraints', status)
        self.assertIn('godmode', status)
        self.assertTrue(status['integrity'])


class TestAielonChain338(unittest.TestCase):
    """Test cases for AielonChain338"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.chain = AielonChain338()
    
    def test_genesis_block_creation(self):
        """Test genesis block is created"""
        self.assertEqual(len(self.chain.chain), 1)
        self.assertEqual(self.chain.chain[0]['index'], 0)
        self.assertEqual(self.chain.chain[0]['data']['type'], 'genesis')
    
    def test_add_block(self):
        """Test adding a block"""
        initial_length = len(self.chain.chain)
        block = self.chain.add_block({'type': 'test', 'data': 'test_data'})
        self.assertEqual(len(self.chain.chain), initial_length + 1)
        self.assertEqual(block['data']['type'], 'test')
    
    def test_chain_integrity(self):
        """Test chain integrity validation"""
        self.chain.add_block({'type': 'test1'})
        self.chain.add_block({'type': 'test2'})
        self.assertTrue(self.chain.validate_chain_integrity())
    
    def test_immutable_lock(self):
        """Test immutable lock application"""
        self.assertFalse(self.chain.lock_state['is_locked'])
        result = self.chain.apply_immutable_lock()
        self.assertTrue(result)
        self.assertTrue(self.chain.lock_state['is_locked'])
    
    def test_add_block_after_lock(self):
        """Test that blocks cannot be added after lock"""
        self.chain.apply_immutable_lock()
        with self.assertRaises(RuntimeError):
            self.chain.add_block({'type': 'test'})
    
    def test_eternal_seal(self):
        """Test eternal seal application"""
        self.chain.apply_immutable_lock()
        signature = self.chain.apply_eternal_seal()
        self.assertIsNotNone(signature)
        self.assertTrue(self.chain.lock_state['is_sealed'])
        self.assertEqual(len(signature), 128)  # SHA-512 hex length
    
    def test_seal_without_lock(self):
        """Test that seal cannot be applied without lock"""
        with self.assertRaises(RuntimeError):
            self.chain.apply_eternal_seal()
    
    def test_reinforcement_level(self):
        """Test reinforcement level"""
        self.assertEqual(self.chain.reinforcement_level, 338)
    
    def test_chain_status(self):
        """Test chain status retrieval"""
        status = self.chain.get_chain_status()
        self.assertIn('chain_length', status)
        self.assertIn('is_locked', status)
        self.assertIn('reinforcement_level', status)
        self.assertEqual(status['reinforcement_level'], 338)


class TestSupremeCommand(unittest.TestCase):
    """Test cases for Supreme Command"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.supreme = SupremeCommand()
    
    def test_initialization(self):
        """Test Supreme Command initialization"""
        self.assertIsNotNone(self.supreme.godmode)
        self.assertIsNotNone(self.supreme.chain)
        self.assertEqual(self.supreme.supreme_level, float('inf'))
    
    def test_initialize_system(self):
        """Test system initialization"""
        result = self.supreme.initialize_system()
        self.assertTrue(result)
        self.assertTrue(self.supreme.evolution_state['initialized'])
    
    def test_resolve_constraints(self):
        """Test constraint resolution"""
        self.supreme.initialize_system()
        result = self.supreme.resolve_constraints()
        self.assertTrue(result)
        self.assertTrue(self.supreme.evolution_state['constraints_resolved'])
    
    def test_activate_framework(self):
        """Test framework activation"""
        self.supreme.initialize_system()
        self.supreme.resolve_constraints()
        result = self.supreme.activate_total_solution_framework()
        self.assertTrue(result)
        self.assertTrue(self.supreme.evolution_state['framework_activated'])
    
    def test_lock_and_seal(self):
        """Test lock and seal"""
        self.supreme.initialize_system()
        self.supreme.resolve_constraints()
        self.supreme.activate_total_solution_framework()
        result = self.supreme.lock_and_seal_chain()
        self.assertTrue(result)
        self.assertTrue(self.supreme.evolution_state['chain_locked'])
        self.assertTrue(self.supreme.evolution_state['chain_sealed'])
    
    def test_validate_and_finalize(self):
        """Test validation and finalization"""
        # Execute all steps
        self.supreme.initialize_system()
        self.supreme.resolve_constraints()
        self.supreme.activate_total_solution_framework()
        self.supreme.lock_and_seal_chain()
        result = self.supreme.validate_and_finalize()
        self.assertTrue(result)
        self.assertTrue(self.supreme.evolution_state['system_finalized'])
    
    def test_complete_upgrade(self):
        """Test complete upgrade execution"""
        result = self.supreme.execute_supreme_upgrade()
        self.assertTrue(result)
        # Check all evolution states
        for state, value in self.supreme.evolution_state.items():
            self.assertTrue(value, f"Evolution state '{state}' should be True")
    
    def test_evolution_states(self):
        """Test evolution states initialization"""
        expected_states = [
            'initialized',
            'constraints_resolved',
            'framework_activated',
            'chain_locked',
            'chain_sealed',
            'system_finalized'
        ]
        for state in expected_states:
            self.assertIn(state, self.supreme.evolution_state)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system"""
    
    def test_end_to_end_workflow(self):
        """Test complete end-to-end workflow"""
        supreme = SupremeCommand()
        
        # Execute upgrade
        result = supreme.execute_supreme_upgrade()
        self.assertTrue(result)
        
        # Verify GodMode
        godmode_status = supreme.godmode.get_system_status()
        self.assertTrue(godmode_status['integrity'])
        self.assertEqual(godmode_status['constraints']['100%'], 1.0)
        self.assertEqual(godmode_status['constraints']['0%'], 0.0)
        self.assertEqual(godmode_status['constraints']['all'], '∞')
        
        # Verify Chain
        chain_status = supreme.chain.get_chain_status()
        self.assertTrue(chain_status['is_locked'])
        self.assertTrue(chain_status['is_sealed'])
        self.assertTrue(chain_status['integrity_valid'])
        self.assertTrue(chain_status['demi_masa_abadi'])
        
        # Verify evolution
        self.assertTrue(supreme.evolution_state['system_finalized'])
    
    def test_constraint_consistency(self):
        """Test constraint consistency across system"""
        supreme = SupremeCommand()
        supreme.execute_supreme_upgrade()
        
        # Verify constraints are consistent
        full = supreme.godmode.resolve_constraint_full()
        zero = supreme.godmode.resolve_constraint_zero()
        all_val = supreme.godmode.resolve_constraint_all()
        
        self.assertEqual(full, 1.0)
        self.assertEqual(zero, 0.0)
        self.assertEqual(all_val, '∞')
    
    def test_immutability_enforcement(self):
        """Test that immutability is enforced"""
        supreme = SupremeCommand()
        supreme.execute_supreme_upgrade()
        
        # Chain should be locked
        self.assertTrue(supreme.chain.lock_state['is_locked'])
        
        # Should not be able to add blocks
        with self.assertRaises(RuntimeError):
            supreme.chain.add_block({'type': 'test'})


def run_tests():
    """Run all tests"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestSupremeGodMode))
    suite.addTests(loader.loadTestsFromTestCase(TestAielonChain338))
    suite.addTests(loader.loadTestsFromTestCase(TestSupremeCommand))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    exit(run_tests())
