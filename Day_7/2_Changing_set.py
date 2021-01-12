# Set are mutable
# add() is used to add value in sets
st = {'items1', 'items2', 'items3', 'items4'}
print('Set', st)
st.add('items5')
print('After Add()', st)

# update() is used to add multiple in sets
st.update(['items6', 'items7', 'items8'])
print('After Update() function: ', st)

# clear() is used to clear the set
st.clear()
print('After Clear Function', st)

# del() is used to del the set
del st
print('Set is Deleted')


# Converting List to set
lst = ['item1', 'item2', 'item3', 'item2', 'item1']
st = set(lst)
print(lst)
print(st)

# Joining Set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st = st1.union(st2)
print("Set 1: {} \nSet 2: {} \nJoined Set: {}".format(st1, st2, st))

# Intersection
# returns a set of items which are in both sets.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st1.intersection(st2))
