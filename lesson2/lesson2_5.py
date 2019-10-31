#!/usr/bin/python3

rating = [7, 5, 5, 3, 3]
print(f'current rating is {rating}')
again_input = 'y'
while again_input.startswith('y'):
    try:
        new_position = int(input('Please enter a new natural value:\n'))
    except ValueError:
        print('you did not enter natural value')
        new_position = 0         
    if new_position > 0:
        position_inserted = False
        for position in rating:
            if new_position > position:
                rating.insert(rating.index(position),new_position)
                position_inserted = True
                break
        if not position_inserted:
            rating.append(new_position)
        print(f'new rating is {rating}') 
    else:
        print('you did not enter natural value')
    again_input = input('Do you want to enter one more value? (y/n):\n').lower()
print("You don't want to add new value, exiting")    
