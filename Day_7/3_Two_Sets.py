# Subset and Superset
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print('st2.issubset(st1):', st1.issuperset(st2))
print('st1.issuperset(st2):', st1.issuperset(st2))

# Difference between Two Sets (st1/st2)
print('st2.difference(st1):', st2.difference(st1))
print('st1.difference(st2):', st1.difference(st2))

# Finding symmetric difference Between TWO sets
print("st2.symmetric_difference(st1):", st2.symmetric_difference(st1))

# Joining Set
print("st2.isdisjoint(st1): ", st2.isdisjoint(st1))
