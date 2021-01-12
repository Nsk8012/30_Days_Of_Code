# 30_Days_Of_Code
# Day 10
# Loops are repetitive tasks untill condition becomes false.
# There are two types while and for loop.
# While loop
count = 0
while count < 5:
    print(count)
    count += 1

print('While with else condition')
# else function can be used in while loop
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(count)

print('Break Condition')
# Break and Continue
# Break will break the loop
n = 0
while n < 5:
    print(n)
    n += 1
    if n == 3:
        break

print('Countinue Condition')
# continue will skip that part
n = 0
while n < 5:
    if n == 3:
        continue
    print(n)
    n += 1
