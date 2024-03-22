n=5
for i in range(1,n+1):
    for j in range(i-1):
        print(' ', end=' ')
    for k in range(2*(n-i)+1):
        print((n+1-i),end=" ")
    print()

#  OUTPUT
#
# 5 5 5 5 5 5 5 5 5
#   4 4 4 4 4 4 4
#     3 3 3 3 3
#       2 2 2
#         1

#  print(2*(n-i)+1,end=" ")  for
# 9 9 9 9 9 9 9 9 9
#   7 7 7 7 7 7 7
#     5 5 5 5 5
#       3 3 3
#         1

# print(k, end=" ") for
#     0 1 2 3 4 5 6 7 8
#      0 1 2 3 4 5 6
#       0 1 2 3 4
#         0 1 2
#           0

# print(i, end=" ")
# 1 1 1 1 1 1 1 1 1
#   2 2 2 2 2 2 2
#     3 3 3 3 3
#       4 4 4
#         5


# print(2*(n-i), end=" ")
# 8 8 8 8 8 8 8 8 8
#   6 6 6 6 6 6 6
#     4 4 4 4 4
#       2 2 2
#         0