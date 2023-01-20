#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """ Finds the peak in a list of integers """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    m = int(length / 2)
    li = list_of_integers

    if m - 1 < 0 and m + 1 >= length:
        return li[m]
    elif m - 1 < 0:
        return li[m] if li[m] > li[m + 1] else li[m + 1]
    elif m + 1 >= length:
        return li[m] if li[m] > li[m - 1] else li[m - 1]

    if li[m - 1] < li[m] > li[m + 1]:
        return li[m]

    if li[m + 1] > li[m - 1]:
        return find_peak(li[m:])
    return find_peak(li[:m])
