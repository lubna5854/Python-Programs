"""
Python program to check whether the string is Symmetrical or Palindrome
"""

input_string=input("Enter the String: ")
length= int(len(input_string)/2)
first_string=input_string[:length]
second_string=input_string[length:]

# check string is symmetric or not

if first_string == second_string:
    print("symmetric")
else:
    print("Not symmetric")

# check is string palindrome

if input_string==input_string[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")