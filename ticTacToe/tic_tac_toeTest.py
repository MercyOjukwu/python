import unittest
from tic_tac_toe import Tic_Tac_Toe

from .import tic_tac_toe


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Tic_Tac_Toe()

    def test_that_object_exists(self):
        self.assertIsNotNone(self.game)
        self.assertIsInstance(self.game, tic_tac_toe.Tic_Tac_Toe)


if __name__ == '__main__':
    unittest.main()
