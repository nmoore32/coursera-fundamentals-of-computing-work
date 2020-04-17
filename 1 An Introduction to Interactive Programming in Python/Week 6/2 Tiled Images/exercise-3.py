##
# Implement a Student class which has the fields person, password, and projects.
# It should have the following methods __init__, get_name, check_password, get_projects,
# and add_project(project_name)
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


joe_person = Person("Joe", "Warren", 52)
joe_student = Student(joe_person, "TopSecret")

print(joe_student.get_name())
print(joe_student.check_password("qwert"))
print(joe_student.check_password("TopSecret"))

print(joe_student.get_projects())
joe_student.add_project("Create practice exercises")
print(joe_student.get_projects())
joe_student.add_project("Implement Minecraft")
print(joe_student.get_projects())
