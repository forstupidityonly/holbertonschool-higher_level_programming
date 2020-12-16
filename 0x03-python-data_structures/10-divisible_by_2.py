#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    tmp = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            tmp.append(True)
        else:
            tmp.append(False)
    return tmp
