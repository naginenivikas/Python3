# !/usr/bin/python3
# -*- codin: UTF-8 -*-

List = ['Guru', 'Vikas', 10, 'Emmanuel']

print([val[-1::-1] if (type(val)==str) else ValueError("Not an String") for val in List])