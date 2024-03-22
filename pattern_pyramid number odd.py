for i in range(5):
    for j in range(5 - i):
        print(' ', end=' ')
    for k in range(2 * i - 1):
        print(2*i-1, end=' ')
    print()

# OUTPUT
#       1
#     3 3 3
#    5 5 5 5 5
# 7 7 7 7 7 7 7

  #   print(k + 1, end=' ')
  #       1
  #     1 2 3
  #   1 2 3 4 5
  # 1 2 3 4 5 6 7
