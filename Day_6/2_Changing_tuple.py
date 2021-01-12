# Tuple are immutable
# Slicing Tuple
tp = ('item1', 'items2', 'item3', 'items4')
# Positive Indexing
print(tp[1:3])  # 3rd index value will not be included
print(tp[0:])   # To print all value in Tuple
# Neagtive Indexing
print(tp[-3:-1])    # -1 value will not be included
print(tp[-4:])       # prints all values

# we can change tuple values by converting it into list
lst = list(tp)
lst[0] = 'hi'
tp = tuple(lst)
print(tp)

# To check the value
print('item3' in tp)
print('items' in tp)

# Joining tuple with plus Operation
tp1 = (1, 2, 3, 4)
tp2 = (9, 8, 7, 6)
tp = tp1 + tp2
print(tp)

# Deleting Tuple
del tp1
print('tuple has been delete', tp1)
