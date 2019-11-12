#!/usr/bin/python3

employees = {}
with open("lesson5_3.txt", "r") as lesson5_3:
    for man in lesson5_3:        
        employees_list = man.split()
        employees[str(employees_list[0])] = int(employees_list[1])
for worker, salary in employees.items():
    if salary < 20000:
        print(f"{worker} has salary less than 20000")
print(f"Average salary is {sum(list(employees.values())) / len(employees)}")
