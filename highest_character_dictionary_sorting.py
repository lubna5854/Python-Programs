
"""
read a string from user. find the highest repeated character from the string. print it in the descending order

"""


string_dict={}
input_string=input("Enter the string: ")
for i in input_string:
    if i in string_dict:
        string_dict[i] += 1
    else:
        string_dict[i] =1
print("highest repeated character: ", max(string_dict,key=string_dict.get))
# sort by keys
print("Dictoinary in Descending order by key: ",dict(sorted(string_dict.items())))

# sort by values
print("Sort by values: ",dict(sorted(string_dict.items(),key=lambda item:item[1],reverse=True)))