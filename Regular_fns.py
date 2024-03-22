# Pgm for Regular expression

import re
pattern=str(input("Enter your pattern: "))
text="Hello how are you, hope you are fine, Are you?"

""" 1. for exact match"""

if re.match(pattern.lower(),text.lower()):
#if re.match(pattern,text):
    print("Matched")
else:
    print("The entered word Not matched")

# 2. for search in a text

if re.search(pattern,text):
    print("The word is in the sentence")
else:
    print("The word is not in sentence")

# 3. findall
tex="GeeksforGeeks: A computer science portal for geeks"
#print("The entered word in th list :",re.findall(pattern,text))
pattern=r'[Gg]eeks'
matches=re.findall(pattern,tex)
print("String geeks:",len(matches))
#print(re.findall(r'[Gg]eeks', 'GeeksforGeeks: A computer science portal for geeks'))


#4.find and replace

print("New Text: ",re.sub(pattern,"Hello Lubna",text))

# 5. Date validation
print('Date{mm-dd-yyyy}:', re.search(r'[\d]{2}-[\d]{2}-[\d]{4}',
									'18-08-2020'))

#6. split()
pattern_split='\s'
split_text=re.split(pattern_split,text)
print("Split text:",split_text)

#7. . to match any character

pattern_dot = "Py...n"
text = "I love Python, Pyt3on, Py45n, and Py@#n!"
matches = re.findall(pattern_dot, text)
print("Matches found:", len(matches))

#Using * to match zero or more occurrences of a character
pattern_occ = "Py.*n"
count = 0
text = ["Python coding", "Pyt3on","Java", "Py45n", "Py@#n","Pyn"]
for i in text:
    if(re.findall(pattern_occ, i)):
        count+=1
print("Occurence Matches found:", count)

#Using ? to match zero or one occurrence of a character
pattern_zero = "Py.?n"
count = 0
text = ["Python coding", "Pyt3on","Java", "Py45n", "Py@#n","Pyn"]
for i in text:
    if(re.findall(pattern_zero, i)):
        count+=1
print("Matches found:", count)

#Using {} to specify the number of occurrences of a character
pattern_curly = "Py{1,2}n"
text = "I love Pyn, Pyyn, and Pyyyn!"
matches = re.findall(pattern_curly, text)
print("Matches found:", len(matches))

#Using \d to match digits

pattern_digit = "\d+"
text = "My phone number is 123-456-7890."
matches = re.findall(pattern_digit, text)
print(matches)
print("Matches found:", len(matches))

#Using \w to match alphanumeric characters
pattern = "\w+"
text = "I_love_Python!"
matches = re.findall(pattern, text)
print(matches)
print("Alpha numeric Matches found:", len(matches))

#Using \s to match whitespace characters

pattern = "\s+"
text = "I love Python!"
matches = re.findall(pattern, text)
print("String Matches found:", len(matches))

#Using | as an OR operator
pattern = "Python|Java"
text = "I write code in Python and Java!"
matches = re.findall(pattern, text)
print("Matches found:", len(matches))

#Using () to group patterns
pattern = "(\d{3})-(\d{3})-(\d{4})"
text = "My phone number is 123-456-7890."
match = re.search(pattern, text)
if match:
    print("Area code:", match.group(1))
    print("Local exchange:", match.group(2))
    print("Line number:", match.group(3))

