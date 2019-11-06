#!/usr/bin/python3

def user(
    '''print taken user info'''
    name = None, surname = None, birth_date = None, city = None, 
    email = None, phone = None
    ):
    print(name, surname, birth_date, city, email, phone)

user(birth_date = "01.01.2000", city = "Moscow", phone = "xxx", 
    email = "xxx", name = "Ivan", surname = "Ivanov")
