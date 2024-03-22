#
# """Write an algorithm for calculating the number of vowels and consonants in a string."""

"""
# By using RE
import re
input_string=input("Enter the string: ")
vowels = r'a|e|i|o|u'
matches=re.findall(vowels,input_string)
print("Vowels are {} and Consonants are {} ".format(len(matches),len(input_string)-len(matches)))
"""

input_string=input("Enter the string: ")
vowels=['a','e','i','o','u']
count=0
vowel=0
for i in input_string:
    if i in vowels:
        count += 1
    else:
        vowel += 1
print("Vowels are {} and Consonants are {} ".format(count,vowel))
