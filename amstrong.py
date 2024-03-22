
# ****** Find a number is Amstrong    *********

num=input("Enter number")
l=len(num)
sum=0
for i in num:
    sum=sum+(int(i)**l)
if sum==int(num):
    print("Amstrong")
else:
    print("Not Amstrong")


# ****** series of Amstrong numbers   *********

# for num in range(1,1000):
#     l = len(str(num))
#     sum = 0
#     for i in str(num):
#         sum = sum + (int(i) ** l)
#     if sum == int(num):
#         print(num,end=" ")
#
#


"""
#      ********      Program for finding nth amstrong    *******

def amstrong(num):
    l = len(str(num))
    sum = 0
    for i in str(num):
        sum=sum+(int(i)**l)
    if sum==int(num):
        return True
    else:
        return False

limit=int(input("Enter the limit:"))
counter=0
num=1
while counter<limit:
    if amstrong(num):
        if counter==limit-1:
            print("{}th amstrong number: {}".format(limit,num))
        counter+=1
    num+=1


 #      *****   without function    *****

 limit=int(input("Enter the limit:"))
counter=0
num=1
while counter<limit:
#for num in range(1000):
    l = len(str(num))
    sum = 0
    for i in str(num):
        sum = sum + (int(i) ** l)
    if sum == int(num):
        if counter==limit-1:
            print(num,end=" ")
        counter+=1
    num+=1

"""