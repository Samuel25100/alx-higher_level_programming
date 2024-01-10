#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    count = 0
    value = 0
    for i in my_list:
        count += i[1]
        value += (i[1] * i[0])
    return value / count
