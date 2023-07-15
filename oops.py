class SuperHeroes():
    def __init__(self, name, superpower):
        self.name = name
        self.superpower = superpower

    def get_superpower(self):
        print(f"I am {self.name} and my superpower is {self.superpower}")

ironMan = SuperHeroes(name="IronMan", superpower="Engineering")

# print(ironMan.name)
# print(ironMan.superpower)
ironMan.get_superpower()



# Create a class representing a classroom
# Take a student list as an attribute
# the list will look like this:["Aditya", "Sneha", "Rahul", etc...]
# Create a method that can print all the students

class Classroom():
    def __init__(self, students_list):
        self.students_list = students_list

    def print_students(self):
        print(self.students_list)

classroom = Classroom(students_list=["Aditya", "Sneha", "Anuska"])
classroom.print_students()

sectionA = Classroom(students_list=["Tanmoy", "Rahul", "Akash"])
sectionA.print_students()