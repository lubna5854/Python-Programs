#
# #list=[1,2,3,4,5,6,7,8,9,10,12,15,16]
# res=[]
# length=list[-1]
# for i in range(1,length+1):
#     if i in list:
#         continue
#     else:
#         res.append(i)
# print("Missing number:",res)


res=[]
# user_input = input("Enter numbers separated by space: ")
# input_list = [int(x) for x in user_input.split()]

input_list=[1,2,3,4,5,7]
# find least number to start range and highest number to end  the range
min_num=min(input_list)
max_num = max(input_list)

for i in range(min_num,max_num+1):
    if i in input_list:
        pass
    else:
        res.append(i)
print("Missing numbers: ",res)
