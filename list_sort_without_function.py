# write a program to find the smallest number among four numbers

array = [4, 8, 6, 7, 9, 3]
# array=[x for x in input("Enter the numbers separated by space: ").split()]
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] >= array[j]:
            array[i], array[j] = array[j], array[i]
print("smallest number is {}".format(array[0]))

