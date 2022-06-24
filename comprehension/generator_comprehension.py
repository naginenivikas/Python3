# !/usr/bin/python3
# -*- coding: UTF8 -*-

#=================================================================
# 
#              Generator Comprehension
# ----------------------------------------------------------------
# 
#         Normal  := ( value, loop )
# 
#         If Con  := ( value, loop, if(condition) )
# 
#         If-else := ( if_value - if(condition) else else_value, loop) 
# 
#    
# =================================================================

def Generator_comprehensions(num, arr=None):
    """ To Perform Generator Comprehension based on "n value"
    
    ARGS:
        arr(list): A List of Interger data
        num(int): An Interger Value
    
    Return:
        Returns a Generator Object on process i/p data
    """
    match num:
        case 1 : return (val*val for val in arr)

        case 2 : return (val for val in arr if val%2 == 0)

        case 3: return (f'{val} is even' if (val%2 == 0) else f'{val} is odd' for val in arr)

        case default: return "Wrong Input for Set Comprehension technique"

Set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("Generator Comprehension : {}\n".format(list(Generator_comprehensions(1, Set))))

dictionary = set({1:'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'})
print("Generator Comprehension with \"IF Conition\": {}\n".format(list(Generator_comprehensions(2, dictionary))))

List = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Generator Comprehension with \"IF-Else Conition\": {}\n".format(list(Generator_comprehensions(3, List))))