##
# Write a function average_age that takes a list of Person objects along with the current
# year and returns the average age.
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


def average_age(persons, current_year):
    sum = 0
    for person in persons:
        sum += person.age(current_year)
    return sum / len(persons)


joe = Person("Joe", "Warren", 1961)
john = Person("John", "Greiner", 1966)
stephen = Person("Stephen", "Wong", 1960)
scott = Person("Scott", "Rixner", 1987)

instructors = [joe, john, stephen, scott]
print(average_age(instructors, 2013))

instructors.pop()
print(average_age(instructors, 2013))
