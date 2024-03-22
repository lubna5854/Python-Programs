"""
Given the names and grades for each student in a class of n students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second-lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

    students.sort(key=lambda x:x[1])
    print("List :",students)
    score=list(set(x[1] for x in students))
    score.sort()
    second_lowest=score[1]
    print("Second lowest: ",second_lowest)

    lowest_list=[]
    for i in students:
        if second_lowest== i[1]:
            lowest_list.append(i[0])
    lowest_list.sort()
    for i in lowest_list:
        print(i)

                                *************************************************************************************

The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
 Print the average of the marks array for the student name provided, showing 2 places after the decimal.

 if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(student_marks)
    if query_name in student_marks:
        print(sum(student_marks[query_name])/len(student_marks[query_name]))

                            ***************************************************************************************

You are given a two lists a and b . Your task is to compute their cartesian product aXb.

from itertools import product
a=list(map(int,input().split()))
b=list(map(int,input().split()))
pdt=list(product(a,b))
for i in pdt:
    print(i,end=",")

*** itertools.permutation()
This tool returns successive r length permutations of elements in an iterable.If  r is not specified or is None, then  r defaults to the length of
 the iterable, and all possible full length permutations are generated.Permutations are printed in a lexicographic sorted order. So, if the input
  iterable is sorted, the permutation tuples will be produced in a sorted order.  ***

from itertools import permutations
perm=[]
my_string,length=input().split()
perm=list(permutations(my_string,int(length)))
perm.sort()
for i in perm:
    print(''.join(i))

                                ****************************************************************************************

itertools.combinations(iterable, r)
This tool returns the  length subsequences of elements from the input iterable.Combinations are emitted in lexicographic sorted order. So, if the
 input iterable is sorted, the combination tuples will be produced in sorted order.

from itertools import combinations
combi=[]
my_string,length=input().split()
for i in range(1,int(length)+1):
    for j in combinations(sorted(my_string),i):
        print(''.join(j))


from itertools import combinations_with_replacement
combi=[]
my_string,length=input().split()
combi=list(combinations_with_replacement(sorted(my_string),int(length)))
# combi.sort()
for i in combi:
    print(''.join(i))

                            *******************************************************************************************

In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function,
 Check this out . You are given a string s . Suppose a character c occurs consecutively x times in the string. Replace these consecutive occurrences
  of the character c with (x,c) in the string.

from itertools import groupby
string=input()
list1=[]
for (key, group) in groupby(string):
  list1.append((len(list(group)),int(key)))
print(*list1)
                    *****************************************************************************************************
ou are given a list of n  lowercase English letters. For a given integer k, you can select any k  indices (assume -based indexing) with a
 uniform probability from the list. Find the probability that at least one of the k  indices selected will contain the letter: 'a'.

from itertools import combinations
count,input_string,select=int(input()),input().split(),int(input())
input_string.sort()
combi=list(combinations(input_string,select))
letter=len([x for x in combi if 'a' in x])
print(letter/len(combi))

**********************************************************************************************************************************************
Your task is to sort the string  in the following manner:
--- > All sorted lowercase letters are ahead of uppercase letters.
--- > All sorted uppercase letters are ahead of digits.
--- > All sorted odd digits are ahead of sorted even digits.

input_string=input()
lower=sorted([x for x in input_string if x.islower()])
upper=sorted([x for x in input_string if x.isupper()])
odd=sorted([x for x in input_string if x.isdigit() and int(x)%2!=0])
even=sorted([x for x in input_string if x.isdigit() and int(x)%2==0])
print(''.join(lower+upper+odd+even))
******************************************************************************************************************************************
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
The design should have ‘WELCOME’ written in the center.
The design pattern should only use |, . and – characters.
****************************************************************************************************************************************

You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    result=""
    for char in s:
        if char.islower():
            result +=char.upper()
        else:
            result +=char.lower()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    *************************************************************************************************************
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.

string="abababaaabbaba"
sub_string=input("Enter substring: ")
res=0
sub_len=len(sub_string)
for i in range(len(string)):
    if string[i:i+sub_len]==sub_string:
        res += 1
print("Substring count: ",res)
********************************************************************************************************************
In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
In the second line, print True if s has any alphabetical characters. Otherwise, print False.
In the third line, print True if s has any digits. Otherwise, print False.
In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
In the fifth line, print True if s has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':
    s = input("Enter a string: ")

    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))
**************************************************************************************************************
You are given a string s and width w.
Your task is to wrap the string into a paragraph of width .

input_string,width=input(),int(input())
for i in range(0,len(input_string),width):
    result=input_string[i:i+width]
    if len(result)==width:
        print(result)
    else:
        print(result)
*********************************************************************************************************************
Pattern of door mat

n,n1=map(int,input().split())
c = 3
k1=int((n1-3)/2)
for i in range(1,n//2+1):
    for j in range(k1):
        print('-', end='')
    for k in range(2 * i - 1):
        print(".|.", end='')
    for j in range(k1):
        print('-', end='')
    k1 -= 3
    print()
for j in range(1):
    for k in range(n):
        print("-", end="")
    print("WELCOME", end="")
    for k in range(n):
        print("-", end="")
    print()
for i in range(1,n//2+1):
    for j in range(c):
        print('-', end='')
    for l in range(2*(n//2-i)+1):
        print('.|.', end='')
    for j in range(c):
        print('-', end='')
    c+=3
    print()
print()

*********** another method *********************
n,m=map(int,input().split())
for i in range(1,n,2):
    print(str(".|."*i).center(m,'-'))
print("WELCOME".center(m,'-'))
for i in range(n-2,-1,-2):
    print(str(".|."*i).center(m,'-'))

output

7 21
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
***********************************************************************************************************************
Given an integer, n, print the following values for each integer  from 1 to n :

Decimal
Octal
Hexadecimal (capitalized)
Binary

def formatting(number):
    width=len(bin(number)[2:])
    for i in range(1,n+1):
        deci=str(i)
        octa=oct(i)[2:]
        hexa=hex(i)[2:].upper()
        bina=bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))

n=int(input())
formatting(n)
*********************************************************************************************************************
You are given an integer, N. Your task is to print an alphabet rangoli of size N.
(Rangoli is a form of Indian folk art based on creation of patterns.)

import string
n=int(input())
design = string.ascii_lowercase

lis = []
for i in range(n):
    s = "-".join(design[i:n])
    lis.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))

print('\n'.join(lis[:0:-1] + lis))

5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
**************************************************************************************************************************
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalized correctly as Alison Heck.

s=input()
for i in s.split():
    s=s.replace(i,i.capitalize())
print(s)
**************************************************************************************************************************
Kevin and Stuart want to play the 'The Minion Game'.

def minion_game(string):
    vowels='AEIOU'
    str_length=len(string)
    kevin=0
    stuart=0
    for i in range(str_length):
        if string[i] in vowels:
            kevin+=str_length-i
        else:
            stuart+=str_length-i

    if kevin>stuart:
        print("Kevin",kevin)
    elif kevin<stuart:
        print("Stuart",stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
****************************************************************************************************************************
# Program for merge the character in string
input_string=input()
length=int(input())
temp=[]
temp_length=0
for i in input_string:
    temp_length += 1
    if i not in temp:
        temp.append(i)
    if temp_length==length:
        print(''.join(temp))
        temp_length=0
        temp=[]
output

aabbcccdgrqw
3

ab
bc
cdg
rqw
*************************************************************************************************************************
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection.
She asked for your help. You pick the stamps one by one from a stack of  country stamps. Find the total number of n distinct country stamps.

n=int(input())
country = set()
for i in range(n):
    country.add(input())
print(len(country))
***********************************************************************************************************************
set operations

length = int(input())
s = set(map(int, input().split()))
n=int(input())
for i in range(n):
    cmd=list(map(str,input().split()))
    if cmd[0]=='pop':
        s.pop()
    elif cmd[0]=='remove':
        s.remove(int(cmd[1]))
    elif cmd[0]=='discard':
        s.discard(int(cmd[1]))
print(sum(s))
***********************************************************************************************************************
# set union operation
n = int(input())
l = list(input().split())
m = int(input())
k = list(input().split())
s1 = set(l)
s2 = set(k)
print(len(s1.union(s2)))

# difference (avail in set a(not set b and not common in set a and set b)
print(len(s1.difference(s2)))

#  print set a and set b, common elements left
print(len(s1.symmetric_difference(s2)))

# intersection
print(len(s1.intersection(s2)))
**********************************************************************************************************************
You are given a set A and N numbers of other sets. These N sets have to perform some specific mutation operations to set A.
Your task is to execute those operations and print the sum of elements of set A.


Input Format
First line contains, number of elements in set A.
Second line contains, space separated list of elements of set A.
Third line contains, N, number of other sets.
Next 2*N lines are divided into N parts of two lines each.
First line of each part contains, space separated entries of operation name and length of other set.
Second line of each part contains, space separated list of elements of other set.

n = int(input())
s = set(map(int, input().split()))
total=0
count = int(input())
for i in range(count):
    cmd = input().split()
    set_S= set(map(int, input().split()))

    if cmd[0] == 'intersection_update':
        s.intersection_update(set_S)
    elif cmd[0] == 'update':
        s.update(set_S)
    elif cmd[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(set_S)
    elif cmd[0] == 'difference_update':
        s.difference_update(set_S)
print(s)
for i in range(len(s)):
    total += int(s.pop())
print(total)

output
16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
{1, 2, 3, 4, 5, 6, 8, 9}
38
************************************************************************************************************************
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of K members per group where K ≠ 1.
The Captain was given a separate room, and the rest were given one room per group.
Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists.
The room numbers will appear K times per group except for the Captain's room.
Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of K and the room number list.

k = int(input())
rooms = list(map(int, input().split()))
seen = {}

for i in rooms:
    if i not in seen:
        seen[i] = 1
    else:
        seen[i] += 1
print(seen)

for key, val in seen.items():
    if val != k:
        print(key)
**************************************************************************************************************************************
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.
If set A is subset of set B, print True.
If set A is not a subset of set B, print False.
Input Format:-
The first line will contain the number of test cases, T.
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B.
test=int(input())
for i in range(test):
    n1=int(input())
    A=set(map(int,input().split()))
    n2=int(input())
    B=set(map(int,input().split()))
    if len(A-B)==0:
        print("True")
    else:
        print("False")
***********************************************************************************************************************************
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.
Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset.
Example
Set ([1 , 3, 4]) is a strict superset of set ([1 , 3]).
Set ([1 , 3, 4]) is not a strict superset of set ([1 , 3, 4]).
Set ([1 , 3, 4]) is not a strict superset of set ([1 , 3, 5]).

# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set(input().split())
n=int(input())
count=0
val=0
for i in range(n):
    if A.issuperset(set(input().split())):
        count += 1
    else:
        val += 1
if val!=0:
    print("False")
else:
    print("True")
***********************************************************************************************************************************************
You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers
are valid or not. You happen to be great at regex so he is asking for your help!
A valid credit card from ABCD Bank has the following characteristics:
► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen “-“.
► It must NOT use any other separator like ‘ ‘ , ‘_’, etc.
► It must NOT have 4 or more consecutive repeated digits.

import re
n=int(input())
for i in range(n):
    credit=input()
    pattern=r'^[4-6]\d{3}(-?\d{4}){3}$'
    if re.match(pattern,credit):
        credit=credit.replace('-','')
        if re.search(r'(\d)\1{3,}',credit):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")

*********************************************************************************************************************************************
You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). You are required to sort
the data based on the Kth attribute and print the final resulting table. Follow the example given below for better understanding.

n,m=map(int,input().split())
arr=[]
for i in range(n):
    line=input().split()
    arr.append([int(i) for i in line])
k=int(input())
arr.sort(key=lambda x:x[k])
for row in arr:
    print(' '.join(str(j) for j in row))
*********************************************************************************************************************************
any()
This expression returns True if any element of the iterable is true.
If the iterable is empty, it will return False.
all()
This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.
You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

n=int(input())
arr=input().split()
print(all([int(i) > 0 for i in arr]) and any([j == j[::-1] for j in arr]))
*****************************************************************************************************************************************
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.

Input Form at
The first line contains X, the number of shoes.
The second line contains the space-separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space-separated values of the shoe size desired by the customer and xi, the price of the shoe.

from collections import Counter
num=int(input())
shoe_size=Counter(map(int,input().split()))
cust=int(input())
total=0
for i in range(cust):
    size, price=map(int,input().split())
    if shoe_size[size]:
        shoe_size[size] -= 1
        total += price
print(total)
**************************************************************************************************************************
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name.
They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.
Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

from collections import Counter
input_string=input()
input_string=sorted(input_string)
lis=Counter(list(input_string))
for key,val in lis.most_common(3):
    print(f"{key} {val}")

output
ggghhhdtrrf
g 3
h 3
r 2
********************************************************************************************************************************************
Your task is to print an array of size N*M with its main diagonal elements as 1's and 0's everywhere else.
identity :
The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as 1 and the rest as 0.
The default type of elements is float.
import numpy
print numpy.identity(3) #3 is for  dimension 3 X 3

#Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]

The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main, upper or lower depending on the optional
 parameter K. A positive K is for the upper diagonal, a negative K is for the lower, and a 0 K (default) is for the main diagonal
 import numpy
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
[[ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]

print numpy.eye(8, 7, k = -2)

import numpy
numpy.set_printoptions(sign=' ')
print(numpy.eye(*map(int, input().split())))
# output
4 5
[[ 1.  0.  0.  0.  0.]
 [ 0.  1.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.]
 [ 0.  0.  0.  1.  0.]]
"""
"""Group A contains ‘a’, ‘b’, ‘a’ Group B contains ‘a’, ‘c’. For the first word in group B, ‘a’, it appears at positions 1 and 3 in group A.
 The second word, ‘c’, does not appear in group A, so print -1.

from collections import defaultdict
d=defaultdict(list)
n,m=map(int, input("Enter inputs").split())
for i in range(n):
    char=input("Input the character: ")
    d[char].append(i+1)
for j in range(m):
    char2=input("Enter character: ")
    if char2 in d:
        print(*d[char2])
    else:
        print(-1)

output
Enter inputs5 2
Input the character: a
Input the character: a
Input the character: b
Input the character: a
Input the character: b
Enter character: a
1 2 4
Enter character: b
3 5
 """
