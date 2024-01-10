#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp_dic = a_dictionary.copy()
    for key, val in temp_dic.items():
        if val == value:
            a_dictionary.pop(key)
    return a_dictionary
