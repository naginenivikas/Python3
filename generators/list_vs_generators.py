import time
import threading


def list_comprehension():
    lt1 = time.time()
    squares = [val**2 for val in range(1000000000)]
    print(f" list comprehension time : {time.time()-lt1}")
    return True

def generator_comprehension():
    gent1 = time.time()
    squares = (val**2 for val in range(1000000000))
    print(f" Generator Comprehension time: {time.time()-gent1}")
    return True
    

if __name__ == '__main__':
    tr1 = threading.Thread(target=list_comprehension)
    tr2 = threading.Thread(target=generator_comprehension)

    tr1.start()
    tr2.start()

    tr1.join()
    tr2.join()
    print("Done with Execution")

# start_time = time.time()
# squares = [i**2 for i in range(100000000)]
# print(time.time()-start_time)


# start_time = time.time()
# squares = (i**2 for i in range(100000000))
# print(time.time()-start_time)
# print(squares)  # <generator object <genexpr> at 0x000001BA01701FC0>

