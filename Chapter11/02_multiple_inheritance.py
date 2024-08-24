class Employee:
    company = "ITC"
    salary = "123939"
    def show(self):
        print(f"The name of the Employee is {self.company} and the salary is {self.salary}")


class Coder:
    language = "python"
    def printLanguages(self):
        print(f"Out of all the language here is your language {self.language}") 



class Programmer(Employee,Coder):
    Company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language}language")



a = Employee()
b = Programmer()

print(a.company,b.Company)

b.show()
b.printLanguages()
b.showLanguage()