def roman_to_int(roman_string):
    if (type(roman_string) is not str) or roman_string is None:
        return 0
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num_list = []
    for i in roman_string:
        num_list.append(data[i])
    num_list += [0]
    value = 0
    for i in range(len(num_list) - 1):
        if num_list[i] >= num_list[i + 1]:
            value += num_list[i]
        else:
            value -= num_list[i]
    return value
