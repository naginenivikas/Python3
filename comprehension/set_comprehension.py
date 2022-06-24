# !/usr/bin/python3
# -*- coding: UTF8 -*-

#=================================================================
# 
#              Set Comprehension
# ----------------------------------------------------------------
# 
#         Normal  := { value, loop }
# 
#         If Con  := { value, loop, if(condition) }
# 
#         If-else := { if_value - if(condition) else else_value, loop}
# 
#         Nested  := { {"sub set values" } loop(no of sub sets)}
# 
# =================================================================

def Set_comprehensions(num, arr=None):
    """ To Perform set Comprehension based on "n value"
    
    ARGS:
        arr(list): A List of Interger data
        num(int): An Interger Value
    
    Return:
        Returns a set processed on i/p Set.
    """
    match num:
        case 1 : return {val*val for val in arr}

        case 2 : return {val for val in arr if val%2 == 0}

        case 3: return {f'{val} is even' if (val%2 == 0) else f'{val} is odd' for val in arr}

        case 4: return { {val for val in range(arr[0], arr[1]+1)}[-1::-1] if (sub_Set%2 !=0 ) else {val for val in range(arr[0], arr[1]+1)} for sub_Set in range(arr[2]) }

        case default: return "Wrong Input for Set Comprehension technique"

Set = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Set Comprehension : {}\n".format(Set_comprehensions(1, Set)))
print("Set Comprehension with \"IF Conition\": {}\n".format(Set_comprehensions(2, Set)))
print("Set Comprehension with \"IF-Else Conition\": {}\n".format(Set_comprehensions(3, Set)))
print("Set Comprehension with \"Nested \": {}\n".format(Set_comprehensions(4, [4, 8, 3])))