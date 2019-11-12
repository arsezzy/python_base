#!/usr/bin/python3


with open("lesson5_2.txt", "r") as lesson5_2:
    content = lesson5_2.readlines()
for line in list(enumerate(content, 1)):
    print(f"String #{line[0]} has {len(list(line[1].split()))} words")
print(f"File has {len(content)} string")
