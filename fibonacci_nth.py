# Implement a Python function to find the nth Fibonacci number.

def fibo(n):
    return n if n<=1 else fibo(n-2)+fibo(n-1)

number=int(input("Enter the number: "))
li=[]
for i in range(number):
    li.append(fibo(i))
print("{}th finbonacci number is {}".format(number,li[number-1]))