#!/usr/bin/python3

from itertools import cycle

user_list = ['a', 'b', 'c', 'd', 'e']
for el in cycle(user_list):
    print(el)
