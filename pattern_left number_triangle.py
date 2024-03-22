# left number triangle pattern
n = 5
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()

# output

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# print(2*(n-i), end=" ")
# 10
# 8 8
# 6 6 6
# 4 4 4 4
# 2 2 2 2 2

# print(i+1, end=" ")
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5