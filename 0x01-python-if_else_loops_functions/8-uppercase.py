#!/usr/bin/python3
def uppercase(str):
    for i in str:
        str = chr(ord(i) - 32)
        print('{:s}'.format(str), end='')
