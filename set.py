# set operations

num={20,10,30,40,50,60,70}
num1={15,25,35,45,55,65,70,40}
print("Older set: ",num)
num.add(11)
num.remove(10)
print("New set: ",num)
print("2nd set of numbers: ",num1)
print("Union : ",num|num1)
print("Intersection: ",num & num1)
print("Digfference: ",num-num1)

# output

# Older set:  {50, 20, 70, 40, 10, 60, 30}
# New set:  {50, 20, 70, 40, 11, 60, 30}
# 2nd set of numbers:  {65, 35, 70, 40, 45, 15, 55, 25}
# Union :  {65, 35, 70, 40, 11, 45, 15, 50, 20, 55, 25, 60, 30}
# Intersection:  {40, 70}
# Digfference:  {11, 50, 20, 60, 30}