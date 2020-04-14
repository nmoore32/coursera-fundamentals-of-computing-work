def point_distance(x0, y0, x1, y1):
    '''Calculates distance between two points'''
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5


def triangle_area(x0, y0, x1, y1, x2, y2):
    '''Calculates area of triangle given coordinates of vertices using Heron's formula'''
    a = point_distance(x0, y0, x1, y1)
    b = point_distance(x1, y1, x2, y2)
    c = point_distance(x2, y2, x0, y0)
    s = 0.5 * (a + b + c)
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


print(triangle_area(0, 0, 3, 4, 1, 1))
