#!/usr/bin/python3
def no_c(my_string):
    new = list(my_string)
    for i in new:
        if i == 'c':
            new.remove('c')
        if i == 'C':
            new.remove('C')
    my_string = "".join(new)
    return my_string
