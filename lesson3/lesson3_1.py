#!/usr/bin/python3

def division(a, b):
    '''Returns a on b division result rounded up to hundredths'''
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        return None

a = float(input("Please enter dividend:\n"))
b = float(input("Please enter denominator:\n"))
print(f"{a} is divided on {b} is {division(a,b)}")
