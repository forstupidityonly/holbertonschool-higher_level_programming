#!/usr/bin/python3
def best_score(a_dictionary):
    tmp = 0
    score = ""
    if a_dictionary is None or a_dictionary == {}:
        return None
    for i in a_dictionary.keys():
        if a_dictionary[i] > tmp:
            tmp = a_dictionary[i]
            score = i
        return score
