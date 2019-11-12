#!/usr/bin/python3

from random import random, randint

with open("lesson5_5.txt", "w") as lesson5_5:
    for i in range(0, 10):
        print(randint(0, 100), file = lesson5_5, end = " ")

with open("lesson5_5.txt", "r") as lesson5_5:    
    print(f"Total sum is {sum(list(map(int, lesson5_5.readline().split())))}")
