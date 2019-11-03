#!/usr/bin/python3
def capital(user_string):
    '''Returns capitalized string'''
    return user_string.capitalize()

user_string = input("please enter a string of words:\n").split()
#print(f"{capital('text')}")
#print(user_string)
print("string with capitalized words:")
for word in user_string:
    print(capital(word), end = ' ')
print("\n")
