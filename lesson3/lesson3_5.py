#!/usr/bin/python3

def summarization(current_sum, digits_list, symbol):
    '''Summarize integers in digit_list  and add it to current_sum

    current_sum - integer
    digits_list - list of digit, where digit is string
    symbol - special symbol for exit. If special symbol is met, 
    stop to sum and return one_more_time = False
    if any other symbol is met, skip it
    '''

 
    one_more_time = True
    for digit in digits_list:
        try:
            digit = int(digit)
        except ValueError:
            try:
                exit_symbol_index = digit.index(symbol)
                if exit_symbol_index == 0:
                    digit = 0
                else:
                    digit = int(digit[:exit_symbol_index])
                current_sum += digit
                one_more_time = False
                break
            except ValueError:
                print(f"{digit} is not an integer, missing it")
                digit = 0
        current_sum += digit
    return current_sum, one_more_time

special_symbol = '!'
current_sum = 0
again = True
while again:
    user_digits = input(f"please enter a string of digits with spacebar" 
                        f" separator. For exit "
                        f"press '{special_symbol}'\n").split()
    current_sum, again = summarization(current_sum, user_digits, special_symbol)
    print(f"current sum is {current_sum}")
print(f"special symbol {special_symbol} is entered, exiting")
