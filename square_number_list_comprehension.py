# Create a Python list comprehension to generate a list of squares of even numbers from 1 to 10.

# li=[2, 3, 4, 5, 6]
li=[int(x) for x in input("Enter the numbers separated by space: ").split()]
square_list=[x**2 for x in li if x % 2 == 0]
print(square_list)