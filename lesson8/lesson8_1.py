#!/usr/bin/python3

import datetime

class Date():
    def __init__(self, str):
        self.date, self.month, self.year = Date.str_to_int(str)

    @classmethod
    def str_to_int(cls, str):
        date, month, year = map(int, str.split("-"))
        return date, month, year

    @staticmethod
    def is_data_correct(str):
        format = "%d-%m-%Y"
        try:
            return datetime.datetime.strptime(str, format)
        except ValueError:
            print("Incorrect date or format! Format must be 'day-month-year'")


date_string = "09-02-2020"
d1 = Date(date_string)
print(Date.is_data_correct(date_string))
print(d1.__dict__)
