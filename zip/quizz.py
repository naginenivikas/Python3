# !/usr/local/python3
# -*- coding: UTF8 -*-

#================================================================
#
#  Input1  :-  [1, 2, 3] [4, 5, 6] [7, 8, 9]  
#
#  Output1 :-  (1+4+7)/3, (2+5+8)/3, (3+6+9)/3 
#----------------------------------------------------------------
# 
#  Input2  :-  [1, 2, 3] [4, 5, 6] [7, 8]
#   
#  Output2 :- (1+4+7)/3, (2+5+8)/3, (3+6+)/2
#================================================================= 


from audioop import avg

l1 = [i for i in range(1,4)]
l2 = [i for i in range(4,7)]
l3 = [i for i in range(7, 10)]

print(list(lambda pair: avg(pair) for pair in zip(l1, l2, l3)))

l1 = [i for i in range(1,4)]
l2 = [i for i in range(4,7)]
l3 = [i for i in range(7, 9)]

print(list(lambda pair: avg(pair) for pair in zip(l1, l2, l3)))