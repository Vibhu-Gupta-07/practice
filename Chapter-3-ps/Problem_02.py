<<<<<<< HEAD
# write a program to fill in a letter template given below with name and date
letter = '''Dear <|Name|>,
You are selected! 
<|Date|>'''

=======
# write a program to fill in a letter template given below with name and date
letter = '''Dear <|Name|>,
You are selected! 
<|Date|>'''

>>>>>>> 99a1cafa93f0df4171e270c79c0de78744a77b8e
print(letter.replace("<|Name|>", "Vibhu").replace("<|Date|>" ,"24 July 2032"))