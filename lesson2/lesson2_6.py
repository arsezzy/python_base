#!/usr/bin/python3

add_more = 'yes'
goods_list = []
analytic_dict = {}
new_goods_list = []

while add_more.startswith('y'):
    goods_item = {}
    goods_item['name'] = input('Please enter a name of item:\n')
    goods_item['price'] = input('Please enter a price:\n')
    goods_item['amount'] = input('Please enter a amount:\n')
    goods_item['unit'] = input('Please enter a unit of measure:\n')
    goods_list.append(goods_item)
    add_more = input("add another one good? (y/n)\n")
numbered_goods_list = list(enumerate(goods_list,1))
print(f'data structure is displayed below:\n {numbered_goods_list}')

for index, val in enumerate(numbered_goods_list):
     new_goods_list.append(val[1])
keys_list = new_goods_list[0].keys() 
for key in keys_list:
    values = []
    for good_dict in new_goods_list:
        values.append(good_dict[key])
    analytic_dict[key] = values
print(f'Analytics data is printed below: \n {analytic_dict}')
