# !/usr/bin/python3
# -*- coding: UTF8 -*-

import time

def str_reverse_recussion(String: str, start_pos: int, end_pos: int):
    """ Function to check given String is palindrome or not
    Args:
        String      (str) : Input String
        start_pos   (int) : start position of String
        end_pos     (int) : end position of String
    
    Return:
        True on Success, False on Failure 
    """
    if start_pos != end_pos:
        if String[start_pos] == String[end_pos]:
            # str_reverse_recussion(String, start_pos+1, end_pos-1)
            # alternative for above line
            str_reverse_recussion(String[start_pos+1 : end_pos], start_pos, len(String[start_pos+1 : end_pos])-1) 
        else:
            print("String is not Palindrome")
            return False
    if start_pos == end_pos:
        print("String is a Palindrome")
    return True

name ="madadam"

start_time = time.time()

print(str_reverse_recussion(name, 0, len(name)-1))

end_time = time.time()

print("Time taken : {}".format(str(end_time-start_time)))