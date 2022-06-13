# !/usr/bin/python3
# -*- coding: UTF8 -*-

global_scope_var = 5

def fun():
    global global_scope_var
    global_scope_var = 7
    return global_scope_var

print(global_scope_var)
print(fun())
print(global_scope_var)