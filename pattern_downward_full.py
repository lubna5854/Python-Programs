n = 6
for i in range(1,n+1):
    for s in range(i - 1):
        print(" ",end="")
    for j in range(i, n + 1):
        print(j, end="")
    print()
for i in range(1, n):
    for s in range(n - i - 1):
        print(" ",end="")
    for j in range(n - i, n + 1):
        print(j,end="")
    print()

# output
# 123456
#  23456
#   3456
#    456
#     56
#      6
#     56
#    456
#   3456
#  23456
# 123456