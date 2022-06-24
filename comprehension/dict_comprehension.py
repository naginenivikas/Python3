# !/usr/bin/python3
# -*- coding: UTF8 -*-

#=================================================================
# 
#              Dictionary Comprehension
# ----------------------------------------------------------------
# 
#         Normal  := { key : value, loop }
# 
#         If Con  := { key : value, loop, if(condition) }
# 
#         If-else := { key : if_value - if(condition) else else_value, loop}
# 
#         Nested  := { key : { value loop } loop(keys)}
# 
#         ZIP     := { list1_key : list2_value loop( with zip(data1, data2))}  
#         (sets of lists/tuples)
#
# =================================================================

def dict_comprehensions(num, arr=None):
    """ To Perform Dictionary Comprehension based on "n value".
    
    ARGS:
        arr(list): A List of Interger data
        num(int): An Interger Value
    
    Return:
        Returns a Dictionary{key:value} processed on i/p List.
    """

def dict_comprehension(num, arr):
    match num:
        case 1: return {val:val**2 for val in arr}

        case 2: return {val:f" {val} is an even value " for val in arr if(val%2==0)}

        case 3: return {val:f" even " if(val%2==0) else f" odd " for val in arr}

        case 4: return {f"{key} key":{value for value in "vikas"} for key in arr}

        case 5: return {f"{key} Square":value**2 for key, value in zip(arr, arr)}

        case default: return "Wrong Input, Please check the argunments...!"

List = [1, 2, 3, 4, 5]
print(f" Normal dictionary comprehension  : {dict_comprehension(1, List)}\n")
print(f" IF dictionary comprehension      : {dict_comprehension(2, List)}\n")
print(f" IF-Else dictionary comprehension : {dict_comprehension(3, List)}\n")
print(f" Nested dictionary comprehension  : {dict_comprehension(4, List)}\n")
print(f" On ZIP dictionary comprehension  : {dict_comprehension(5, List)}\n")