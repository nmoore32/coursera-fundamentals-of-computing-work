x0, y0 = 0, 0
x1, y1 = 3, 4
x2, y2 = 1, 1

a = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
b = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
c = ((x2 - x0) ** 2 + (y2 - y0) ** 2) ** 0.5
s = 0.5 * (a + b + c)
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(area)
