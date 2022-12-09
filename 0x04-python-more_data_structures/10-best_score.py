#!/usr/bin/python3
def best_score(a_dictionary):
    Max = None
    if a_dictionary:
        for key in a_dictionary:
            if Max:
                if a_dictionary[Max] < a_dictionary[key]:
                    Max = key
                continue
            Max = key
    return Max
