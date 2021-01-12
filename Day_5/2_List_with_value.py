# Initialing the value
fruits = ['banana', 'orange', 'mango', 'lemon', 'apple']
print('Fruits:', fruits)
print('Length of Fruits List:', len(fruits))
# List can have items of different data types.
lst = ['Nishanth', 15, True, {'Country': 'India', 'City': 'Coimbatore'}]
print(lst)

# Index of list
# [a, b, c, d, e]
#  0, 1, 2, 3, 4    - In Positive Indexing
# -5,-4,-3,-2,-1    - In Negative Indexing
# calling values in list by index
ls = ['a', 'b', 'c', 'd', 'e']
print(ls[2])    # calling 3rd value in index
print(ls[-1])   # calling last value in index

# Unpacking the list by assigning the values
a, b, c, *rest = ls  # the index value will be assigned to this variables seperated by ,
print(a)
print(rest)     # *rest is used for collecting other values in a upacked list
