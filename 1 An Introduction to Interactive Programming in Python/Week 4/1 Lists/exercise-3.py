##
# Write a function add_vector(v, w) that adds two 2D vectors and returns the result
#


def add_vector(v, w):
    return [v[0] + w[0], v[1] + w[1]]


print(add_vector([0, 0], [1, 2]))
print(add_vector([1, 2], [1, -1]))
