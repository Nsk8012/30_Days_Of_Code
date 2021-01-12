# For loop with range
# create variable with range
lst = list(range(11))
print(lst)
st = set(range(1, 11))
print(st)

# For loop
for number in range(11):
    print(number)

# Nested For Loop

dct = {'item1': 'value1', 'item2': 'value2',
       'item3': 'value3', 'item4': 'value4', 'alpha': ['a', 'b', 'c', 'd', 'e']}
for key in dct:
    if key == 'alpha':
        for i in dct['alpha']:
            print(i)


# For Else
for n in range(11):
    print(n)
else:
    print('The loop starts at', n)

# Pass
# will be not executed
num = 0
print('Before Loop', num)
for num in range(6):
    pass
print('After Loop', num)
