import unittest
from activity import fizzbuzz
from unittest.mock import patch

class FizzBuzzTestCase(unittest.TestCase):

    def test_fizzbuzz_logic(self):

        for number in range(1, 999):
            if number % 3 == 0 and number % 5 == 0:
                self.assertEqual(fizzbuzz(number), "FizzBuzz")
            elif number % 3 == 0:
                self.assertEqual(fizzbuzz(number), "Fizz")
            elif number % 5 == 0:
                self.assertEqual(fizzbuzz(number), "Buzz")
            else:
                self.assertEqual(fizzbuzz(number), str(number))

    @patch('builtins.input', side_effect=["3", "5", "15", "7"])
    def test_fizzbuzz_with_mocked_input(self, mock_input):
        expected_outputs = ["Fizz", "Buzz", "FizzBuzz", "7"]
        inputs = [3, 5, 15, 7]
        
        for expected, value in zip(expected_outputs, inputs):
            self.assertEqual(fizzbuzz(value), expected)

if __name__ == '__main__':
    unittest.main()