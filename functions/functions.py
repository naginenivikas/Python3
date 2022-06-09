# !/usr/bin/python3
# -*- coding: UTF8 -*-

def args_add(arg1, arg2):
    return arg1 + arg2
print("O/P : {}".format(args_add(int(input("Enter 1'st Number: ")), int(input("Enter 2'nd Number: ")))))
print("{}".format("=")*60)
print("O/P : {}".format(args_add(input("Enter 1'st String: "), input("Enter 2'nd Number: "))))