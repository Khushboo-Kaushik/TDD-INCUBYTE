import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.string_add import Addclass

class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        calculator = Addclass()  # Create an instance of Addclass
        result = calculator.add("")  # Call the add method on the instance
        self.assertEqual(result, 0)  # Expect the result to be 0

    def test_single_number(self):
        calculator = Addclass()
        result = calculator.add("1")
        self.assertEqual(result, 1)  # Expect 1

    def test_multiple_numbers(self):
        calculator = Addclass()
        result = calculator.add("1,5")
        self.assertEqual(result, 6)  # Expect 1 + 5 = 6

    def test_newline_separator(self):
        calculator = Addclass()
        result = calculator.add("1\n2,3")
        self.assertEqual(result, 6)  # Expect 1 + 2 + 3 = 6

    def test_negative_number(self):
        calculator = Addclass()
        with self.assertRaises(ValueError) as context:
            calculator.add("1,-5")
        self.assertTrue("Negative numbers not allowed" in str(context.exception))

if __name__ == '__main__':
    unittest.main()