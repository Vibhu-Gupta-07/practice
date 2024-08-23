class Employee:
    language = "Python"
    salary = 150000

    def __init__(self,name,salary,language):
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry = Employee("Harry",1200000,"java")
# harry.name = "Harry"
print(harry.name,harry.salary,harry.language)

# rohan = Employee()