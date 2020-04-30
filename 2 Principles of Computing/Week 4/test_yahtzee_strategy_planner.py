"""
Test suite for Yahtzee Strategy Planner (YPS)
"""
import unittest

from yahtzee_strategy_planner import score, expected_value, gen_all_holds, gen_all_sequences, strategy


class TestYSP(unittest.TestCase):
    """
    Series of tests for Yahtzee Strategy Planner
    """

    def test_score(self):
        """
        Test the the score function returns the proper score for a hand
        """
        self.assertEqual(score([1, 2, 3, 4, 5, 6]), 6)
        self.assertEqual(score([1, 1, 1, 1, 1, 6]), 6)
        self.assertEqual(score([1, 1, 1, 1, 1, 1]), 6)
        self.assertEqual(score([1, 1, 1, 2, 2, 2]), 6)
        self.assertEqual(score([1, 1, 1, 1, 5, 5]), 10)
        self.assertEqual(score([5, 5, 5, 6, 6, 6]), 18)

    def test_expected_value(self):
        """
        Test that expected value returns the appropriate values
        """
        self.assertEqual(expected_value((1,), 6, 0), 1)
        self.assertEqual(expected_value((1, 1), 6, 0), 2)
        self.assertEqual(expected_value((1, 2), 6, 0), 2)
        self.assertAlmostEqual(expected_value((1,), 6, 1), 3.6666666666666665)
        self.assertAlmostEqual(expected_value((2,), 6, 1), 4)
        self.assertAlmostEqual(expected_value((3,), 6, 1), 4.5)
        self.assertAlmostEqual(expected_value((4,), 6, 1), 5.166666667)
        self.assertAlmostEqual(expected_value((5,), 6, 1), 6)
        self.assertAlmostEqual(expected_value((6,), 6, 1), 7)
        self.assertAlmostEqual(expected_value((1,), 2, 2), 2.75)
        self.assertEqual(expected_value((6, 6, 6, 6, 6), 6, 0), 30)
        self.assertAlmostEqual(expected_value((6, 6, 6, 6), 6, 1), 25)

    def test_gen_all_holds(self):
        """
        Test that gen_all_holds generates each unique combination of dice
        that can be held from a given hand
        """
        self.assertEqual(gen_all_holds([1]), set({(), (1,)}))
        self.assertEqual(gen_all_holds([1, 1]), set({(), (1,), (1, 1)}))
        self.assertEqual(gen_all_holds([1, 2]), set({(), (1,), (2,), (1, 2)}))
        self.assertEqual(gen_all_holds([1, 1, 1]), set(
            {(), (1,), (1, 1), (1, 1, 1)}))
        self.assertEqual(gen_all_holds([1, 2, 3]), set(
            {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}))

    def test_strategy(self):
        """
        Test that strategy returns the appropriate strategy
        """
        self.assertEqual(strategy((6, 6, 6, 6, 1), 6), (25.0, (6, 6, 6, 6)))
        self.assertEqual(strategy((6, 6, 6, 6, 5), 6), (25.0, (6, 6, 6, 6)))
        self.assertEqual(strategy((6, 6, 6, 6, 6), 6), (30.0, (6, 6, 6, 6, 6)))
        self.assertEqual(strategy((6, 6, 6, 5, 5), 6), (20.0, (6, 6, 6)))
        self.assertAlmostEqual(strategy((6, 6, 5, 5, 5), 6)[0], 16.66666667)
        self.assertEqual(strategy((6, 6, 5, 5, 5), 6)[1], (5, 5, 5))


if __name__ == '__main__':
    unittest.main()
