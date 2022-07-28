# Generates a sequence of even numbers from 1 to input number 
# Input  :  10
# Output :  2, 4, 6, 8, 10

def my_even_number_generator(numbers):
    for num in range(1, numbers+1):
        if num % 2 == 0:
            yield num

even_numbers = my_even_number_generator(10)

for elem in even_numbers:
    print(f"{elem}", end=', ')