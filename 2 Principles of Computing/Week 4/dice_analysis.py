"""
Program to analyze expected value of simple dice game.
You pay $10 to play.
Roll three dice.
You win $200 if you roll triples, get your $10 back if doubles, and lose the $10 otherwise
"""


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """

    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans


def max_repeats(seq):
    """
    Determines the maximum number of times any individual item occurs
    in the sequence
    """
    item_count = [seq.count(item) for item in seq]
    return max(item_count)


def compute_expected_value():
    """
    Compute the expected value (excluding the initial $10, so an answer of $10 corresponds to breaking even)
    """
    all_rolls = gen_all_sequences([1, 2, 3, 4, 5, 6], 3)
    results = [max_repeats(roll) for roll in all_rolls]

    expected_value = 0
    for result in results:
        if result == 2:
            # The probability for getting any given is 1/216 since there are 216 possible results
            expected_value += 10 / 216
        elif result == 3:
            expected_value += 200 / 216
    return expected_value


def run_test():
    """
    Testing
    """
    outcomes = set([1, 2, 3, 4, 5, 6])
    print(
        f"Number of possible outcomes for rolling three dice: {len(gen_all_sequences(outcomes, 3))}")

    print(f"Max repeats for (3, 2, 1) is: {max_repeats([3, 2, 1])}")
    print(f"Max repeats for (3, 3, 1) is: {max_repeats([3, 3, 1])}")
    print(f"Max repeats for (3, 3, 3) is: {max_repeats([3, 3, 3])}")

    print(f"Expected value is: {compute_expected_value()}")


run_test()
