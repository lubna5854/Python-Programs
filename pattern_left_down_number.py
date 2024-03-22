n = 5
for i in range(n):
    # internal loop run for n - i times
    for j in range(n - i):
        #print(i+1, end=' ')
        print(2*(n-i)+1, end=' ')
    print()

#   OUTPUT
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# n = 5
# for i in range(1,n+1):
#     # internal loop run for n - i times
#     for j in range(n - i+1):
#         #print(i+1, end=' ')
#         print(i*2, end=' ')
#     print()
#
# 2 2 2 2 2
# 4 4 4 4
# 6 6 6
# 8 8
# 10

# print(n-i,end=" ")
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# print(j+1, end=' ')
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1