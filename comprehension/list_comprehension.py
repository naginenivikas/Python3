# !/usr/bin/python3
# -*- coding: UTF8 -*-

#=================================================================
# 
#              List Comprehension
# ----------------------------------------------------------------
# 
#         Normal  := [ value, loop ]
# 
#         If Con  := [ value, loop, if(condition) ]
# 
#         If-else := [ if_value - if(condition) else else_value, loop]
# 
#         Nested  := [ [ "sub list values" ] loop(no of sub List)]
#
# =================================================================

def list_comprehensions(num, arr=None):
    """ To Perform List Comprehension based on "n value".
    
    ARGS:
        arr(list): A List of Interger data
        num(int): An Interger Value
    
    Return:
        Returns a list processed on i/p List.
    """
    match num:
        case 1 : return [val*val for val in arr]

        case 2 : return [val for val in arr if val%2 == 0]

        case 3: return [f'{val} is even' if (val%2 == 0) else f'{val} is odd' for val in arr]

        case 4: return [ [val for val in range(arr[0], arr[1]+1)][-1::-1] if (sub_list%2 !=0 ) else [val for val in range(arr[0], arr[1]+1)] for sub_list in range(arr[2]) ]

        case default: return "Wrong Input for List Comprehension technique"

List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("List Comprehension : {}\n".format(list_comprehensions(1, List)))
print("List Comprehension with \"IF Conition\": {}\n".format(list_comprehensions(2, List)))
print("List Comprehension with \"IF-Else Conition\": {}\n".format(list_comprehensions(3, List)))
print("List Comprehension with \"Nested \": {}\n".format(list_comprehensions(4, [4, 8, 3])))