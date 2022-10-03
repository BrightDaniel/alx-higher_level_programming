#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for key in sorted(my_dict.keys()):
        print("{:s}: {}".format(key, my_dict[key]))
