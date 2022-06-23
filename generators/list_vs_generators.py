import time

# start_time = time.time()
# squares = [i**2 for i in range(100000000)]
# print(time.time()-start_time)


start_time = time.time()
squares = (i**2 for i in range(100000000))
print(time.time()-start_time)
print(squares)  # <generator object <genexpr> at 0x000001BA01701FC0>

