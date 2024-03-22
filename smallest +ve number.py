# You are given an array arr[] of N integers. The task is to find the smallest positive number missing from the array.
def smallest(arr):
    arr.sort()
    positive_array=[i for i in arr if i>0]
    if positive_array==[]:
        return 1
    for i in range(1,len(positive_array)+1):
        if positive_array[i-1]==i:
            continue
        else:
            return i
    return i+1

input_list=[1,1,2,5,6,-10,-6]
dup = []
res = []
for i in input_list:
    if i not in dup:
        dup.append(i)
    elif i not in res:
        res.append(i)
    else:
        continue
print("Missing :",smallest(dup))