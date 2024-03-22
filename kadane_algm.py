# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

# user_input = input("Enter numbers separated by space: ")
# length=len(user_input)
# arr= [int(x) for x in user_input.split()]


def kadane(max_value,arr,length):
    max_sum = arr[0]
    current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
    # for i in range(length):
    #     sum = 0
    #     for j in range(i,length):
    #         sum+=arr[j]
    #         if sum>max_value:
    #             max_value=sum
    # return max_value


arr = [1,-2,3,2,-5]
length = len(arr)
max_value = max(arr)
print("Max: ",max_value)
print("Value",kadane(max_value,arr,length))