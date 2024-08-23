class Employee:
    language = "python"
    salary = 15000000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


harry = Employee()
harry.language = "Javascript"
# attribute
# harry.getInfo()
Employee.getInfo(harry)