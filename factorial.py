# Python 3 program to find
# factorial of given number
def factorial(n):
    return 1 if (n == 1 or 0) else n * factorial(n - 1)


num = int(input("Enter Limit: "))
print("Factorial is: ", factorial(num))


# n=1
# num=int(input("Enter a limit: "))
# for i in range(1,num+1):
#     if n==1:
#         n+=1
#     else:
#         n=n*(n+1)
# #print("Factorial of", num, "is", factorial(num))
# print("Factorial: ",n)
