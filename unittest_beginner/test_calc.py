

import unittest
import calc


class TestCaseCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2,3), 5)

if __name__ == "__main__":
    unittest.main()
