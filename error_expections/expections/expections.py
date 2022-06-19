# !/usr/bin/python3
# -*- coding: UTF8 -*-

a = 10
try:
    if type(a) == list:
        print("A Is of type List")
except TypeError as typerr:
    print("Found an Type Error Issue: {}".format(typerr))
