#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.copy()
    for i in my_list:
        if idx == my_list.index(i):
            copy[idx] = element
            return (new)
        elif idx >= len(my_list):
            return (new)
        elif idx < 0:
            return (new)
