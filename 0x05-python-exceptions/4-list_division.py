#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    idx = 0
    while idx < list_length:
        aws = 0
        try:
            aws = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            new_list.append(aws)
            idx = idx + 1
    return new_list
            
