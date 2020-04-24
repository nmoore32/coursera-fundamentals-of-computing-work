"""
Test suite for twenty_forty_eight.py
"""
import unittest

from twenty_fourty_eight import TwentyFortyEight
from twenty_fourty_eight import merge
from twenty_fourty_eight import UP, DOWN, LEFT, RIGHT


class TestTwentyFortyEight(unittest.TestCase):
    """
    Series of tests for twenty_forty_eight
    """

    def test_merge(self):
        """
        Test the merge helper function for 2048
        """
        self.assertEqual(merge([2, 0, 2, 4]), [4, 4, 0, 0])
        self.assertEqual(merge([0, 0, 2, 2]), [4, 0, 0, 0])
        self.assertEqual(merge([2, 2, 0, 0]), [4, 0, 0, 0])
        self.assertEqual(merge([2, 2, 2, 2, 2]), [4, 4, 2, 0, 0])
        self.assertEqual(merge([8, 16, 16, 8]), [8, 32, 8, 0])
        self.assertEqual(merge([]), [])
        self.assertEqual(merge([8]), [8])
        self.assertEqual(merge([8, 4]), [8, 4])

    def setUp(self):
        """
        Create an instance of TwentyFortyEight for each test
        """
        self.game = TwentyFortyEight(5, 4)

    def test_initial_values(self):
        """
        Check that attributes initialize correctly
        (tests __init__(), reset() and _calculcate_indices())
        """
        # Total value of initial tiles should be 4, 6, or 8
        total_value = 0
        for row in self.game._grid:
            total_value += sum(row)
        self.assertIn(total_value, (4, 6, 8))
        self.assertEqual(self.game._grid_height, 5)
        self.assertEqual(self.game._grid_width, 4)
        self.assertEqual(self.game._initial_indices,
                         {1: [(0, 0), (0, 1), (0, 2), (0, 3)],
                          2: [(4, 0), (4, 1), (4, 2), (4, 3)],
                          3: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],
                          4: [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)]})

    def test_new_tile(self):
        """
        Check that new tile adds a new tile of value 2 or 4
        """
        # Adding a new tile increases the sum of all the tiles by 2 or 4
        for dummy_i in range(20):
            current_value = 0
            for row in self.game._grid:
                current_value += sum(row)
            self.game.new_tile()
            new_value = 0
            for row in self.game._grid:
                new_value += sum(row)
            # When dummy_i reaches 17 the board will be full, at the point
            # the new_value should be unchanged when more tiles are added
            if dummy_i < 18:
                self.assertIn(
                    new_value, (current_value + 2, current_value + 4))
            else:
                self.assertEqual(new_value, current_value)

    def test_set_tile(self):
        """
        Test that the set tile functions sets new tiles in the specified location
        """
        for row in range(self.game._grid_height):
            for col in range(self.game._grid_width):
                self.game.set_tile(row, col, 2)
                self.assertEqual(self.game._grid[row][col], 2)

    def test_get_grid(self):
        """
        Test the get_grid_height() and get_grid_width() return correct result
        """
        self.assertEqual(self.game.get_grid_height(), self.game._grid_height)
        self.assertEqual(self.game.get_grid_width(), self.game._grid_width)

    def test_str(self):
        """
        Test that an appropriate string representation of the 2048 is returned
        """
        for row in range(self.game._grid_height):
            for col in range(self.game._grid_width):
                self.game.set_tile(row, col, 0)
        self.assertEqual(str(
            self.game), '[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]')

    def test_get_tile(self):
        """
        Test that get_tile() returns the appropriate value
        """
        self.game.set_tile(0, 0, 2)
        self.assertEqual(self.game.get_tile(0, 0), 2)


if __name__ == '__main__':
    unittest.main()
