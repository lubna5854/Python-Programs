"""
Program to find a string is contained in a ascribbed text
pattern= "OLONSEIGHCET"
input=solo   output= Present
input= noon    output= Absent

"""
def string_check(input_string,pattern):
    input_string = input_string.lower()
    pattern = pattern.lower()

    for i in input_string:
        if i in pattern:
            pattern=pattern.replace(i," ",1)
        else:
            return "Absent"
    return "Present"

input_string=input("Enter the string: ")
pattern="OLONSEIGHCET"
print(string_check(input_string,pattern))