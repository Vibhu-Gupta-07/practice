try: 
    a = int (input("Hey, enter a number"))
    print(a)

except ValueError as v :
    print("Hello ")
    print (v) 

except Exception as e:
    print(e)

print("thank you")
