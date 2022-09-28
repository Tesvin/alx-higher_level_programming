#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for f, v in sorted(a_dictionary.keys()):
        print("{}: {}".format(f, v))
