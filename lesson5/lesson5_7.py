#!/usr/bin/python3
import json

firms = {}
with open("lesson5_7.txt") as lesson5_7:
    for firm in lesson5_7:
        firm_split = firm.split()
        firms[firm_split[0]] = int(firm_split[2]) - int(firm_split[3])
sums =[x for x in list(firms.values()) if x > 0]  
average_profit = {"average_profit" : round(sum(sums) / len(sums), 2)}
for firm, profit in firms.items():
    firms[firm] = abs(profit)
final_list = [firms, average_profit]
with open("lesson5_7_json.txt", "w") as lesson5_7_json:
    json.dump(final_list, lesson5_7_json)
