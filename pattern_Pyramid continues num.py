
for i in range(5):
    for j in range(5 - i):
        print(' ', end=' ')
    for k in range(2 * i - 1):
        print(i, end=' ')
    print()

# OUTPUT
#     1
#    2 2 2
#   3 3 3 3
# 4 4 4 4 4 4