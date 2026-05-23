class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)

s1 = Student("Gopi", 19)
s1.show()
