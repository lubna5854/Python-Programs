# finding duplicated elements

ques=[55,44,11,22,44,55,11,33,66,88,88,88,44,88,88]
dup=[]
res=[]


for i in ques:
    if i not in dup:
        dup.append(i)
    elif i not in res:
        res.append(i)
    else:
        continue
print("dupliacte elements: ",res)
dup.sort()
print(dup)

# [res.append(i) for i in input_list if i not in res]