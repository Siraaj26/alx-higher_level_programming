#!/usr/bin/python3

def no_c(my_string):
    new_string=""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and not 'C':
            new_string += my_string[i]
        return new_string
