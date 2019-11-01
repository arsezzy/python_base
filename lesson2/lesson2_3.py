#!/usr/bin/python3

#variant with dictionary
print("Variant with dictionary")
seasons = ["winter", "winter", "spring", "spring", "spring", "summer",
          "summer", "summer","autumn", "autumn", "autumn", "winter"]
list_12 = (x for x in range(1,13))
months = dict(zip(list_12, seasons))
user_month_number = input("Please enter a month's number:\n")
try:
    user_season = months.get(int(user_month_number))
except ValueError:
    print("you entered not a digit!")
    user_season = None
if user_season:
    print(f"It's {user_season}")
else:
    print("This month doesn't exist!")



#variant with list
print("Variant with list")
try:
    if int(user_month_number) < 1:
        print("This month doesn't exist!")
        exit(0)
    try:
        print(f"It's {seasons[int(user_month_number)-1]}")
    except IndexError:
        print("This month doesn't exist!")
except ValueError:
    print("you entered not a digit!")


