# Short Hand is used to code in single line.
n = 4
print('Positive Number') if n > 0 else print('Negative Number')

n = 0
print('Positive Number') if n > 0 else print('Negative Number')

# Nested Condition
n = 6
if n > 0:
    if n % 2 == 0:
        print('Even Positive Number')
    else:
        print('Odd Positive Number')
elif n == 0:
    print('It\'s Zero')
else:
    print('It\'s Negative Number')
