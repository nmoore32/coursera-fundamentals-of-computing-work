"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    scores = {}
    for die in hand:
        if die in scores:
            scores[die] += die
        else:
            scores[die] = die
    return max(scores.values())


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    exp_value = 0
    # Make list of outcomes to use to generate all possible final hands
    outcomes = [idx + 1 for idx in range(num_die_sides)]
    final_hands = [held_dice +
                   seq for seq in gen_all_sequences(outcomes, num_free_dice)]
    # Sum up the expected values for each possible final hand
    for hand in final_hands:
        # The float() here is to ensure python 2 also runs the program correctly
        exp_value += float(score(hand)) / len(final_hands)
    return exp_value


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    # Subset isn't, strictly speaking, the right word to use since repeated elements
    # are allowed. But the function is very similiar to a function that takes a set
    # and returns its powerset
    subsets = set([()])
    if len(hand) > 0:
        for subset in gen_all_holds(hand[1:]):
            new_subset = list(subset)
            subsets.add(tuple(new_subset))
            subsets.add(tuple(sorted([hand[0]] + new_subset)))
    return subsets


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    best_hold = (0.0, ())
    for hold in gen_all_holds(hand):
        exp_value = expected_value(hold, num_die_sides, len(hand) - len(hold))
        if exp_value > best_hold[0]:
            best_hold = (exp_value, hold)
    return best_hold


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print("Best strategy for hand", hand, "is to hold",
          hold, "with expected score", hand_score)


print(expected_value((2, 2), 6, 2))
print(strategy((1,), 6))
