##
# Write a function that takes an integer number of seconds in range (0, 3600) and
# outputs a string with number of minutes and seconds
# .


def format_time(seconds):
    return f"Minutes: {seconds // 60}  Seconds: {seconds % 60}"


print(format_time(10))
print(format_time(30))
print(format_time(60))
print(format_time(70))
print(format_time(610))
print(format_time(2000))
