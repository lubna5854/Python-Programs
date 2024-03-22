"""
asci=65
n=5
for i in range(n):
    for j in range(i+1):
        print(chr(asci),end=" ")
        asci += 1
    print()

output
A
B C
D E F
G H I J
K L M N O
"""
"""
word="Python"
n=5
x=""
for i in word:
    x += i
    print(x)
    
output
P
Py
Pyt
Pyth
Pytho
Python
"""

"""
asci=65
n=6
for i in range(n):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print(chr(asci),end=" ")
        asci += 1
    print()
    
output
                A
              B C D
            E F G H I
          J K L M N O P
        Q R S T U V W X Y
"""

"""
n=6
for i in range(n):
    for k in range(n-i):
        print(" ",end=" ")
    asci = 65
    for j in range(2*i-1):
        print(chr(asci),end=" ")
        asci += 1
    print()
#
#         A
#       A B C
#     A B C D E
#   A B C D E F G
# A B C D E F G H I
"""

"""
str2="PQR"
str1="ABCD"

for i in range(4):
    print(str1[0:i+1] + str2[i:])
    
A P Q R
A B Q R
A B C R
A B C D
"""

"""
string1="IAS"
for j in range(1,3):
    print(string1[-j:],end=" ")
    print()
for i in range(3,0,-1):
    print(string1[3-i:],end=" ")
    print()
 
S
AS
IAS
AS
S   
"""

