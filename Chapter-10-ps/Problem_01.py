# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = programmer("Harry",1200000,295639)
print(p.name, p.salary, p.pincode, p.company)
r = programmer("Rohan",1100000,298569)
print(r.name, r.salary, r.pincode, r.company)