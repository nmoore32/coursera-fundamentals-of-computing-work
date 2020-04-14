def interval_intersect(a, b, c, d):
    '''Returns True if the interval [a, b] intersects the interval [c, d]'''
    return c <= b and a <= d


print(interval_intersect(2, 4, 1, 3))
