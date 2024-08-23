# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class demo:
    a = 4 

o = demo() # Prints tha class atribute because instance attribute if not present 
print(o.a)

o.a = 0 # Instance attribute is set 
print(o.a)# prints teh instance attribute because instance attribuete is present

print(demo.a)# Prinst the class attribute 