#!/usr/bin/python3

from functools import reduce

print(f"multiplication of all even from 100 to 1000 is: \n"
      f"{reduce((lambda x, y: x*y), [el for el in range(100, 1001, 2)])}")

