<<<<<<< HEAD
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("enter the value: "))

=======
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("enter the value: "))

>>>>>>> 99a1cafa93f0df4171e270c79c0de78744a77b8e
print(f"The factorial of the {n} is: {factorial(n)}")