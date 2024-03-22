# 123456
# 213456
# 231456
# 234156
# 234516
# 234561

list=[]
size=int(input("Enter Limit: "))
for j in range(1,size+1):
    list.append(str(j))
for i in range(size):
    if i == 0:
        print("".join(list))
    else:
        list[i],list[i-1]=list[i-1],list[i]
        print("".join(list))


"""
list[i]=list[i-1]
list[i-1]=list[i]
"""