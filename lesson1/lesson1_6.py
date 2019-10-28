#!/usr/bin/python3

km = int(input("Please enter how many kilometers" 
                   "runner can do on the first day: "))
target_km =int(input("Please enter target kilometers per day: "))
days = 1
while km < target_km:
    km *= 1.1
    days += 1
print(f"Runner is needed to train for {days} days") 
