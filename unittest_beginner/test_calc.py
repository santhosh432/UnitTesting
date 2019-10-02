

import unittest
import calc


class TestCaseCalc(unittest.TestCase):
    def setUp(self):
        print('This instance method is for SetUp')

    def test_add(self):
        self.assertEqual(calc.add(2,3), 5)

    def tearDown(self):
        print('This instance method is for teardown')

if __name__ == "__main__":
    unittest.main()


'''
Another way to run unit test is
python3 -m unittest test_cal.py
'''