# Write tests for is_even() using unittest
import unittest
from main import is_even, process_numbers   
class TestMainFunctions(unittest.TestCase):
    def test_is_even_with_even_number(self):
        self.assertTrue(is_even(4))
    
    def test_is_even_with_odd_number(self):
        self.assertFalse(is_even(5))
    
    def test_is_even_with_zero(self):
        self.assertTrue(is_even(0))
    
    def test_is_even_with_negative_even_number(self):
        self.assertTrue(is_even(-2))
    
    def test_is_even_with_negative_odd_number(self):
        self.assertFalse(is_even(-3))