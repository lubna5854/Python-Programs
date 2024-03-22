# create a tuple and do the operations

tup=(12,"hello",45,"hai","Eight",86,"new","Myself",78,49)
lis_conv=list(tup)
print("List before operations: ",lis_conv)
lis_conv.insert(5,"Diana")
lis_conv.append("Elizabeth")
print("Index of second last element: ",lis_conv.index(78)+1)
tup=tuple(lis_conv)
print("List after operation: ",tup)