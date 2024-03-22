lis=[5,4,3,4,6,8,7,8,8,8,4]
res=sorted(lis,key=lis.count,reverse=True)
print(res)

# output
# [8, 8, 8, 8, 4, 4, 4, 5, 3, 6, 7]
