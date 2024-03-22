# import re
# input_string=input("Enter string: ")
# sub_string=input("Enter sub-string: ")
# res=re.findall(sub_string,input_string)
# print("Count of substring: ",len(res))

# string="lubna how are you lubna, lubna"
string="abababaaabbaba"
sub_string=input("Enter substring: ")
res=0
sub_len=len(sub_string)
for i in range(len(string)):
    if string[i:i+sub_len]==sub_string:
        res += 1
print("Substring count: ",res)