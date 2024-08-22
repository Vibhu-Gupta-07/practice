<<<<<<< HEAD

'''

Write a program to print the following star pattern.
* * *
*   *    for n = 3
* * *

'''

n = 4
for i in range (1,n+1):
    if(i==1 or i==n):
        print("* " *n,end="")
    else:
        print("* ",end="")
        print("  "* (n-2),end="")
        print("* ",end="")
    print("")
=======

'''

Write a program to print the following star pattern.
* * *
*   *    for n = 3
* * *

'''

n = 4
for i in range (1,n+1):
    if(i==1 or i==n):
        print("* " *n,end="")
    else:
        print("* ",end="")
        print("  "* (n-2),end="")
        print("* ",end="")
    print("")
>>>>>>> 99a1cafa93f0df4171e270c79c0de78744a77b8e
