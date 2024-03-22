# Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or
# equal to all the elements to its right side. The rightmost element is always a leader.

def LeaderinArray(A,n):
    leaders=[]
    right=A[-1]
    for i in range(n-1, -1, -1):
        if A[i] >= right:
            leaders.append(A[i])
            right = A[i]
    leaders.reverse()
    return leaders

A=[16,17,4,3,5,35]
length=len(A)
print(LeaderinArray(A,length))