import numpy as np

input_list = []

input_list2 = []
n = int(input("Enter the number of rows: "))

for i in range(n):
    input1 = input("Enter 1st array row " + str(i+1) + ": ") # e.g. 1 2 and 3 4
    input_row = input1.split() # or split(",") if comma-separated
    input_list.append(input_row) # e.g. [["1", "2"], ["3", "4"]]
array = np.array(input_list, dtype=int) # e.g. array([[1, 2], [3, 4]])

for i in range(n):
    input2 = input("Enter 2nd array row " + str(i+1) + ": ") # e.g. 1 2 and 3 4
    input_row2 = input2.split() # or split(",") if comma-separated
    input_list2.append(input_row2) # e.g. [["1", "2"], ["3", "4"]]
array2 = np.array(input_list2, dtype=int) # e.g. array([[1, 2], [3, 4]])

print("Array1:")
print(array)
print("Array2: ")
print(array2)

# print('\nApplying mod() function:')
# print(np.mod(arr, arr1))
#
# print('\nApplying remainder() function:')
# print(np.remainder(arr, arr1))

print("Addition: ")
print(array+array2)
print("Subtraction: ")
print(array-array2)
print("Multiplication: ")
print(array*array2)
print("Division :")
print(array//array2)

print("After deletion: ")
dele=np.delete(array,(1,1))
print(dele)

print("After inseertion :")
ins=np.insert(dele, 2, 10)
print(ins)