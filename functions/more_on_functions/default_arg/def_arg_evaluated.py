# !/usr/bin/Python3
# -*- coding: UTF8 -*-

i = 5
def def_arg_evaluated(arg=i):
    print("ARG value: \"{}\"".format(arg))

i = 6
def_arg_evaluated()
def_arg_evaluated(i)
print("{}".format("=")*60)
# ----------------------
# O/P:-
# ARG value: "5"
# ARG value: "6"
# ----------------------

def f(a, L=[]):
    L.append(a)
    print(L)
f(4)
f(3)
f(2)
print("{}".format("=")*60)
# ----------------------
# O/P:-
# [4]
# [4, 3]   
# [4, 3, 2]
# ----------------------
def f(a, L=[]):
    if len(L) == 0 :
        L = []
        pass
    L.append(a)
    print(L)
f(4)
f(3)
f(2)
# ----------------------
# O/P:-
# [4]
# [3]   
# [2]
# ----------------------