# Dictionary are mutable
dct = {'Key1': 'Value1', 'Key2': 'Value2', 'Key3': 'Value3', 'Key4': 'Value4'}
print("Before Adding:", dct)
dct['Key5'] = 'Value5'
print('After Adding', dct)

# Changing Values in Dictionary repescted to key
dct['Key1'] = 'Values-one'
print('Modified Dictionary', dct)

# To check keys in a dictionary
print("'key1' in dictionary", 'key1' in dct)
print("'key3' in dictionary", 'key3' in dct)

# To remove the key and value pairs from a dictionary
print('Before Changing:', dct)
# pop(key)
dct.popitem()       # Removes last item
print(dct)
# popitem()
dct.pop('Key1')     # Removes the value of Key1
print(dct)
# del function
del dct['Key2']

# Changing Dictionary to a list of items
dct = {'Key1': 'Value1', 'Key2': 'Value2', 'Key3': 'Value3', 'Key4': 'Value4'}
# items() is used collect the keys along with values
print(dct.items())

# Clearing a Dictionary
# Clear()
print(dct.clear())

# Copy a Dictionary
dct_copy = dct.copy()
print(dct_copy)

# Getting Dictionary keys as a List
keys = dct.keys()
print(keys)

# Getting Dictionary Values as a List
values = dct.values()
print(values)

# Deleting a Dictionary
del dct
print('Dictionary is Deleted')
