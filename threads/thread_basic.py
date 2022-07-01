# !/usr/bin/python3
# -*- coding: UTF8 -*-

from threading import Thread

def even_numbers(num):
    for item in range(num):
        if (item%2 == 0):
            print(f"Even_number: {item}")

def odd_numbers(num):
    for item in range(num):
        if (item%2 !=0):
            print(f"Odd_number: {item}")

# def check_prime(num):
#     for item in range(2,num):
#         if not (num % item):
#             print("Not a Prime")
#     print("Prime Number")

if __name__  == "__main__":
    # tr1 = Thread(target=echo, args=(100,))
    # tr2 = Thread(target=check_prime, args=(97,))
    n = 25
    tr1 = Thread(target=even_numbers, args=(n,))
    tr2 = Thread(target=odd_numbers, args=(n,))    
 
    # Thread start execution at this point 
    tr1.start() 
    tr2.start() 

    # Wait until Thread execution is completed then Main process execution
    tr1.join()
    tr2.join()
    print("Done")



"""
Before Start
Thread1 before start
Even_number: 0      
Even_number: 2      
Even_number: 4      
Even_number: 6      
Even_number: 8      
Even_number: 10     
Even_number: 12     
Even_number: 14     
Even_number: 16     
Even_number: 18     
Even_number: 20     
Even_number: 22     
Even_number: 24     
Thread1 After start 
Thread2 before start
Odd_number: 1       
Thread2 After start 
Odd_number: 3       
Odd_number: 5       
Thread1 before Join 
Odd_number: 7       
Thread1 After Join
Thread2 before Join
Odd_number: 9
Odd_number: 11
Odd_number: 13
Odd_number: 15
Odd_number: 17
Odd_number: 19
Odd_number: 21
Odd_number: 23
Thread2 After Join
Done
"""