"""
Python program to find the sum of all items in a dictionary
"""

my_dict = {"Remya": 345, "Arun": 257, "Tarun": 652, "Vidya": 365, "Lubna": 658}
Sum = 0
for item in my_dict.values():
    Sum = Sum + item
print("Sum of values: ",Sum)

