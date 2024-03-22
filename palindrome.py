# Palindrome checking

# def pal(string):
#     res=string[::-1]
#     if string==res:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")

# string=input("Enter string: ")
# pal(string)

# palindrome number series
def pal(string):
    res=string[::-1]
    if res==string:
        return True
print("Palindrome numbers are: ")
for i in range(1000):
    if pal(str(i)):
        print(i)
