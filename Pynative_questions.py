
"""
**********************************  Print characters from a string that are present at an even index number  *********************************

string="Lubna"
print(string[::2])

*********************  Remove first n characters from a string  ***************************************

string="Lubna-ap"
val=int(input("Enter number to remove alphabets: "))
print(string[val::])

***********************  Check if the first and last number of a list is the same ************************************

list1=[12,25,45,23,56,12]

if list1[0]==list1[-1]:
    print("Both are same")
else:
    print("Values are different")

*********************************** Return the count of a given substring from a string ************************************************
import re
string="Lubna -ap hello lubna how are you lubna"
string=string.lower()
pattern=input("Enter the string you want to search: ")
match=re.findall(pattern,string)
print("The substring count is {}".format(len(match)))

# using loop
# string="lubna how are you lubna, lubna"
string="abababaaabbaba"
sub_string=input("Enter substring: ")
res=0
sub_len=len(sub_string)
for i in range(len(string)):
    if string[i:i+sub_len]==sub_string:
        res += 1
print("Substring count: ",res)

# using string method

string="Lubna -ap hello lubna how are you lubna"
string=string.lower()
sub_string=input("Enter the substring: ")
print("The substring count is ",string.count(sub_string))

# using method startswith()
string="Lubna -ap hello lubna how are you lubna"
string=string.lower()
sub_string=input("Enter the substring: ")
res=sum(1 for i in range(len(string)) if string.startswith(sub_string,i))
print("Count : ",res)

*************************  Write a Program to extract each digit from an integer in the reverse order.   ******************************
number=int(input("Enter the number: "))
while number>0:
    rev=number%10
    number=number//10
    print(rev,end=" ")

**********************   Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.   ******************************************************
a=int(input("Base: "))
b=int(input("Exponent: "))
print("{} raised to the power {} is {}".format(a,b,a**b))

"""

