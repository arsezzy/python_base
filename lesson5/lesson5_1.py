#!/usr/bin/python3

user_input = 'initial_string'
with open("lesson5_1.txt", "w") as task5_1:
    while user_input:
        user_input = input("Please enter new line. " 
                           "For exit enter empty line\n")
        print(user_input, file = task5_1) 
