# !/usr/bin/python3
# -*- coding: UTF8 -*-

#################################################################################
#  Example: Input number for factorial is 4
#-------------------------------------------------------------------------------
#   stack_frame_4
#                  -> 4 * stack_frame_3
#                  and rest not executed code before function call (return 4 * stack_frame_3)
#                  4 * 3 * 2 * 1
#--------------------------------------------------------------------------------
#   stack_frame_3
#                  -> 3 * stack_frame_2    
#                  and rest not executed code before function call (return 3 * stack_frame_2)
#                  3 * 2 * 1
#--------------------------------------------------------------------------------
#   stack_frame_2
#                  -> 2 * stack_frame_1    
#                  and rest not executed code before function call (return 2 * stack_frame_1)
#                  2 * 1
#--------------------------------------------------------------------------------
#   stack_frame_1
#                  -> n == 1 so return 1
#################################################################################
def fact(n):
    if n == 0 or n == 1:
        return n
    n = n * fact(n-1)
    return n

num = int(input("Enter the Number: "))
print("Factorial of \"{}\" : {}".format(str(num), str(fact(num))))