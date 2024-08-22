<<<<<<< HEAD
'''
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

=======
'''
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

>>>>>>> 99a1cafa93f0df4171e270c79c0de78744a77b8e
pattern(4)