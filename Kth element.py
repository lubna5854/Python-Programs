# Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given
# array. It is given that all array elements are distinct.

arr=[7,10,4,3,20,15]
arr.sort()
print(arr)
k=int(input("Enter index number: "))
print("Element:",arr[k-1])
