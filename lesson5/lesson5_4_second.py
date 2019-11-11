#!/usr/bin/python3

import requests

with open("lesson5_4_rus.txt", "w") as lesson5_4_rus:
    with open("lesson5_4_en.txt") as lesson5_4_en:
        for line in lesson5_4_en:
            string = line.split()
            if string[0] == "one":
                string[0] = "один"
            elif string[0] == "two":
                string[0] = "два"
            elif string[0] == "three":
                string[0] = "три"
            elif string[0] == "four":
                string[0] = "четыре"
            print(" ".join(string), file = lesson5_4_rus) 

