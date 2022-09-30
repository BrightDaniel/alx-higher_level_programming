#!/usr/bin/python3
def element_at(my_list, idx):
    if idx == -1:
        return None
    elif idx > my_list:
        return None
    else:
        return my_list
    print("Element at index {:d} is {}".format(my_list, idx))
