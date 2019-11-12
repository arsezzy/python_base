#!/usr/bin/python3

plan = {}
hours = []
with open("lesson5_6.txt") as lesson5_6:
    for subject in lesson5_6:
        subject_split = subject.split()
        subject_name = subject_split[0]
        all_hours = subject_split[1:]
        plan[subject_name] = 0
        for types in all_hours:
            try:
                plan[subject_name] += int(types[:types.find("(")])
            except ValueError:
                pass
print(plan)
