"""
Unit Tests for AI Engine
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from ai.ai_engine import AIEngine


class TestAIEngine(unittest.TestCase):
    """Test cases for AI Engine"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.ai_engine = AIEngine()
        self.ai_engine.initialize()
    
    def test_initialization(self):
        """Test AI engine initialization"""
        self.assertEqual(self.ai_engine.model_version, "2.0")
        self.assertEqual(len(self.ai_engine.context_memory), 0)
        self.assertIn("patterns", self.ai_engine.learning_data)
    
    def test_process_natural_language(self):
        """Test natural language processing"""
        result = self.ai_engine.process_natural_language("What is the blockchain status?")
        
        self.assertIn("intent", result)
        self.assertIn("entities", result)
        self.assertIn("sentiment", result)
        self.assertIn("confidence", result)
        self.assertEqual(result["intent"], "query")
    
    def test_intent_detection(self):
        """Test intent detection"""
        words = ["create", "new", "transaction"]
        intent = self.ai_engine._detect_intent(words)
        self.assertEqual(intent, "action")
        
        words = ["what", "is", "status"]
        intent = self.ai_engine._detect_intent(words)
        self.assertEqual(intent, "query")
    
    def test_entity_extraction(self):
        """Test entity extraction"""
        words = ["blockchain", "aielonchain338", "status"]
        entities = self.ai_engine._extract_entities(words)
        
        self.assertIsInstance(entities, list)
        self.assertTrue(any(e["type"] == "blockchain" for e in entities))
    
    def test_sentiment_analysis(self):
        """Test sentiment analysis"""
        positive_words = ["great", "excellent", "amazing"]
        sentiment = self.ai_engine._analyze_sentiment(positive_words)
        self.assertEqual(sentiment["sentiment"], "positive")
        
        negative_words = ["bad", "terrible", "awful"]
        sentiment = self.ai_engine._analyze_sentiment(negative_words)
        self.assertEqual(sentiment["sentiment"], "negative")
    
    def test_learn_from_interaction(self):
        """Test learning from interactions"""
        interaction = {"action": "query", "result": "success"}
        self.ai_engine.learn_from_interaction(interaction)
        
        self.assertGreater(len(self.ai_engine.learning_data["patterns"]), 0)
    
    def test_contextual_recommendation(self):
        """Test contextual recommendations"""
        self.ai_engine.process_natural_language("Show security settings")
        recommendations = self.ai_engine.get_contextual_recommendation({})
        
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)
    
    def test_statistics(self):
        """Test getting statistics"""
        self.ai_engine.process_natural_language("Test query")
        stats = self.ai_engine.get_statistics()
        
        self.assertIn("model_version", stats)
        self.assertIn("queries_processed", stats)
        self.assertGreater(stats["queries_processed"], 0)


if __name__ == '__main__':
    unittest.main()
