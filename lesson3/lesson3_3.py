#!/usr/bin/python3

def sum_two(a, b, c):
    '''returns sum of two maximum elements'''
    sum_list = a, b, c
    return sum(sum_list) - min(sum_list)

a = int(input("Please enter the first digit:\n"))
b = int(input("Please enter the second digit:\n"))
c = int(input("Please enter the third digit:\n"))
print(sum_two(a,b,c))
