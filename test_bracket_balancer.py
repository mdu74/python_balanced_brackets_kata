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

    def test_Balance_GivenBalancedBrackets_ShouldReturnOK(self):
        balancedBrackets = ["[]", "[][]", "[[]]", "[[[][]]]"]
        for bracket in balancedBrackets:
            # Arrange
            brackets = bracket
            # Act
            result = BracketsBalancer.Balance(brackets)
            # Assert
            self.assertEqual(result, "OK")

    def test_Balance_GivenUnBalancedBrackets_ShouldReturnFAIL(self):
        balancedBrackets = ["]["]
        for bracket in balancedBrackets:
            # Arrange
            brackets = bracket
            # Act
            result = BracketsBalancer.Balance(brackets)
            # Assert
            self.assertEqual(result, "FAIL")
    
    
