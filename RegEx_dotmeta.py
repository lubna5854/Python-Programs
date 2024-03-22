
import re
x="h.l..i"
text=input("Enter your text: ")
if re.match(x,text):
    print("Correct")
else:
    print("Not match")