import unittest
from Main import guessing_game

class TestCase(unittest.TestCase):
    def setUp(self):
        print("About to run a Test Function")

    def testcase1(self):
        result = guessing_game()
        self.assertEqual()

        if __name__ == '__main__':
            unittest.main()