input_string=input("Enter the string: ")
str_dict={}
for i in input_string:
    if i in str_dict:
        str_dict[i] += 1
    else:
        str_dict[i] = 1
for key, value in str_dict.items():
    print(f"{value}{key}",end="")

"""
OUTPUT
Enter the string: hhaahhrrttaa
4h4a2r2t
"""