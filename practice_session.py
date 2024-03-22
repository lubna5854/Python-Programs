# def sorting(arr):
#     res=arr.sort()
#     return res
#
# arr=[0,2,1,2,0]
# # length=len(arr)
# # print("Sorted array: ",sorting(arr))
# #
#
# def sorting(arr):
#     res = sorted(arr)
#     return res
#
# arr = [0, 2, 1, 2, 0]
# print("Sorted array:", sorting(arr))
n = 6

# Print the top half of the pattern in reverse
for i in range(n, 0, -1):
    for s in range(i - 1):
        print(" ", end="")
    for j in range(i, n + 1):
        print(j, end="")
    print()

# Print the bottom half of the pattern in reverse
for i in range(n - 1, 0, -1):
    for s in range(n - i - 1):
        print(" ", end="")
    for j in range(n - i, n + 1):
        print(j, end="")
    print()
