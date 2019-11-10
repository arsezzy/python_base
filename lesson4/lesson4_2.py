#!/usr/bin/python3

digit_list = [1, 6, 1, 3, 6, 2, 2, 6, 5, 7, 10, 4]
print(f"Initial list is \n{digit_list}")
#First variant - maybe not a generator ?
#Next element is bigger than previous in final list
print("First variant, next element is bigger than previous in final list")
new_list = []
for el in digit_list:
    try:                      #for including first element from initial list
        if el > new_list[-1]:
            new_list.append(el)
    except IndexError:
        new_list.append(el)
print(new_list)


#second variant
#Next element is bigger than previous in final list
print("Second variant, next element is bigger than previous in final list")
def generator(my_list):
    max = my_list[0] - 1    # for including first element from initial list
    for el in (my_list):
        if el > max:
            max = el
            yield el

print(list(generator(digit_list)))


#Third variant
#Next element is bigger than previous in initial list
print("Third variant, next element is bigger than previous in initial list")
def generator(my_list):
    previous = my_list[0] - 1    # for including first element from initial list
    for el in (my_list):
        if el > previous:
            previous = el
            yield el
        previous = el

print(list(generator(digit_list)))

