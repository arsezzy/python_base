#!/usr/bin/python3

class MyException(Exception):
    def __init__(self, text):
        self.text = text


a = int(input("Please enter first digit\n"))
b = int(input("Please enter second digit\n"))
try:
    if b == 0:
        raise MyException("You can't divide on zero!")
    print(f"{a} / {b} = {round(a/b, 2)}")
except MyException as err:
    print(err)
finally:
    print("Program terminated")
