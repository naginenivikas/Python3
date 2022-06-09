# !/usr/bin/python3
# -*- coding: UTF8 -*-

def swap_list_first_last_1(tmp=[]):
    if len(tmp) == 0:
        return tmp
    tmp[0], tmp[-1] = tmp[-1], tmp[0]
    return tmp

def swap_list_first_last_2(tmp=[]):
    """" pack expects atleast 2 values
        Args:
            tmp(list): A list
    """
    beg, *mid, end = tmp
    tmp = [end, *mid, beg]
    return tmp

li1 = [1, 2, 3]
li2 = [3]
li4 = []
li3 = [5, 2, 3, 4, 1]

print(swap_list_first_last_1(li1))
print(swap_list_first_last_1(li2))
print(swap_list_first_last_1(li3))
print(swap_list_first_last_1(li4))

print("{}".format("=")*60)

print(swap_list_first_last_2(li1))
# print(swap_list_first_last_2(li2)) # expects atleast 2 argunmnets for packing
print(swap_list_first_last_2(li3))
# print(swap_list_first_last_2(li4)) # expects atleast 2 argunmnets for packing