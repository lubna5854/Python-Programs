# n =5
# for i in range(1,n+1):
#     for s in range(i - 1):
#         print(" ",end=" ")
#     for j in range(i, n + 1):
#         print(j, end=" ")
#     print()

"""
1 2 3 4 5
  2 3 4 5
    3 4 5
      4 5
        5 """

"""
n =4
num=1
for i in range(1,n+1):
    for s in range(i - 1):
        print(" ",end=" ")
    for j in range(i, n + 1):
        print(num, end=" ")
        num += 1
    print()
    
1 2 3 4 
  5 6 7 
    8 9 
      10 """