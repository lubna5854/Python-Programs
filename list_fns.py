# list with all functions

x=input("Enter numbers : ")
input_list=[int(i) for i in x.split()]

input_list.append(2)
print("List after append:",input_list)

input_list.insert(4,8)
print("List after insert:",input_list)

indx=int(input("Which numberr u want to know the index: "))
print("Index of ",indx," is",input_list.index(indx))

input_list.remove(5)
print("After rempve",input_list)

input_list.pop(1)
print("After pop:",input_list)
print("Element: ",input_list.pop(2)) # pop also print 2nd index element, simultaneously it deletes the element from list
print("Input list:",input_list)

del input_list[::2]
print("After deletion: ",input_list)
