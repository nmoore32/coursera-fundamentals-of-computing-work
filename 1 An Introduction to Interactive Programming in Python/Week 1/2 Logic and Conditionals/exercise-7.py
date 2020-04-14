def print_digits(number):
    '''Determines which digits are in the tens and ones place given a two-digit positive integer'''
    if number < 0 or number >= 100:
        print("Error: Input is not a two-digit number")
    else:
        print(
            f"The tens digit is {number // 10}, and the ones digit is {number % 10}.")


print_digits(27)
