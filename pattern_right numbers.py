# right number triangle pattern
n = 5
for i in range(n):
    # print spaces
    for j in range(1, n - i):
        print(" ", end="")
    # print numbers
    for k in range(i + 1):
        print(k + 1, end="")
    print()

#     output
#     1
#    12
#   123
#  1234
# 12345