#!/usr/bin/python3

def no_c(my_string):
    new_s = my_string.translate({ord('c'): None})
    new_s = new_s.translate({ord('C'): None})
    return new_s
