#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary = {key: val*2 for key, val in a_dictionary.items()}
    return a_dictionary
