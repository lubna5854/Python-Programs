# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

user_input = input("Enter numbers separated by space: ")
length=len(user_input)
arr= [int(x) for x in user_input.split()]

# arr=[3,2,8,4]
a=0
length=len(arr)

for i in range(0,length):
    for j in range(i+1,length):
        if arr[i]>=arr[j]:
            arr[i],arr[j]=arr[j],arr[i]

print("Sorted array: ",arr)