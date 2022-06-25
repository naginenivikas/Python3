# !/usr/bin/python3
# -*- coding: UTF-8 -*-

# Creating the Nested List with comprehension technique

names = ['Ganga', 'yamuna', 'Godavari']

# Nested List
List = [[val for val in names] for val in range(3)]
print(List)


# Nested to flatten List Converstion
List = [val for sub_list in List for val in sub_list]
print(List)