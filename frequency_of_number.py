# frequency of number

input_list=[2,5,4,3,2,4,5,7,8,2,5]
number=int(input("Enter the number: "))
count=0

for i in input_list:
    if i == number:
        count += 1
print("Frequency of {} is {}".format(number,count))

"""
output

Enter the number: 2
Frequency of 2 is 3
"""
"""
# frequency of each element in list
input_list=[2,5,4,3,2,4,5,7,8,2,5]
# number=int(input("Enter the number: "))
dic={}
for i in input_list:
    count=0
    for j in input_list:
        if i==j:
            count += 1
        dic[i]=count
for key,val in dic.items():
    print("Frequency of {} is {}".format(key,val))
"""