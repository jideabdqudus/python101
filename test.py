import unittest
from Main import guessing_game

class TestCase(unittest.TestCase):
    def setUp(self):
        print("About to run a Test Function")

    def testcase1(self):
        result = guessing_game(5, 5)
        self.assertTrue(result)

    def testcase2(self):
        result = guessing_game(5, 0)
        self.assertFalse(result)

    def testcase3(self):
        result = guessing_game(5, 11)
        self.assertFalse(result)

    def testcase4(self):
        result = guessing_game(5, "aksks")
        self.assertFalse(result)


if __name__ == '__main__':
   unittest.main()