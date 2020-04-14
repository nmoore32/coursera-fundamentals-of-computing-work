def is_leap_year(year):
    '''Determines whether a year is a leap year'''
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


print(is_leap_year(2020))
