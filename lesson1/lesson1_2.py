#!/usr/bin/python3

#first variant
user_time = int(input("Please enter time in seconds:\n"))
SECONDS_IN_HOUR = 3600
MINUTES_IN_SECONDS = 60
time_hours = user_time//SECONDS_IN_HOUR
time_minutes = (user_time%SECONDS_IN_HOUR)//MINUTES_IN_SECONDS 
time_seconds = user_time - time_hours*SECONDS_IN_HOUR - time_minutes*MINUTES_IN_SECONDS
if (time_hours < 10):
    time_hours = "0" + str(time_hours)
if (time_minutes < 10 ):
    time_minutes = "0" + str(time_minutes)
if (time_seconds < 10):
    time_seconds =  "0" + str(time_seconds)

print(f"time in hh:mm:ss \n{time_hours}:{time_minutes}:{time_seconds}")

#second variant
print("Second variant:")
import datetime
print(f"time in hh:mm:ss \n {str(datetime.timedelta(seconds=user_time))}")
