#!/usr/bin/python3
def uniq_add(my_list=[]):
    Listset = set(my_list)
    result = sum(Listset)
    print("Result: {:d}".format(result))
