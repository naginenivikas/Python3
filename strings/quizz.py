#!/usr/local/bin/python3
# -*- coding: UTF8 -*-

# string reversal
print("{}".format('#')*60)
print("#\t\t 1'st PUZZLE")

print("{}".format(input("Enter User Name : "))[::-1])

print("{}".format('#')*60)
print("#\t\t 2'nd PUZZLE")
# Read name and character from user and print length of the name and count the occurance of character in name(case insentitive).
name, char = input("Enter name and char with comma seperator : ").split(',')
print("\nlength of \"{}\" : {} and occurance of \"{}\" in \"{}\" : {}".format(name, len(name), char, name, name.lower().count(char.lower())))

print("{}".format('#')*60)