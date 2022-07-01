# !/usr/bin/Python3
# -*- coding: UTF8 -*-

for _ in iter(int, 1):
    num = int(input("Enter the number to check even/odd: "))
    if not (num & 0x01):
        print("Even Number")
        continue