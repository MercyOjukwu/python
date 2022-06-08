import unittest
from . import playground

class PLaygroundTest(unittest.TestCase):
    def setUp(self) -> None:
        print("hey you")



    def tearDown(self) -> None:
        print("Bye")


if __name__ == '__main__':
    unittest.main()
