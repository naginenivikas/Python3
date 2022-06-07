#!/usr/local/bin/python3
# -*- coding: UTF8 -*-
name, age = input("Enter name and age with , operator : ").split(',')
print("name :{} age :{}".format(name.strip().replace(" ", "_"), age.strip()))


