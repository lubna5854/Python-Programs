"""
n = 5
for i in range(n):
    counter = i+1
    for j in range(i+1):
        print(counter, end=" ")
        counter += 1
    print()
1
2 3
3 4 5
4 5 6 7
5 6 7 8 9
"""

"""
n=5
for i in range(n):
    num=i+1
    c=n-1
    for j in range(i+1):
        print(num,end=" ")
        num += c
        c -= 1
    print()
    """
"""
1 
2 6 
3 7 11 
4 8 12 16 
5 9 13 17 21 
"""

"""
n = 5
for i in range(n):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(i + 1):
        print(k + 1, end=" ")
    for l in range(i - 1, -1, -1):
        print(l + 1, end=" ")
    print()
    
OUTPUT
          1 
        1 2 1 
      1 2 3 2 1 
    1 2 3 4 3 2 1 
  1 2 3 4 5 4 3 2 1 


"""
"""
row =5
for i in range(1,row+1):
    for j in range(i):
        print(format(i+(j*row), "2d"), end=" ")
    print()

output    
 1 
 2  7 
 3  8 13 
 4  9 14 19 
 5 10 15 20 25 
"""

"""
n=5
for i in range(1, n + 1):
    c = 1
    for j in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print(c, end=" ")
        c = c * (i - j) // j
    print()
    
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 
"""
"""
n=9
for i in range(n):
    for j in range(i,-1,-1):
        print(2**j,end=" ")
    print()
    
output
1 
2 1 
4 2 1 
8 4 2 1 
16 8 4 2 1 
32 16 8 4 2 1 
64 32 16 8 4 2 1 
128 64 32 16 8 4 2 1 
256 128 64 32 16 8 4 2 1 
"""

"""
n = 9
for i in range(n):
    for k in range(i + 1):
        print(2**k, end=" ")
    for l in range(i - 1, -1, -1):
        print(2**l, end=" ")
    print()

output
1 
1 2 1 
1 2 4 2 1 
1 2 4 8 4 2 1 
1 2 4 8 16 8 4 2 1 
1 2 4 8 16 32 16 8 4 2 1 
1 2 4 8 16 32 64 32 16 8 4 2 1 
1 2 4 8 16 32 64 128 64 32 16 8 4 2 1 
1 2 4 8 16 32 64 128 256 128 64 32 16 8 4 2 1 
"""
"""
for i in range(5):
    number = 10
    for j in range(i+1):
        if number%2 == 0:
            print(number, end=" ")
        else:
            pass
        number -= 2
    print()
    
output
10 
10 8 
10 8 6 
10 8 6 4 
10 8 6 4 2
"""
"""
n=5
for i in range(1,n+1):
    for j in range(i,n+1):
        print(j,end=" ")
    print()
output
1 2 3 4 5 
2 3 4 5 
3 4 5 
4 5 
5 
"""

"""
n=5
for i in range(n):
    number = n-i
    for j in range(n-i):
        print(number,end=" ")
        number -= 1
    print()
    
output
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
 """
"""n=5
for i in range(n):
    number = 5
    for j in range(n-i):
        print(number,end=" ")
        number -= 1
    print()
    
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 """
"""
n=5
for i in range(n):
    number = 5
    for j in range(i+1):
        print(number,end=" ")
        number -= 1
    print()
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 
"""

"""n=5
for i in range(n):
    number = 5
    for j in range(n-i):
        print(number,end=" ")
        number -= 1
    for j in range(i):
        print("   ",end=" ")
    for k in range(i+1,n+1):
        print(k,end=" ")
    print()
    
5 4 3 2 1 1 2 3 4 5 
5 4 3 2     2 3 4 5 
5 4 3         3 4 5 
5 4             4 5 
5                 5 
"""

"""
n=5
for i in range(n):
    number=n-i
    for j in range(i+1):
        print(number,end=" ")
        number += 1
    for k in range(n-i-1):
        print(n,end=" ")
    print()

5 5 5 5 5 
4 5 5 5 5 
3 4 5 5 5 
2 3 4 5 5 
1 2 3 4 5
"""
"""

n=5
for i in range(n+1):
    if i % 2 == 0:
        for j in range(i):
            print(j+1,end=" ")
    else:
        for j in range(i,0,-1):
            print(j,end=" ")
    print()


1
1 2
3 2 1
1 2 3 4
5 4 3 2 1
"""

"""

n=7
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    for k in range(n-i-1):
        print("*",end=" ")
    print()

1******
12*****
123****
1234***
12345**
123456*
1234567
"""
"""
row =5
for i in range(1,row+1):
    for j in range(i):
        print(i+(j*row),end=" ")
    print()

1 
2 7 
3 8 13 
4 9 14 19 
5 10 15 20 25
"""

"""
n=7
counter=1
for i in range(n):
    for j in range(i+1):
        print(counter,end=" ")
        counter=counter % 9 + 1
    print()

output
1 
2 3 
4 5 6 
7 8 9 1 
2 3 4 5 6 
7 8 9 1 2 3 
4 5 6 7 8 9 1 
"""
"""
n=5
counter=1
for i in range(n):
    if i % 2 == 0:
        for j in range(i+1):
            print(counter,end=" ")
            counter += 1
    else:
        start=counter+i
        for j in range(i+1):
            print(start,end=" ")
            start -= 1
            counter += 1
    print()

1 
3 2 
4 5 6 
10 9 8 7 
11 12 13 14 15 
"""