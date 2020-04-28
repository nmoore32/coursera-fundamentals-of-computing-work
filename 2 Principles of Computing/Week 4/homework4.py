"""
Functions to enumerate sequences of outcomes
Repetition of outcomes is allowed
"""
from math import factorial


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


def gen_sorted_sequences(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences
    """
    all_sequences = gen_all_sequences(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)


def gen_all_permuations(outcomes, length):
    """
    Function that determines all the permuations of outcomes of a specified length
    """
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                if item not in new_seq:
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
        ans = temp
    return ans


def gen_all_powersets(seq):
    """
    Recursively generates and returns the set of all subsets (the powerset) of a given set
    """
    # Basically, the function starts with a set containing only the empty set
    # and generates new subsets by iterating through the elements of the original set
    # and adding each element to each previously generated subset

    # So for the set (1, 2, 3, 4, 5)
    # Once it reaches the end of the recursive calls, it returns the empty set
    # Then it adds and (), (5) to the powersets and returns that
    # then it adds to the new powerset (one level up) and also adds (4) and (4, 5)
    # So the next returned set contains (), (4), (5), and (4, 5)
    # Then the next contains (), (3), (4), (5), (3, 4), (3, 5), and (3, 4, 5), etc.

    subsets = set([()])
    if len(seq) > 0:
        for subset in gen_all_powersets(seq[1:]):
            # Add each returned subset to list, both with and without the previous element
            new_subset = list(subset)
            subsets.add(tuple(new_subset))
            subsets.add(tuple([seq[0]] + new_subset))
    return subsets


def question1():
    """
    Given the set of outcomes corresponding to a coin flip, how many sequences of
    outcomes of length five (repetition allowed) are possible?
    """
    # Answer is 2^5 = 32
    ans = gen_all_sequences(('Heads', 'Tails'), 5)
    return ans


def question2():
    """
    Consider a sequence of trials in which a fair four-sided die (with faces numbered 1-4)
    is rolled twice. What is the expected value of the product of the two die rolls?
    """
    # Since the die rolls are independent, the expectation value of the product
    # is equal to the product of the expectation values for each die roll
    # Expected value of roll of four-sided = (1 + 2 + 3 + 4) / 4 = 2.5
    # Expected value of product 2.5^2 = 6.25
    sequences = gen_all_sequences((1, 2, 3, 4), 2)
    exp = 0
    for seq in sequences:
        exp += (seq[0] * seq[1]) / len(sequences)
    return exp


def question3():
    """
    Given a trial in which a decimal digit is selected from the list ["0", "1", "2", "3", "4", "5",
    "6", "7", "8", "9"] with equal probability 0.1, consider a five digit string created by a sequence
    of such trials (leading zeros and repeated digits are allowed). What is the probability that
    this five-digit string consisting of five consecutive digits in either ascending or descending
    order (e.g; "34567", or "43210")?
    """
    # Answer is total number of favorable outcomes (12) over total number of outcomes (10^5 = 100,000)
    # anser = 0.00012
    seqs = gen_all_sequences((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 5)
    ascending_count = 0

    for seq in seqs:
        # Zip creates a list of pairs. The second member of each pair is the
        # the next number in the sequence of numbers. So we can check if the
        # sequence is in ascending order by ensuring that the second member
        # of each pair is equal to the first member + 1
        if all(prev + 1 == next for prev, next in zip(seq, seq[1:])):
            ascending_count += 1

    # Number of descending possibilites equal to number of ascending
    total_count = 2 * ascending_count
    # Number of favorable outcomes over total number of outcomes
    ans = total_count / len(seqs)
    return ans


def question4():
    """
    Given a trial in which five digit strings are formed as permutations of the digits
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]. (In this case, repetition of the digits
    is not allowed.) If the probability of each permutation is the same, what is the probability
    that this five digits string consists of consecutive digits in either ascending or
    descenind order (e.g; "34567", or "43210")?
    """
    # Answer is total number of favorable outcomes (12) over
    # total number of outcomes (m! / (m - n)!) where m is number of items and n is length
    # # total outcomes = 10 x 9 x 8 x 7 x 6 = 30240
    # probability = 12 / 30240 = 0.0003968
    seqs = gen_all_permuations((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 5)
    ascending_count = 0

    for seq in seqs:
        if all(prev + 1 == next for prev, next in zip(seq, seq[1:])):
            ascending_count += 1

    total_count = 2 * ascending_count
    ans = total_count / len(seqs)
    return ans


def question7():
    """
    If the set T has n members, how many distinct sets S are subsets of T? You may want
    to figure out the answer for a few specfic values of n first.
    This prints out the lengths of the powersets for sets with 1 to 5 elements
    """
    # The resulting pattern makes it clear that the answer is 2^n
    # But you can also determine that this is answer by noting that each element can
    # either be present or absent (2 possibilities) from a given subset.
    # The number of possible subsets is 2 x 2 x 2 x 2 .... n times for a set with n elements
    # Say we have set (1, 2, 3)
    # We have the subsets (), (1) where 1 is either present or absent (2 subsets)
    # We double the number of subsets when we consider whether 2 is present or absent
    # (), (1), (2), (1, 2) (4 subsets)
    # (), (1), (2), (3), (1, 2), (1, 3), (2, 3), (1, 2, 3) (8 subsets)
    #
    print(len(gen_all_powersets(([1]))))
    print(len(gen_all_powersets((1, 2))))
    print(len(gen_all_powersets((1, 2, 3))))
    print(len(gen_all_powersets((1, 2, 3, 4))))
    print(len(gen_all_powersets((1, 2, 3, 4, 5))))


def question8():
    """
    Given a standard 52 card deck of playing cards, what is the probability
    of being dealt a five card hand of the same suit?
    """
    # Number of permuntations given m outcomes and n choices - m! / (m - n)!
    # Number of combinations given m outcomes and n choices - m! / (m-n)!n!

    # Simply using the formula gives
    #favorable_combinations = factorial(13) / (factorial(13 - 5) * factorial(5))
    #total_combinations = factorial(52) / (factorial(52 - 5) * factorial(5))

    # But this is computationally wasteful, it would be better to simplify the expressions
    favorable_combinations = 1 / factorial(5)
    for idx in range(13, 8, -1):
        favorable_combinations *= idx
    total_combinations = 1 / factorial(5)
    for idx in range(52, 47, -1):
        total_combinations *= idx

    return favorable_combinations / total_combinations


def question9():
    """
    Pascal's triangle is an triangular array of numbers in which the entry on one row
    of the triangle corresponds to the sum of the two entries directly above the entry.

    Determine a math expression in m and n using factorial that represents the value
    of the nth entry of the mth row of Pascal's triangle. (Both the row numbers and
    entry numbers are indexed starting at zero.)
    """
    # Looking at the first few rows of the triangle it appears that something like
    # m! / n! works for the first few entries but then is a little too big for the next ones
    # but since 0! = 1! = 1, division by (m - n)! will not change the result for the first
    # few entries and may give the correct result of further entries

    # m! / n! (m-n)!    this is, in fact, the correct answer, the problem is fairly
    # straightforward given the starting hint to find a formula using m, n, and factorials


print(f"Question 1: {len(question1())}")
print(f"Question 2: {question2()}")
print(f"Question 3: {question3()}")
print(f"Question 4: {question4()}")
print("Question 5: This question was to create function to determine permuations")
print("Question 6 not included as not a coding question")
print("Question 7: 2^n subsets")
print(f"Question 8: {question8()}")
