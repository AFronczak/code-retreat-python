import unittest
from gamey import hello, numbers

class TestStringMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3, 2+1)

    def test_hello(self):
        self.assertEqual(hello(), "hi")

    def test_numbers(self):
        self.assertEqual(numbers(), 5)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
