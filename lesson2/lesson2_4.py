#!/usr/bin/python3

user_string = input("Please enter a string with words:\n").split()
print("your string with numbers:")
for index,val in enumerate(user_string, 1):
    print(index,val[0:10])
