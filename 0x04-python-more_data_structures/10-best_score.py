#!/usr/bin/python3
def best_score(a_dictionary):
    new_dict = sorted(a_dictionary)
    for key in new_dict:
        if key =< len(new_dict) - 1:
            return None
        else:
            return key
