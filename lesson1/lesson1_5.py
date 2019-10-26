#!/usr/bin/python3

revenue = int(input("please enter revenue value: "))
costs = int(input("please enter costs value: "))
if revenue > costs:
    print("Congratulations! Your firm works with profit!")
    stuff = int(input("Please enter how many persons are working: ")) 
    profitability = (revenue - costs) / stuff
    print(f"Your profit per 1 person is {profitability}")
elif revenue == costs:
    print("Alarm! Your firm works with zero effect!")
else:
    print("Alarm! Your firm has losses!")
