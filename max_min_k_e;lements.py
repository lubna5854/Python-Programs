'''
Python – Maximum and Minimum K elements in Tuple/List
'''
input_list = [2, 5, 7, 1, 3, 51, 45]
input_list.sort()
print("The sorted list: ",input_list)
count = int(input("Enter how many positions you need: "))
print("Minimum {} numbers".format(count),input_list[:count])
print("Maximum {} numbers".format(count),input_list[-count:])


'''
output

The sorted list:  [1, 2, 3, 5, 7, 45, 51]
Enter how many positions you need: 3
Minimum 3 numbers [1, 2, 3]
Maximum 3 numbers [7, 45, 51]
'''