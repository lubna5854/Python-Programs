'''
Python program to create a list of tuples from given list having number and its cube in each tuple
'''

input_list = [2, 3, 4, 5, 9]
cube_list=[(val, val**3) for val in input_list]
print("the numbers and cubes: ",cube_list)

'''
output

the numbers and cubes:  [(2, 8), (3, 27), (4, 64), (5, 125), (9, 729)]
'''