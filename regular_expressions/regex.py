# !/usr/bin/python3
# -*- coding: UTF-8 -*-

import re

def regular_exp(num):
    match num:
        case 'titles': return r'Note \d – ([^\n]+)'

        case 'phone': return r'(\d{10})|(\+\d{2}-\d{10})|(\d{4}-\d{3}-\d{4})'

        case default: "Wrong Input, Please check Input Args..!"


string = ""
with open('titles.txt', 'r', encoding="UTF-8") as rf:
    for line in rf.readlines():
        string += line

matches = ['titles', 'phone']


for items in matches:
    print(f"Pattern matching for {items} : {re.findall(regular_exp(items), string)}\n")