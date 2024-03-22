input_string= "Hello world how are you..?"
words = input_string.split()
replace=input("Word to replace: ")
insert_word=input("Word to insert: ")

if replace in input_string:
    index1=words.index(replace)
    words[index1]=insert_word
    new_string=' '.join(words)
else:
    print("Entered word is not in string..")
print(new_string)

"""
output
Word to replace: world
Word to insert: Lubna
Hello Lubna how are you..?
"""