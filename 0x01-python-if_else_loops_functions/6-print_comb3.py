#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x + 1, 10):
        if x == 8 and y == 9:
            continue
        else:
            print('{:d}{:d}, '.format(x, y), end='')
print('89')
