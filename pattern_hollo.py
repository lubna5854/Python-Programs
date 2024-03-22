# hollow square pattern
n = 5
for i in range(n):
    for j in range(n):
        # print * completely in first and last row
        # print * only in first and last position in other rows
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# output

# *****
# *   *
# *   *
# *   *
# *****

'''
print(i+1)

output
1 1 1 1 1 
2       2 
3       3 
4       4 
5 5 5 5 5 

'''
"""

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or j==1 or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

*         
* *       
*   *     
*     *   
* * * * * 
"""

"""
print(i, end=" ")

1 
2 2 
3   3 
4     4 
5 5 5 5 5 
"""

"""
print(j, end=" ")
1 
1 2 
1   3 
1     4 
1 2 3 4 5 
"""
"""
n=5
for i in range(1,n+1):
    for j in range(i-1):
        print(' ', end=' ')
    for k in range(2*(n-i)+1):
        if k==0 or k==2*(n-i) or i==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

output
* * * * * * * * * 
  *           * 
    *       * 
      *   * 
        * 

"""
"""
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        if j==0 or j==2*i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(2*(n-i)-3):
        if j==0 or j==2*(n-i)-4:  # 2*(5-0)-4=6, so in place of 6 4 8, we print *.
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

output

        * 
      *   * 
    *       * 
  *           * 
*               * 
  *           * 
    *       * 
      *   * 
        * 

"""
"""
# hollow pyramid star pattern
n = 5
for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end=' ')
    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2 or i == n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()



# OUTPUT
#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *
"""