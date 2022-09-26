#!/usr/bin/python3
def no_c(my_string):
    new = list(my_string)
    for x in new:
        if x == 'c':
            new.remove('c')
        if x == 'C':
            new.remove('C')
    my_string = " ".join(new)
    return my_string
