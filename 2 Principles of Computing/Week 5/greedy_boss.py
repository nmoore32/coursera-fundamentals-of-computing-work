"""
Simulator for greedy boss scenario

Your starting salary is $100 a day and you can bribe your boss
to increase it by $100 a day.

The initial bribe cost is $1000.
"""
from math import ceil, log
import matplotlib.pyplot as plt

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000


def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type=STANDARD):
    """
    Simulation of greedy boss
    """

    # initialize necessary local variables
    # Keep track of current day and total earnings, these are the values to be returned
    # Keep track of current savings to determine when the next bribe is affordable
    # Keep track of current salary in order to increment total earnings/savings appropriately
    # Keep track of the current bribe cost
    current_day = 0
    total_earnings = 0
    current_savings = 0
    current_salary = INITIAL_SALARY
    current_bribe_cost = INITIAL_BRIBE_COST

    # define  list consisting of days vs. total salary earned for analysis
    days_vs_earnings = []

    # Each iteration of this while loop simulates one bribe
    while current_day <= days_in_simulation:

        # update list with days vs total salary earned
        # use plot_type to control whether regular or log/log plot
        # Append the current day and total earnings to the return list
        if plot_type == STANDARD:
            days_vs_earnings.append((current_day, total_earnings))
        else:
            if current_day == 0:
                days_vs_earnings.append((0, 0))
            else:
                days_vs_earnings.append(
                    (log(current_day), log(total_earnings)))

        # check whether we have enough money to bribe without waiting
        # Determine how long until the next bribe is affordable
        if current_savings >= current_bribe_cost:
            days_to_next_bribe = 0
        else:
            # Time to next bribe is time needed to earn current_bribe_cost - current_savings
            # given current salary
            # The float is to ensure backwards compatibility with Python 2
            time_to_next_bribe = (current_bribe_cost -
                                  current_savings) / float(current_salary)
            days_to_next_bribe = int(ceil(time_to_next_bribe))

        # advance current_day to day of next bribe (DO NOT INCREMENT BY ONE DAY)
        current_day += days_to_next_bribe

        # update state of simulation to reflect bribe
        total_earnings += days_to_next_bribe * current_salary
        current_savings += (days_to_next_bribe *
                            current_salary - current_bribe_cost)
        current_salary += SALARY_INCREMENT
        current_bribe_cost += bribe_cost_increment

    return days_vs_earnings

# Plotting results


def run_simulation(days_in_simulation, bribe_cost_increment, plot_type=STANDARD):
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    data = greedy_boss(days_in_simulation, bribe_cost_increment, plot_type)
    print(data)
    x_coords = [coords[0] for coords in data]
    y_coords = [coords[1] for coords in data]
    ax.plot(x_coords, y_coords)

    # Format plot
    plt.title('Greedy boss simulation', fontsize=24)
    plt.xlabel('Days', fontsize=16)
    plt.ylabel('Earnings', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


run_simulation(70, 500, plot_type=LOGLOG)

# Tests

#print(greedy_boss(35, 100))
# should print [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700)]

#print(greedy_boss(35, 0))
# should print [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]
