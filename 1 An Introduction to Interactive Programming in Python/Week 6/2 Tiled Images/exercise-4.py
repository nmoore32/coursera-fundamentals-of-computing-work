##
# Write a function assign that takes a list of Student objecs, a student full name, a password,
# and a project as parameters. The function should search the list of students for students whose
# name and password match the supplied information. When a match is found, the function checks
# the student's current list of prjects for the supplied prohect. If the project does not already
# exist in the list, the function adds the project to the list.
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


class Student:

    def __init__(self, person, pwd):
        self.person = person
        self.password = pwd
        self.projects = []

    def get_name(self):
        return self.person.full_name()

    def check_password(self, pwd):
        return pwd == self.password

    def get_projects(self):
        return self.projects

    def add_project(self, project):
        self.projects.append(project)


def assign(students, name, pwd, project):
    for student in students:
        if name == student.person.full_name() and pwd == student.password:
            if project not in student.projects:
                student.add_project(project)


# Testing code

# create some Student objects using Person object
joe = Student(Person("Joe", "Warren", 52), "TopSecret")
joe.add_project("Create practice exercises")
joe.add_project("Implement Minecraft")

scott = Student(Person("Scott", "Rixner", 29), "CodeSkulptor")
scott.add_project("Beat Joe at RiceRocks")

john = Student(Person("John", "Greiner", 47), "outdoors")


# create a list of students
profs = [joe, scott, john]

# test assign
print(joe.get_projects())
assign(profs, "Joe Warren", "TopSecret", "Practice RiceRocks")
print(joe.get_projects())

print(john.get_projects())
assign(profs, "John Greiner", "OUTDOORS", "Work on reflexes")
print(john.get_projects())
assign(profs, "John Greiner", "outdoors", "Work on reflexes")
print(john.get_projects())
