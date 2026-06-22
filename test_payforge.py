# test_payforge.py
"""
Tests for PayForge module.
"""

import unittest
from payforge import PayForge

class TestPayForge(unittest.TestCase):
    """Test cases for PayForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PayForge()
        self.assertIsInstance(instance, PayForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PayForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
