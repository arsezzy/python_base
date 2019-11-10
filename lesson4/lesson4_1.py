#!/usr/bin/python3

from sys import argv

def salary(coef):
    hours, rate, bonus = coef
    return hours * rate + bonus

print(f"current salary is {salary(list(map(int,argv[1:4])))}")
