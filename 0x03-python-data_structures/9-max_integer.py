#!/usr/bin/python3
def max_integer(my_list=[]):
    if not(my_list):
        return (None)
    num = 0
    for i in my_list:
        if num < i:
            num = i
    return (num)
