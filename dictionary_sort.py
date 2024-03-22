'''
Sort dictionary by value and key
'''

my_dict = {'apple': 3, 'banana': 1, 'orange': 2, 'grape': 4}
print("The dictionary keys: ",my_dict)
SortByvalue=dict(sorted(my_dict.items()))
print("Dictionary sorted by value :", SortByvalue)

SortBykey = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by Key: ", SortBykey)

'''
item[1]: This is the expression that specifies what to use as the sorting key. In Python, dictionaries are iterable,
 and iterating over a dictionary yields its keys. So, item[1] refers to the value associated with each key.
'''