# Given a sorted array containing only 0s and 1s, find the transition point.

# Example 1:
# Input:
# N = 5
# arr[] = {0,0,0,1,1}
# Output: 3
# Explanation: index 3 is the transition point where 1 begins.

arr=[0,0,0,1,1]
length=len(arr)
for i in range(length):
    if arr[i]==1:
        res=arr[i]
print("Index",arr.index(res))