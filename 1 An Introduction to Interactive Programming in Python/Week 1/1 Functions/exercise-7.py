'''Calculate new balance after compound interest'''


def future_value(present_value, annual_rate, years):
    return present_value * (1 + 0.01 * annual_rate) ** years


print(future_value(1000, 7, 10))
