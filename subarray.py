# Given an unsorted array A of size N that contains only positive integers, find a continuous sub-array that adds to a given number S
# and return the left and right index(1-based indexing) of that subarray
#
# Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements
# from 2nd position to 4th position
# is 12.
def subArray(arr,length,s):
    for i in range(length):
        sum=0
        for j in range(i,length):
            sum+=arr[j]
            if sum==s:
                return [i+1,j+1]
            elif sum>s:
                break
    else:
        return -1

arr=[1,2,3,5,4,8,7,9]
length=len(arr)
s=int(input("Enter sum: "))
print(subArray(arr,length,s))
