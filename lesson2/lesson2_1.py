#!/usr/bin/python3

list1 = ['word', 1, 2.0, None, (1,2), {1:"one", 2:"two"}, False]
for val in list1:
    print(f"{val} is {type(val)}")
