#!/usr/bin/python3

user_int = input("please enter an integer:\n")
digit = 9
while digit > 0:
    if str(digit) in user_int:
        break
    else:
        digit-=1
print(f"Maximum digit in {user_int} is {digit}")    
