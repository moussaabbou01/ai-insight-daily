"""
Unit tests for the AI Insight Daily project.
Run with: pytest tests/
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from storage import ConceptStorage
from email_template import EmailTemplate
from ai_generator import AIConceptGenerator


class TestConceptStorage(unittest.TestCase):
    """Test ConceptStorage class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_file = 'test_concepts.json'
        self.storage = ConceptStorage(self.test_file)
    
    def tearDown(self):
        """Clean up test files"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        # Clean up test data directory if created
        test_dir = os.path.dirname(self.test_file)
        if test_dir and os.path.exists(test_dir) and not os.listdir(test_dir):
            os.rmdir(test_dir)
    
    def test_add_and_load_concepts(self):
        """Test adding and loading concepts"""
        test_concepts = ["Concept A", "Concept B", "Concept C"]
        self.storage.add_concepts(test_concepts)
        
        loaded = self.storage.load_concepts()
        self.assertEqual(loaded, test_concepts)
    
    def test_max_storage_limit(self):
        """Test that storage respects maximum limit"""
        concepts = [f"Concept {i}" for i in range(150)]
        self.storage.add_concepts(concepts, max_stored=100)
        
        loaded = self.storage.load_concepts()
        self.assertEqual(len(loaded), 100)
        self.assertEqual(loaded[-1], "Concept 149")
    
    def test_get_recent_concepts(self):
        """Test getting recent concepts"""
        concepts = [f"Concept {i}" for i in range(100)]
        self.storage.add_concepts(concepts)
        
        recent = self.storage.get_recent_concepts(count=10)
        self.assertEqual(len(recent), 10)
        self.assertEqual(recent[-1], "Concept 99")


class TestEmailTemplate(unittest.TestCase):
    """Test EmailTemplate class"""
    
    def test_create_html_email(self):
        """Test HTML email creation"""
        test_content = """# Test Concept
        
This is a test concept with **bold text**.

- Point 1
- Point 2
- Point 3"""
        
        html = EmailTemplate.create_html_email(test_content)
        
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("AI Insight Daily", html)
        self.assertIn("Test Concept", html)
        self.assertIn("<strong>", html)
        self.assertIn("<li", html)
    
    def test_format_content(self):
        """Test content formatting"""
        content = "This is **bold text** and regular text"
        formatted = EmailTemplate._format_content(content)
        
        self.assertIn("<strong>", formatted)
        self.assertIn("</strong>", formatted)
        self.assertIn("bold text", formatted)


class TestAIConceptGenerator(unittest.TestCase):
    """Test AIConceptGenerator class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.generator = AIConceptGenerator(
            api_key="test_key",
            api_url="https://test.api",
            model="test_model"
        )
    
    def test_create_prompt(self):
        """Test prompt creation"""
        previous = ["Neural Networks", "Deep Learning"]
        prompt = self.generator._create_prompt(previous)
        
        self.assertIn("Neural Networks", prompt)
        self.assertIn("Deep Learning", prompt)
        self.assertIn("5 NEW concepts", prompt)
    
    def test_extract_concept_titles(self):
        """Test concept title extraction"""
        content = """# Concept One
        
Some description here

## Concept Two

More description

### Concept Three

Even more text"""
        
        titles = AIConceptGenerator.extract_concept_titles(content)
        self.assertGreater(len(titles), 0)
        self.assertTrue(all(isinstance(t, str) for t in titles))


if __name__ == '__main__':
    unittest.main()
