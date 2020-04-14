def name_and_age(name, age):
    '''Returns sentence stating name and age'''
    if age < 0:
        return "Error: Invalid age"
    else:
        return f"{name} is {age} years old."


print(name_and_age('Joe Warren', 52))
print(name_and_age('Joe Warren', -1))
