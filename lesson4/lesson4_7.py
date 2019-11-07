#!/usr/bin/python3

from math import factorial

MAX_DIGIT = 16
def fibo_gen():
    for el in range(1,MAX_DIGIT):
        yield factorial(el)

for el in fibo_gen():
    print(el)
