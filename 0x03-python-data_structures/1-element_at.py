#!/usr/bin/python3

# that retrieves an element from a list like in C.

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return
    return my_list[idx]
