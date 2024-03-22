# Return the numbers in their order of appearing twice.
# So, if X and Y are the repeating numbers, and X repeats twice before Y repeating twice, then the order should be (X, Y).

# Example 1:
# Input:
# N = 4
# array[] = {1,2,1,3,4,3}
# Output: 1 3
# Explanation: In the given array, 1 and 3 are repeated two times.


arr=[1,2,3,3,2,4,5]
res=[]
# for i in arr:
#     if i not in dup:
#         dup.append(i)
#     elif i not in res:
#         res.append(i)
#     else:
#         continue
seen = set()
res = [x for x in arr if x in seen or seen.add(x)]
print("dupliacte elements: ",res)
