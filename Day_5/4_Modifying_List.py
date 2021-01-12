# Modifying List
# List are Mutable
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
fruits[0] = 'avocado'   # Changing the value at the index of 0 in the list.
fruits[-1] = 'lime'     # changing the value at the last index in the list.
print(fruits)
# Checking items in aList
print('lime' in fruits)     # list consists of lime, which was added
print('apple' in fruits)    # apple is not in the list,so it return False

# Insert() method
lst = ['item1', 'items2']
lst.insert(2, 'item')   # At 2nd index we added item in our list
print('After Insert()', lst)

# Remove() method
lst.remove('item')
print('After Remove()', lst)

# Pop() method
lst.pop()   # Removes last value in index, can be used by index values
print('After pop', lst)

# CLear() method
lst.clear()
print('After Clear', lst)   # clears the list,i.e, del all value in list

# Del keyword
'''
del lst
print('After del', lst)     # Del the whole list
'''

# Copying List
lst = ['item1', 'items2']
lst_copy = lst.copy()   # Copy function is used to copy a list
print('Copied list', lst_copy)

# Reverse List
lst.reverse()           # Reverse function is used to reverse the function
print('Reversed List', lst)

# Sorting a List
lst = [5, 7, 2, 4, 9, 1, 3, 0]
lst.sort()
print(lst)   # Sort function is used to sort the list
lst.sort(reverse=True)
print(lst)   # To reverse sort the list

# Joing two list
ls1 = [1, 2, 3, 4, 5]
ls2 = [10, 20, 30, 40]

# Plus Operation
ls_plus = ls1 + ls2
print('Using Plus Operation', ls_plus)

# Extend method
ls1.extend(ls2)
print('Using Extend method', ls1)

# Index() method
print(ls1.index(10))   # To find the index of a list
