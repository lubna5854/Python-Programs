'''
program to interchange first and last elements in the list
'''

list1=[1,2,3,4,5,6]
a=list1[-1]
list1[-1]=list1[0]
list1[0]=a
print(list1)
