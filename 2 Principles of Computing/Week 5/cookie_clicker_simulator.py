"""
Cookie Clicker Simulator
"""
from math import ceil, inf
from build_info import BuildInfo

# Constants
SIM_TIME = 10000000000.0


class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self._total_cookies_produced = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._current_CPS = 1.0  # CPS = cookies per second
        # List of tuples containing (time of item purchase, item, cost of item, total cookies produced)
        self._history = [(0, 0, None, 0.0, 0.0)]

    def __str__(self):
        """
        Return human readable state
        """
        return_string = (f"\nTotal cookies produced: {self._total_cookies_produced:.1f}\n" +
                         f"Current cookies: {self._current_cookies:.1f}\n" +
                         f"Current time: {self._current_time:.1f}\n" +
                         f"Current CPS: {self._current_CPS:.1f}\n")
        return return_string

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self._current_cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_CPS

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self._history.copy()

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._current_cookies >= cookies:
            return 0.0
        else:
            # Round up to nearest integer with ceil, then convert resulting int to float
            return float(ceil((cookies - self._current_cookies) / self._current_CPS))

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time <= 0.0:
            return
        else:
            self._current_time += time
            self._current_cookies += time * self._current_CPS
            self._total_cookies_produced += time * self._current_CPS

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies < cost:
            return
        else:
            self._current_cookies -= cost
            self._current_CPS += additional_cps
            self._history.append(
                (self._current_time, item_name, cost, self._total_cookies_produced))


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    new_build_info = build_info.clone()
    clicker = ClickerState()

    # As long as there is enough time to save up for more expensive buildings do the following
    while clicker.get_time() < duration:
        # Determine the best item to buy given the time left
        time_left = duration - clicker.get_time()
        next_item = strategy(clicker.get_cookies(), clicker.get_cps(),
                             clicker.get_history(), time_left, new_build_info)

        # If there is no item returned by the strategy for the time left, or there is not enough
        # time to save up to buy the next item, exit the loop
        if not next_item:
            break
        time_until_next = clicker.time_until(
            new_build_info.get_cost(next_item))
        if time_until_next > duration:
            break

        # Advance time until the next item is affordable, buy it, and update the building info
        # (The cost to buy the next building of the same type increases with each purchase)
        cost = new_build_info.get_cost(next_item)
        clicker.wait(time_until_next)
        clicker.buy_item(next_item, cost, new_build_info.get_cps(next_item))
        new_build_info.update_item(next_item)

    # If there isn't enough time left for the selected strategy to function properly within the remaining time
    # repeatedly call that strategy with 0 time left to determine how best to use remaining time
    next_item = strategy(clicker.get_cookies(), clicker.get_cps(),
                         clicker.get_history(), 0, new_build_info)
    while next_item and clicker.get_cookies() >= new_build_info.get_cost(next_item):
        cost = new_build_info.get_cost(next_item)
        clicker.buy_item(next_item, cost, new_build_info.get_cps(next_item))
        new_build_info.update_item(next_item)
        next_item = strategy(clicker.get_cookies(), clicker.get_cps(),
                             clicker.get_history(), 0, new_build_info)
    # If the first while loop ended before duration, accumulate cookies based on current cps until time up
    clicker.wait(duration - clicker.get_time())

    return clicker


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"


def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None


def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    cheapest_cost = inf
    cheapest_item = None
    for item in build_info.build_items():
        cost = build_info.get_cost(item)
        if cost < cheapest_cost and cookies + cps * time_left >= cost:
            cheapest_cost = cost
            cheapest_item = item
    return cheapest_item


def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    largest_cost = 0.0
    expensive_item = None
    for item in build_info.build_items():
        cost = build_info.get_cost(item)
        if cost > largest_cost and (cookies + cps * time_left) >= cost:
            largest_cost = cost
            expensive_item = item
    return expensive_item


def strategy_best(cookies, cps, history, time_left, build_info):
    """
    Always return the item that (i) has the highest cps / cost value and (ii) is affordable in
    the remaining time. 
    """
    best_cps_per_cost = 0.0  # Highest return value scaled by item cost
    best_item = None
    for item in build_info.build_items():
        cost = build_info.get_cost(item)
        item_cps = build_info.get_cps(item)
        cps_per_cost = item_cps / cost
        time_until = (cost - cookies) / cps
        if cps_per_cost > best_cps_per_cost and cookies + cps * time_left >= cost:
            best_cps_per_cost = cps_per_cost
            best_item = item
    return best_item

# Tests

# print(simulate_clicker(BuildInfo(), SIM_TIME, strategy_cursor_broken))
# Output should be
# Total cookies produced: 153308849165.9
# Current cookies: 6965195661.5
# Current time: 10000000000.0
# Current CPS: 16.1


# print(simulate_clicker(BuildInfo(), 1000, strategy_cheap))
# Output should be
# Total cookies produced: 3897.7
# Current cookies: 154.6
# Current time: 1000.0
# Current CPS: 7.7

# print(simulate_clicker(BuildInfo(), 1000, strategy_expensive))
# Output should be
# Total cookies produced: 5124.1
# Current cookies: 8.4
# Current time: 1000.0
# Current CPS: 24.7


# Some results

# print(simulate_clicker(BuildInfo(), SIM_TIME, strategy_cheap))
# Total cookies produced: 1152859356212787584.0
# Current cookies: 149360255735977.9
# Current time: 10000000000.0
# Current CPS: 123436706.3

# print(simulate_clicker(BuildInfo(), SIM_TIME, strategy_expensive))
# Total cookies produced: 683676443442532096.0
# Current cookies: 2414.6
# Current time: 10000000000.0
# Current CPS: 133980795.7

# print(simulate_clicker(BuildInfo(), SIM_TIME, strategy_best))
# Total cookies produced: 1314018864995952384.0
# Current cookies: 57028878943.2
# Current time: 10000000000.0
# Current CPS: 140318078.7
