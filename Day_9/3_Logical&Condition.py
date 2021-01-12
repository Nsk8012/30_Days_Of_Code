# Logical condition - and & or
# and
n = 5
if n > 0 and n % 2 == 0:
    print('Even Positive')
elif n > 0 and n % 2 == 1:
    print('Odd Positive')
elif n == 0:
    print('Zero')
else:
    print('Negative NUmber')

# or
n = 0
if n > 0 or n == 0:
    print('Not Negative Number')
else:
    print('Negative Number')
