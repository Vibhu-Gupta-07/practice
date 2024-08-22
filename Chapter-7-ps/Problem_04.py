<<<<<<< HEAD
# Write a program to find whether a given number is prime or not
n = int(input("Enter the number you want to try :"))

for i in range (0,n):
    n = int(input("Enter the number to check the number is  prime or not: "))
    
    for i in range(2,n):
        if(n%i) == 0:
            print("Number is not prime")
            break

    else:
=======
# Write a program to find whether a given number is prime or not
n = int(input("Enter the number you want to try :"))

for i in range (0,n):
    n = int(input("Enter the number to check the number is  prime or not: "))
    
    for i in range(2,n):
        if(n%i) == 0:
            print("Number is not prime")
            break

    else:
>>>>>>> 99a1cafa93f0df4171e270c79c0de78744a77b8e
        print("It is a prime number")