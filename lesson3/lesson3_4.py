#!/usr/bin/python3

def power_first(x, y):
    '''return x in power y, first variant'''
    return round(x ** y,4)

def power_second(x, y):
    ''' return x in power y, second variant'''
    power = x
    for i in range(abs(y)-1):
        power *= x    
        print(f"current power is {power}")
    return round(1 / power,4)


while True:
    a = float(input("please enter the positive digit:\n"))
    if a > 0:
        break
    else:
        print("digit is not positive, try again")
while True:
    b = int(input("please enter the negative integer:\n"))
    if b < 0:
        break
    else:
        print("digit is not negative, try again")
print(f"first variant is {power_first(a,b)}")
print(f"second variant is {power_second(a,b)}") 
