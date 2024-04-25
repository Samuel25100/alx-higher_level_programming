#!/usr/bin/python3
"""Find a peak in a list of unsorted integers return it."""


def find_peak(list_of_integers):
    """Do the recursion to find peak."""
    if not list_of_integers:
        return None

    le = len(list_of_integers)
    li = list_of_integers
    if (le == 2 and li[0] != li[1]):
        return (li[0] if li[0] > li[1] else li[1])
    elif (le == 2 and li[0] == li[1]):
        return (li[0])

    if (le >= 2) and (le % 2 == 0):
        tmp = le // 2
        re1 = find_peak(li[0:tmp])
        re2 = find_peak(li[tmp:])
        return (re1 if re1 > re2 else re2)
    elif (le >= 2) and (le % 2 != 0):
        if (le == 3):
            la = find_peak(li[0:2])
            return (la if la > li[2] else li[2])
        tmp = (le - 1) // 2
        fin = le - 1
        re1 = find_peak(li[0:tmp])
        re2 = find_peak(li[tmp:fin])
        la = (re1 if re1 > re2 else re2)
        return (la if la > li[-1] else li[-1])
