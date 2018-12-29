class person:
    def __init__(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")

    def display(self):
        print("\n\nName: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


class marks:
    def __init__(self):
        self.stuClass = input("Class: ")
        print("Enter the marks of the respective subjects")
        self.literature = int(input("Literature: "))
        self.math = int(input("Math: "))
        self.biology = int(input("Biology: "))
        self.physics = int(input("Physics: "))

    def display(self):
        print("Study in: ", self.stuClass)
        print("Total Marks: ", self.literature + self.math + self.biology + self.physics)

class student(person, marks):
    def __init__(self):
        person.__init__(self)
        marks.__init__(self)

    def result(self):
        person.display(self)
        marks.display(self)


stu1 = student()
stu2 = student()
stu1.result()
stu2.result()