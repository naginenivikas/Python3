def my_gen(num):
    for item in range(1,num+1):
        print(f"called generator : {item}")
        yield item

print(my_gen(10))  # <generator object my_gen at 0x0000023A3B261FC0>

numbers = my_gen(10)  # We have generated the sequence

# for Every Iteration generator will be called.
for val in numbers:
    print(f" Iterator on Generator : {val}")

#  Only one time we can Iterator over generator once done it will be flushed from memory

for val in numbers:                                      
    print(f"{val}", end=', ')

"""
Output:-

called generator : 1 
1
called generator : 2 
2
called generator : 3 
3
called generator : 4 
4
called generator : 5 
5
called generator : 6 
6
called generator : 7 
7
called generator : 8 
8
called generator : 9 
9
called generator : 10
10

"""

# =================================================================================================

numbers = list(my_gen(10))   # Generator will be called when we convert to type list

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in numbers:
    print(f"{val}", end=' ')
print("\n")
for val in numbers:                                      
    print(f"{val}", end=' ')

"""s
Output:- 
called generator : 1 
called generator : 2 
called generator : 3 
called generator : 4
called generator : 5
called generator : 6
called generator : 7
called generator : 8
called generator : 9
called generator : 10
1 2 3 4 5 6 7 8 9 10  
1 2 3 4 5 6 7 8 9 10
"""