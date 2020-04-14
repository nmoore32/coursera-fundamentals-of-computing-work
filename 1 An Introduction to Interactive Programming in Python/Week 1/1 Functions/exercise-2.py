'''Calculates total seconds given a number of hours, minutes, and seconds'''


def total_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


print(total_seconds(7, 21, 37))
