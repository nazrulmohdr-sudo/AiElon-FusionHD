"""
Unit Tests for AielonChain338 Blockchain
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from blockchain.aielonchain338 import AielonChain338, Transaction, Block


class TestTransaction(unittest.TestCase):
    """Test cases for Transaction"""
    
    def test_transaction_creation(self):
        """Test transaction creation"""
        tx = Transaction("Alice", "Bob", 10.0)
        
        self.assertEqual(tx.sender, "Alice")
        self.assertEqual(tx.recipient, "Bob")
        self.assertEqual(tx.amount, 10.0)
        self.assertIsNotNone(tx.transaction_id)
    
    def test_transaction_validation(self):
        """Test transaction validation"""
        valid_tx = Transaction("Alice", "Bob", 10.0)
        self.assertTrue(valid_tx.is_valid())
        
        invalid_tx = Transaction("Alice", "Bob", -10.0)
        self.assertFalse(invalid_tx.is_valid())
        
        invalid_tx2 = Transaction("", "Bob", 10.0)
        self.assertFalse(invalid_tx2.is_valid())
    
    def test_transaction_to_dict(self):
        """Test transaction to dictionary conversion"""
        tx = Transaction("Alice", "Bob", 10.0)
        tx_dict = tx.to_dict()
        
        self.assertIn("transaction_id", tx_dict)
        self.assertIn("sender", tx_dict)
        self.assertIn("recipient", tx_dict)
        self.assertIn("amount", tx_dict)


class TestBlock(unittest.TestCase):
    """Test cases for Block"""
    
    def test_block_creation(self):
        """Test block creation"""
        block = Block(0, [], "0")
        
        self.assertEqual(block.index, 0)
        self.assertEqual(len(block.transactions), 0)
        self.assertEqual(block.previous_hash, "0")
        self.assertIsNotNone(block.hash)
    
    def test_block_hash_calculation(self):
        """Test block hash calculation"""
        block = Block(0, [], "0")
        original_hash = block.hash
        
        # Recalculate hash
        new_hash = block.calculate_hash()
        self.assertEqual(original_hash, new_hash)
    
    def test_block_mining(self):
        """Test block mining"""
        block = Block(0, [], "0")
        difficulty = 2
        block.mine_block(difficulty)
        
        # Check that hash starts with required zeros
        self.assertTrue(block.hash.startswith("0" * difficulty))


class TestAielonChain338(unittest.TestCase):
    """Test cases for AielonChain338"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.blockchain = AielonChain338(difficulty=2)
    
    def test_genesis_block(self):
        """Test genesis block creation"""
        self.assertEqual(len(self.blockchain.chain), 1)
        self.assertEqual(self.blockchain.chain[0].index, 0)
        self.assertEqual(self.blockchain.chain[0].previous_hash, "0")
    
    def test_add_transaction(self):
        """Test adding transactions"""
        tx = Transaction("Alice", "Bob", 10.0)
        result = self.blockchain.add_transaction(tx)
        
        self.assertTrue(result)
        self.assertEqual(len(self.blockchain.pending_transactions), 1)
    
    def test_create_transaction(self):
        """Test creating transactions"""
        tx_id = self.blockchain.create_transaction("Alice", "Bob", 10.0)
        
        self.assertIsNotNone(tx_id)
        self.assertEqual(len(self.blockchain.pending_transactions), 1)
    
    def test_mine_pending_transactions(self):
        """Test mining pending transactions"""
        self.blockchain.create_transaction("Alice", "Bob", 10.0)
        initial_length = len(self.blockchain.chain)
        
        new_block = self.blockchain.mine_pending_transactions("Miner1")
        
        self.assertEqual(len(self.blockchain.chain), initial_length + 1)
        self.assertEqual(len(self.blockchain.pending_transactions), 0)
        self.assertIsNotNone(new_block)
    
    def test_chain_validation(self):
        """Test blockchain validation"""
        self.assertTrue(self.blockchain.is_chain_valid())
        
        # Add valid transaction and mine
        self.blockchain.create_transaction("Alice", "Bob", 10.0)
        self.blockchain.mine_pending_transactions("Miner1")
        
        self.assertTrue(self.blockchain.is_chain_valid())
    
    def test_get_balance(self):
        """Test getting balance"""
        # Mine reward to Alice
        self.blockchain.mine_pending_transactions("Alice")
        balance = self.blockchain.get_balance("Alice")
        
        self.assertEqual(balance, self.blockchain.mining_reward)
    
    def test_transaction_history(self):
        """Test getting transaction history"""
        self.blockchain.create_transaction("Alice", "Bob", 5.0)
        self.blockchain.mine_pending_transactions("Miner1")
        
        history = self.blockchain.get_transaction_history("Alice")
        
        self.assertIsInstance(history, list)
        self.assertGreater(len(history), 0)
    
    def test_chain_info(self):
        """Test getting chain info"""
        info = self.blockchain.get_chain_info()
        
        self.assertIn("chain_length", info)
        self.assertIn("difficulty", info)
        self.assertIn("is_valid", info)
        self.assertTrue(info["is_valid"])


if __name__ == '__main__':
    unittest.main()
