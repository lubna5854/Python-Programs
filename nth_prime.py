# Program to check if a number is prime or not
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
                print(num,end=" ")
            count += 1
        num += 1

# 2 3 5 7 11 13 17 19 23 29 31