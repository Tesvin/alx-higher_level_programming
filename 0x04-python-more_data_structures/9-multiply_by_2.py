#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """new dictionary with all values multiplied by 2"""
    dict = {x: (a_dictionary[x]*2) for x in a_dictionary}
    """Returns a new dictionary"""
    return dict
