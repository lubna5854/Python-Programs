rows = 7

for i in range(1, rows+1):
    for j in range(1, i):
        print(" ", end="")
    for j in range(i, rows+1):
        print(j, end=" ")
    print()

for i in range(rows-1, 0, -1):
    for j in range(1, i):
        print(" ", end="")
    for j in range(i, rows+1):
        print(j, end=" ")
    print()

"""
1 2 3 4 5 6 7 
 2 3 4 5 6 7 
  3 4 5 6 7 
   4 5 6 7 
    5 6 7 
     6 7 
      7 
     6 7 
    5 6 7 
   4 5 6 7 
  3 4 5 6 7 
 2 3 4 5 6 7 
1 2 3 4 5 6 7 
"""
"""

def print_mirror(n):
    temp = 1
    temp2 = 1
    for i in range(n):
        for j in range(n , i, -1):
            print(" ", end=" ")
        for k in range(1, temp + 1):
            print(abs(k - temp2), end=" ")
        temp += 2
        temp2 += 1
        print()

n = 5
print_mirror(n)

          0 
        1 0 1 
      2 1 0 1 2 
    3 2 1 0 1 2 3 
  4 3 2 1 0 1 2 3 4 
"""
