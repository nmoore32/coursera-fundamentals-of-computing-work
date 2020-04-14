def smaller_root(a, b, c):
    '''Returns the smaller root of a quadratic equation if it exists'''
    discrim = b ** 2 - (4 * a * c)
    if discrim < 0:
        print("Error: No real solutions")
        return
    else:
        return (-b - discrim ** 0.5) / (2 * a)


print(smaller_root(1, 2, 3))
print(smaller_root(2, 0, -10))
print(smaller_root(6, -3, 5))
