def is_lunchtime(hour, is_am):
    '''Determines whether it is lunch time given an integer reprsenting the hour and a boolean
    representing whether its am or pm'''
    return not is_am and hour == 12


print(is_lunchtime(12, True))
print(is_lunchtime(12, False))
print(is_lunchtime(11, False))
