'''
program to check a number is prime but not in fibonacci series
'''
def prime(n):
    flag=False
    if n<2:
        print("Not a prime number")
    else:
        for i in range(2,n):
            if n%i==0:
                flag=True
                break
    if flag:
        print(n," Not a prime number")
    else:
        print(n," is Prime number")


n=int(input("Enter the number: "))
num1=0
num2=1
list_fibo=[0,1]
for i in range(n):
    sum_num=num1+num2
    list_fibo.append(sum_num)
    num1=num2
    num2=sum_num

if n in list_fibo:
    print("Number is fibonacci")
else:
    print("Number not in fibanacci")
    prime(n)

'''
output

Enter the number: 13
Number is fibonacci

'''