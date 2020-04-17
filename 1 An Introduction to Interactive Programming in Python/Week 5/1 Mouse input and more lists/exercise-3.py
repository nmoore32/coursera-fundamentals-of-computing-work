##
# Write a function that given a day of the week, prints out the index for its position in a list
#
day_list = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]


def day_to_number(day):
    return day_list.index(day)


print(day_to_number("Sunday"))
print(day_to_number("Monday"))
print(day_to_number("Tuesday"))
print(day_to_number("Wednesday"))
print(day_to_number("Thursday"))
print(day_to_number("Friday"))
print(day_to_number("Saturday"))
