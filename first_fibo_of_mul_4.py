'''
write a program to print 1st Fibonacci number from a given range that is a multiple of 4.
 Given a range of 3 and 150, first Fibonacci number that is a multiple of 4 is 8

'''

def fib(n):
    fib_numbers = [0, 1]
    for i in range(2, n+1):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])
    return fib_numbers

def first_fib_multiple_of_four(start, end):
    fib_numbers = fib(end)
    for i in range(start, end+1):
        if fib_numbers[i] % 4 == 0:
            return fib_numbers[i]
    return "No such number found"

print(first_fib_multiple_of_four(3, 150))