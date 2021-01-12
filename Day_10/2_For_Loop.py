# For Loop with List
num = [1, 2, 3, 4, 5]
for n in num:
    print(n)

# For Loop with String
st = 'Nishanth'
for s in st:
    print(s)

# For Loop with Tuple
tpl = (1, 2, 3, 4, 5)
for t in tpl:
    print(t)

dct = {'item1': 'value1', 'item2': 'value2',
       'item3': 'value3', 'item4': 'value4'}
for key in dct:
    print(key)

for key, value in dct.items():
    print("{} - {}".format(key, value))

# For Loop in Set
sets = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
for st in sets:
    print(st)
# Break and Continue
# Break
for n in num:
    print('Before Break', n)
    if n == 3:
        break

# Continue
num = (0, 1, 2, 3, 4, 5)
for n in num:
    print('Before Continue', n)
    if n == 3:
        continue
    print('Next number should be ', n+1) if n != 5 else print('loop ends')
print('Outside the Loop')
