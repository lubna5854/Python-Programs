# Given two integer array A and B of size N each. A sum combination is made by adding one element from array A and another element of array B.
# Return the maximum K valid sum combinations from all the possible sum combinations.
# Note : Output array must be sorted in non-increasing order.

# Example 1:
#
# Input:
# N = 2
# K = 2
# A [ ] = {3, 2}
# B [ ] = {1, 4}   {4,7,3,6}  {7,6}
# Output: {7, 6}
# Explanation:
# 7 -> (A : 3) + (B : 4)
# 6 -> (A : 2) + (B : 4)


#
# for i in A:
#     for j in B:
#         sum_AB.append(i+j)
def mxmsumcombination(A,B,k):
    sum_AB=[]
    sum_AB=[i+j for i in A for j in B]
    sum_AB.sort(reverse=True)
    return sum_AB[:k]

A=[1, 4, 2, 3]
B=[2, 5, 1, 6]
k=int(input("Enter number: "))
print(mxmsumcombination(A,B,k))