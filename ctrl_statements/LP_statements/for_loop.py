# !/usr/bin/python3
# -*- coding: UTF8 -*-

# =======================================================================
#    
#    Input :- "12345"
#    
#    output:- 1+2+3+4+5 = 15
#  
#    Des :- read string from user and add one by one character as int
#           and display output 
#
# =======================================================================

def sum(num):
    total = 0
    for ch in num:
        total += int(ch)
    return total
num = input("Enter string with numbers \"{45367}\": ")
print("Sum of \"{}\": {}".format(num, sum(num)))

total = 0
for ch in input("Enter a string with numbers \"{1234}\": "):
    total += int(ch)
print("Sum of string: {}".format(total))

