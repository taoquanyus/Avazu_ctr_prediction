import unittest

class TestExample(unittest.TestCase):
    """A simple test case example."""

    def test_addition(self):
        """Test that 1 + 1 equals 2."""
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        """Test that 5 - 3 equals 2."""
        self.assertEqual(5 - 3, 2)

if __name__ == '__main__':
    unittest.main()