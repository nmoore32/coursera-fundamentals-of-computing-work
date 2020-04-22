"""
Test suite for solitaire_mancala.py
"""
import unittest

from solitaire_mancala import SolitaireMancala


class TestSolitaireMancala(unittest.TestCase):
    """
    Series of tests for solitaire_mancala
    """

    def setUp(self):
        """
        Create a new SolitaireMancala object to be used for each test
        """
        self.game = SolitaireMancala()

    def test_initial_value(self):
        """
        Check that board initialzes as empty list
        """
        self.assertEqual(str(self.game), '[]')

    def test_set_board(self):
        """
        Check that the board is identical to list provided to set_board method
        """
        self.game.set_board([1])
        self.assertEqual(str(self.game), '[1]')
        self.game.set_board([1, 0, 5])
        self.assertEqual(str(self.game), '[5, 0, 1]')

    def test_str(self):
        """
        Check that the proper string representation of the board is returned
        """
        self.assertEqual(str(self.game), '[]')
        self.game.set_board([1])
        self.assertEqual(str(self.game), '[1]')
        self.game.set_board([1, 0, 5])
        self.assertEqual(str(self.game), '[5, 0, 1]')
        self.game.set_board([1, 2, 0, 4, 5])
        self.assertEqual(str(self.game), '[5, 4, 0, 2, 1]')

    def test_get_num_seeds(self):
        """
        Check that get_num_seeds returns the correct number of seeds
        """
        self.game.set_board([0, 1, 2, 3, 4, 5, 6])
        for idx in range(7):
            self.assertEqual(self.game.get_num_seeds(idx), idx)

    def test_is_game_won(self):
        """
        Check to see that the is_game_won correctly identified winning board states
        """
        self.game.set_board([6, 0, 0, 0, 0, 0, 0])
        self.assertEqual(self.game.is_game_won(), True)
        self.game.set_board([6, 1, 0, 0, 0, 0, 0])
        self.assertEqual(self.game.is_game_won(), False)
        self.game.set_board([0, 1, 0, 0, 0, 0, 0])
        self.assertEqual(self.game.is_game_won(), False)
        self.game.set_board([6, 0, 1, 0, 0, 0, 0])
        self.assertEqual(self.game.is_game_won(), False)
        self.game.set_board([6, 0, 0, 2, 0, 0, 0])
        self.assertEqual(self.game.is_game_won(), False)
        self.game.set_board([6, 0, 0, 0, 0, 2, 0])
        self.assertEqual(self.game.is_game_won(), False)

    def test_is_legal_move(self):
        """
        Check to see if is_legal_move correctly identifies legal moves
        """
        self.game.set_board([0, 1, 2, 3, 4, 5, 6])
        for idx in range(1, 7):
            self.assertEqual(self.game.is_legal_move(idx), True)
        self.game.set_board([0, 0, 0, 0, 0, 0, 0])
        for idx in range(1, 7):
            self.assertEqual(self.game.is_legal_move(idx), False)
        self.game.set_board([0, 2, 3, 4, 5, 6, 7])
        for idx in range(1, 7):
            self.assertEqual(self.game.is_legal_move(idx), False)

    def test_apply_move(self):
        """
        Check whether apply move changes the board state appropriately
        """
        self.game.set_board([0, 1, 2, 3, 4, 5, 6])
        self.game.apply_move(1)
        self.assertEqual(str(self.game), '[6, 5, 4, 3, 2, 0, 1]')
        self.game.apply_move(2)
        self.assertEqual(str(self.game), '[6, 5, 4, 3, 0, 1, 2]')
        self.game.apply_move(3)
        self.assertEqual(str(self.game), '[6, 5, 4, 0, 1, 2, 3]')
        self.game.apply_move(4)
        self.assertEqual(str(self.game), '[6, 5, 0, 1, 2, 3, 4]')
        self.game.apply_move(5)
        self.assertEqual(str(self.game), '[6, 0, 1, 2, 3, 4, 5]')
        self.game.apply_move(6)
        self.assertEqual(str(self.game), '[0, 1, 2, 3, 4, 5, 6]')

    def test_choose_move(self):
        """
        Test whether choose_move chooses the correct move
        """
        self.game.set_board([0, 1, 2, 3, 4, 5, 6])
        self.assertEqual(self.game.choose_move(), 1)
        self.game.set_board([0, 0, 2, 3, 4, 5, 6])
        self.assertEqual(self.game.choose_move(), 2)
        self.game.set_board([0, 0, 1, 3, 4, 5, 6])
        self.assertEqual(self.game.choose_move(), 3)
        self.game.set_board([0, 0, 1, 2, 4, 5, 6])
        self.assertEqual(self.game.choose_move(), 4)
        self.game.set_board([0, 0, 1, 2, 3, 5, 6])
        self.assertEqual(self.game.choose_move(), 5)
        self.game.set_board([0, 0, 1, 2, 3, 4, 6])
        self.assertEqual(self.game.choose_move(), 6)
        self.game.set_board([0, 0, 1, 2, 3, 4, 5])
        self.assertEqual(self.game.choose_move(), 0)
        self.game.set_board([6, 0, 0, 0, 0, 0, 0])
        self.assertEqual(self.game.choose_move(), 0)


if __name__ == '__main__':
    unittest.main()
