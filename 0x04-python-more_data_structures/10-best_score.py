#!/usr/bin/python3
def best_score(a_dictionary):
    value = 0
    if a_dictionary is None:
        return None
    value = max(a_dictionary, key=a_dictionary.get)
    return value
