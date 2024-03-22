def sum_of_numbers(x):
    if x==1:
        return 10
    else:
        return x * 10 + sum_of_numbers(x-1)

n= int(input("Enter a number: "))
print("Sum : ", sum_of_numbers(n))