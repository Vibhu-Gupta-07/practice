<<<<<<< HEAD
# Write a recursive function to calculate the sum of first n natural numbers

def sum(n):
    if (n==1):
        return 1
    return sum(n-1) +n
    

n = int(input("Enter the value:"))
=======
# Write a recursive function to calculate the sum of first n natural numbers

def sum(n):
    if (n==1):
        return 1
    return sum(n-1) +n
    

n = int(input("Enter the value:"))
>>>>>>> 99a1cafa93f0df4171e270c79c0de78744a77b8e
print(f"{sum(n)} that is the sum of the n number ")