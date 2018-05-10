import unittest
from brackets_balancer import BracketsBalancer

class TestBracketsBalancer(unittest.TestCase):
    def test_Balance_GivenEmptyString_ShouldReturnEmptryString(self):
        # Arrange
        brackets = ""
        # Act
        result = BracketsBalancer.Balance(brackets)
        # Assert
        self.assertEqual(result, "")
    def test_Balance_GivenOneSetOfBalancedBrackets_ShouldReturnOK(self):
        # Arrange
        brackets = "[]"
        # Act
        result = BracketsBalancer.Balance(brackets)
        # Assert
        self.assertEqual(result, "OK")
