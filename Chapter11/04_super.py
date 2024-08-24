class Employee:
    def __init__(self):
        print("COnstructor of employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("COnstructor of programmer")
    b = 2

class manager(Programmer):
    def __init__(self):
        super().__init__()
        print("COnstructor of manager")
    c = 3

o = Employee()
print(o.a)


o = Programmer()
print(o.a, o.b)

o = manager()
print(o.a, o.b, o.c)