# arrange positive and negative numbers separately

array=[-10,-23,-5,-41,8,4,6,7,-13,56,10]
res=[]
res1=[]
for i in array:
    if i<0:
        res.append(i)
    else:
        res1.append(i)
res.extend(res1)
print(res)