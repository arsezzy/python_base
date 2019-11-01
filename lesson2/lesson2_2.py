#!/usr/bin/python3
list1 = input("please enter a list, separator - spacebar\n").split(" ")
list_final = list1[::2]
list_odd = list1[1::2]
current_index = 0
while current_index < len(list1) - 1:
    list_final.insert(current_index, list_odd[int(current_index/2)])
    current_index += 2
print(f"Result list is {list_final}")
