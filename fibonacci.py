# Fibonacci Series

# def fibo(n):
#     if n<=1:
#         return n
#     else:
#         return fibo(n-2)+fibo(n-1)

def fibo(n):
    return n if n<=1 else fibo(n-2)+fibo(n-1)


x=int(input("Enter the Limit: "))
print("Fibonacci series: ")
for i in range(x):
   print(fibo(i),end=" ")
