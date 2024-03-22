# # Square pattern program

# star square pattern

# for i in range(5):
#     # Create a list of columns
#     for j in range(5):
#         print("*", end=" ")
#     print("")

# OUTPUT
# *****
# *****
# *****
# *****
# *****

# number square pattern
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j<=i:
#             print(j, end=" ")
#         else:
#             print(i,end=" ")
#     print()

# OUTPUT
# 1 1 1 1 1
# 1 2 2 2 2
# 1 2 3 3 3
# 1 2 3 4 4
# 1 2 3 4 5

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j<=i:
#             print(i, end=" ")
#         else:
#             print(j,end=" ")
#     print()
#
#   OUTPUT
# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if j <= n-i+1:
            print(j, end=" ")
        else:
            print(n-i+1, end=" ")
    print()

# OUTPUT
# 1 2 3 4 5
# 1 2 3 4 4
# 1 2 3 3 3
# 1 2 2 2 2
# 1 1 1 1 1

"""

6 5 4 3 2 1
5 5 4 3 2 1
4 4 4 3 2 1
3 3 3 3 2 1
2 2 2 2 2 1
1 1 1 1 1 1 


n=6
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i>=j:
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()
"""

"""

6 6 6 6 6 6 
6 5 5 5 5 5 
6 5 4 4 4 4 
6 5 4 3 3 3 
6 5 4 3 2 2 
6 5 4 3 2 1 

n=6
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i>=j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
"""