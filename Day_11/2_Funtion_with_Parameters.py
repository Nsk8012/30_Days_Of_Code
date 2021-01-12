# Function with parameters
# Syntax
# Declaring a function
# def function_name(parameter):
#    code line 1
#    code line 2
# calling a function
# function_name(parameter)
# ------------------------------------------------------------------------------------------
def greeting(name):
    mgs = 'Hello ' + name
    return mgs


print(greeting('Nsk'))
# ------------------------------------------------------------------------------------------


def square(num):
    return num*num


print('Square:', square(4))
# ------------------------------------------------------------------------------------------


def area_of_circle(r):
    pi = 3.14
    area = pi * r ** 2
    return area


print('Area Of Circle', area_of_circle(3))
# --------------------------------------------------------------------------------------------


def sum(num1, num2):
    sum = num1 + num2
    return sum


print('sum of two numbers:', sum(5, 6))
# -----------------------------------------------------------------------------------------------------

# Function passsing aarguments with key and value


def calculate_age(born_year, current_year):
    age = current_year - born_year
    return age


print('Age is', calculate_age(born_year=1999, current_year=2021))
# ---------------------------------------------------------------------------------------------------


def is_even(n):
    if n % 2 == 0:
        print('Even')
        return True
    return False


print('Check number is Even', is_even(8))
print('Check number is Even', is_even(5))

# ------------------------------------------------------------------------------------------------


def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(sum_all_nums(1, 2, 3, 4, 5))
# ---------------------------------------------------------------------------------------------------
# Function Default and Arbitrary Number of parameters in function


def generate_grp(team_name, *args):
    print(team_name)
    for i in args:
        print(i)


generate_grp('Team-1', 'a', 'b', 'c')
