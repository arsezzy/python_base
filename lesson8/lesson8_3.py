#!/usr/bin/python3

class NotDigitException(Exception):
    '''Exception if not a digit'''
    def __init__(self, txt):
        self.txt = txt


user_list = []
while(True):
    user_data = input("please enter a new digit, to stop enter stop\n")
    try:
        if user_data.isdigit():
            user_list.append(int(user_data))
        else:
            raise NotDigitException("you need to enter only digits")
    except NotDigitException as err:
        if user_data == "stop":
            break
        else:
            print(err)
print(f"final list is {user_list}")
