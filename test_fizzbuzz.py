import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_three(self):
        self.assertEqual(fizzbuzz.fizzbuzz(3), 'Fizz')

    def test_five(self):
        self.assertEqual(fizzbuzz.fizzbuzz(5), 'Buzz')

    def test_seven(self):
        self.assertEqual(fizzbuzz.fizzbuzz(7), 7)

    def test_fifteen(self):
        self.assertEqual(fizzbuzz.fizzbuzz(15), 'FizzBuzz')

    def test_ten(self):
        self.assertEqual(fizzbuzz.fizzbuzz(10), 'Buzz')

    def test_thirty(self):
        self.assertEqual(fizzbuzz.fizzbuzz(30), 'FizzBuzz')

    def test_six(self):
        self.assertEqual(fizzbuzz.fizzbuzz(6), 'Fizz')

if __name__ == '__main__':
    unittest.main()
