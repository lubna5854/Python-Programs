# pyramid star pattern

for i in range(5):
    for j in range(5 - i):
        print(' ', end=' ')
    for k in range(2 * i - 1):
        print('*', end=' ')
    print()


#     output

#         *
#       * * *
#     * * * * *
#   * * * * * * *

"""
n=5
for i in range(n):
    for k in range(n-i+1):
        print(" ",end=" ")
    for j in range(i+1):
        print(i+j+1,end=" ")
    num = i * 2
    for j in range(1,i+1):
        print(num, end=" ")
        num -= 1
    print()
    
output
            1 
          2 3 2 
        3 4 5 4 3 
      4 5 6 7 6 5 4 
    5 6 7 8 9 8 7 6 5 
"""

"""
n=5
for i in range(n):
    for k in range(n-i+1):
        print(" ",end=" ")
    for j in range(i+1):
        print(i+j,end=" ")
    num = i * 2-1
    for j in range(1,i+1):
        print(num, end=" ")
        num -= 1
    print()
    
output
            0 
          1 2 1 
        2 3 4 3 2 
      3 4 5 6 5 4 3 
    4 5 6 7 8 7 6 5 4

"""