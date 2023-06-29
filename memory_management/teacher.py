import sys


class Student:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"del method for student {self.name}")


class Teacher:
    def __init__(self):
        self.student1 = Student('Joe')
        self.student2 = Student('Mike')
        self.student3 = Student('Kris')


t1 = Teacher()

st1 = t1.student1

print(sys.getrefcount(st1))

del t1


