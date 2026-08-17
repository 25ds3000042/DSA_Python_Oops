class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    def study(self):
        print(self.name, "is studying Python")


# Creating objects
student1 = Student("Rahul", 21, "Data Science")
student2 = Student("Anita", 22, "Artificial Intelligence")

# Calling methods
student1.display()
student1.study()

print()

student2.display()
student2.study()
