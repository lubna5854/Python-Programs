"""
array=[1,1,3,4]
find the duplicate, and replace the correct number, then add it with duplicate
ex.in this array duplicate is 1 and missing is 2, the result is 2+1=3
"""
arr = [5, 11, 9, 6, 8, 7,9]
arr.sort()
print(arr)

result = 0
min_value = min(arr)
max_value = max(arr)

for i in range(min_value, max_value):
    if i not in arr:
        result = i + i-1
        break

print("The result is:", result)

