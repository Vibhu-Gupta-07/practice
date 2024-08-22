<<<<<<< HEAD
# Write a python function to remove a given word from a list ad strip it at the same time.

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l =["Harry","Rohan","Mohan","an"]
=======
# Write a python function to remove a given word from a list ad strip it at the same time.

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l =["Harry","Rohan","Mohan","an"]
>>>>>>> 99a1cafa93f0df4171e270c79c0de78744a77b8e
print(rem(l,"an"))