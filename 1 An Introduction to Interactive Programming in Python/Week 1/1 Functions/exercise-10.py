def point_distance(x0, y0, x1, y1):
    '''Calculates distance between two points'''
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5


print(point_distance(2, 2, 5, 6))
