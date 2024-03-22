n=5

for i in range (n):
    num=i+1
    c=n-1
    for j in range(i+1):
        print (num,end=" ")
        num=num+c
        c=c-1
    print()

    """
    1
    2 6 
    3 7 10
    4 8 11 13
    5 9 12 14 15
    """

"""
n = 5
counter = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(counter, end=" ")
        counter += 1
    print()

OUTPUT
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

"""
"""
n=7
for i in range(n+1):
    for j in range(i):
        print(i*(j+1),end=" ")
    print()


output:
1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 

"""