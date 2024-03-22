
import re
x=input("Enter your text")
text="[a-z][0-9][A-Z]"
if re.search(text,x):
    print("Match")
else:
    print("Not match")

    # OUTPUT
    #
    # Enter your text : a5L
    # Match