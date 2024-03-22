#          ***************      Program to check if a number is prime or not          **************

num =int(input("Enter number: "))
flag = False
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


#        **********      series of prime numbers till n         *****************
""" 

def prime_num(nth):
    if nth == 1:
        return False
    elif nth > 1:
        for i in range(2,nth):
            if (nth % i) == 0:
                return False
        return True

count = 0
limit = int(input("Enter the number : "))

if limit <= 0:
    print("Invalid number")
else:
    num = 2
    while count < limit:
        if prime_num(num):
            print(num,end=" ")
            count += 1
        num += 1
"""



""" #      *************     Program for finding nth prime        *************

def prime_num(nth):
    if nth == 1:
        return False
    elif nth > 1:
        for i in range(2,nth):
            if (nth % i) == 0:
                return False
        return True

count = 0
limit = int(input("Enter the number : "))

if limit <= 0:
    print("Invalid number")
else:
    num = 2
    while count < limit:
        if prime_num(num):
            if count==limit-1:
                print("{}th prime number {}".format(limit,num))
            count += 1
        num += 1
"""