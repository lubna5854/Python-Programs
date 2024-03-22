def ascii_number(input_string):
    result=0
    for char in input_string:
        result=result * 26 +( ord(char) - ord('A') + 1)
    return result

input_string=input("Enter string: ")
print("Ascii number: ",ascii_number(input_string))

"""
Enter string: AA
Ascii number:  27
"""