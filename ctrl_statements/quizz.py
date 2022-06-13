# !/usr/bin/python3
# -*- coding: UTF8 -*-

#========================================================================
#
#           Input  : range of natural numbers from "1 - n" and winning number
#           
#           output : Win, if winnig number matches with Win number, no of retry with win  
#
#     Example:  i/p: 1 - 10, 5 
#               o/p: 6 retry and 4 is Win number
#========================================================================
from random import randint

def lottery(num: int, win_num: int, cnt: int):
    if win_num == num:
        print("You win with \"{}\" retries, Win number is \"{}\"".format(str(cnt+1), str(num)))
        return True
    else:
        if win_num < num:
            print("too High")
        else:
            print("too low")
        return False

start, end = input("Enter range of +ve numbers 1 - n : ").replace(' ', '').split("-")
win_num = randint(int(start), int(end))
cnt = 0
while True:
    if lottery(int(input(f"Guess win number between {start} - {end}: ").strip()), win_num, cnt):
        break
    else:
        cnt += 1
        continue

