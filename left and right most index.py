# Given a sorted array with possibly duplicate elements.The task is to find indexes of first and last occurrences of an element X in the
# given array.
# Note: If the element is not present in the array return {-1, -1} as pair.

# Example
# Input:
# N = 9
# v[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}
# X = 5
# Output:
# 2
# 5
# flag=True

def leftright(arr,x):
    a=[]
    if x in arr:
        for i in range(len(arr)):
            if x==arr[i]:
                a.append(i)
        return [a[0],a[-1]]
    else:
        return [-1,-1]

arr=[1,1,3,4,4,5,5]
user_input=int(input("Enter the number:"))
print("Index: ",leftright(arr,user_input))