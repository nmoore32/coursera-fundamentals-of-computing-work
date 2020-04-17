##
# Implement a Person class with fields first_name, last_name, and birth_year
#


class Person:

    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def age(self, current_year):
        return current_year - self.birth_year

    def __str__(self):
        return f"The person's name is {self.full_name()}. Their birth year is {self.birth_year}"


joe = Person("Joe", "Warren", 1961)
john = Person("John", "Greiner", 1966)
stephen = Person("Stephen", "Wong", 1960)
scott = Person("Scott", "Rixner", 1987)

print(joe)
print(john)
print(stephen)
print(scott)

print(joe.age(2013))
print(scott.age(2013))
print(john.full_name())
print(stephen.full_name())
