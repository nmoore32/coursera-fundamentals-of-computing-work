##
# Write a function that takes a list of strings as input and returns a single string
# concatenating all the string in the list
#


def string_list_join(string_list):
    return_string = ''
    for string in string_list:
        return_string = return_string + string
    return return_string


print(string_list_join([]))
print(string_list_join(["pig", "dog"]))
print(string_list_join(["spam", " and ", "eggs"]))
print(string_list_join(["a", "b", "c", "d"]))
