#!/usr/bin/python3

initial_list = [1, 7, 1, 9, 2, 2, 3, 5, 3, 4, 8, 6, 1, 8]
uniq_list = list(el for el in initial_list if initial_list.count(el) == 1)
print(f"list with uniq digits is {uniq_list}")
