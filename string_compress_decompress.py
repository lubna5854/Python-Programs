a = input()
c = 0
i = 0
b=""
while c <(len(a)):
    if a[i] == a[c]:
        c += 1
    else:
        b += (str(c-i) + a[i])
        i = c
b += (str(c-i) + a[i])
print(b)
#
# input_string = input("Enter string: ")
# str_dict = {}
# count=0
# temp=""
# for char in range(len(str_dict)):
#     if str_dict[char]==count:
#         count += 1
#     else:
#         temp += str(count-char) + str_dict[count-char]
#         char=count
#     temp += str(count-char) + str_dict[char]
#
#
#

