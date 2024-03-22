n = 4
counter = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(counter, end=" ")
        counter += 1
    print()

count=n*(n+1)//2
for i in range(n,0,-1):
    count-=i
    k=count+1
    for j in range(1,i+1):
        print(k,end=" ")
        k += 1
    print()

"""
output
1 
2 3 
4 5 6 
7 8 9 10 
7 8 9 10 
4 5 6 
2 3 
1 
"""