a = int (input("Hey, enter a number"))
b = int (input("Hey enter second number"))

if(b==0):
    raise ZeroDivisionError("Hey our programm is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")