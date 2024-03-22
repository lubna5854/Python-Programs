# Given two sorted arrays of distinct elements. There is only 1 difference between the arrays.
# First array has one element extra added in between. Find the index of the extra element.

user_input = input("Enter numbers separated by space: ")
arr= [int(x) for x in user_input.split()]

user_input1 = input("Enter numbers separated by space: ")
arr1= [int(x) for x in user_input1.split()]

sum1= sum(arr)
sum2=sum(arr1)
if sum1> sum2:
    res = sum1 - sum2
    print("Missing number index:",arr.index(res))
else:
    res=sum2-sum1
    print("Missing number index: ",arr1.index(res))
