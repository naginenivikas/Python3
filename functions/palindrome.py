# !/usr/bin/python3
# -*- coding: UTF8 -*-

# =====================================================================
#  After reversing the original string if equals to original string called palindrome
#
#          i/p :-   (m a d a m) -> ( m a d a m)
#                    | | | | |_______| | | | |
#                    | | | |___________| | | |
#                    | | |_______________| | |
#                    | |___________________| |
#                    |_______________________|
#
# ===================================================================

def is_palindrome(String: str):
    """ Check the String is Palindrome or not
        
    ARGS:
        String (str): String to be checked.

    Return:
        True on Success, False on Failure.  
    """
    if String.lower() == String[::-1].lower():
        print("\"{}\" is Palindrome".format(String))
        return True
    else:
        print("\"{}\" Not a Palindrome".format(String))
        return False


List = ["madam", "Madam", "vikas"]
for ele in List:
    is_palindrome(ele)
    