<<<<<<< HEAD
# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user

marks_1 = int(input("Enter marks of First subject : "))
marks_2 = int(input("Enter marks of Second subject : "))
marks_3 = int(input("Enter marks of Third subject : "))

Total_Percentage = (100*(marks_1 +marks_2+marks_3))/300

if(Total_Percentage >= 40 and marks_1 >= 33 and marks_2 >=33 and marks_3 >=33):
    print("your are passed",Total_Percentage)

else:
=======
# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user

marks_1 = int(input("Enter marks of First subject : "))
marks_2 = int(input("Enter marks of Second subject : "))
marks_3 = int(input("Enter marks of Third subject : "))

Total_Percentage = (100*(marks_1 +marks_2+marks_3))/300

if(Total_Percentage >= 40 and marks_1 >= 33 and marks_2 >=33 and marks_3 >=33):
    print("your are passed",Total_Percentage)

else:
>>>>>>> 99a1cafa93f0df4171e270c79c0de78744a77b8e
    print("Try again you are failed",Total_Percentage)