
input_string =input("Enter input: ")
char_count = {}
result = ""
for char in input_string:
    char_count[char] = char_count.get(char, 0) + 1
for char, count in char_count.items():
    result += str(count) + char
print("Result: ",result)



