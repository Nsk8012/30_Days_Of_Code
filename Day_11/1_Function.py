# 30_Days_Of_Code
# Day 11
# Function is reusable block of code or program statements designed to perform a certain task.
# --------------------------------------------------------------------------------------------
# Syntax:
# Function without parameters
# Declaring a function
# def function_name():
#    code line 1
#    code line 2
# calling a function
# function_name()
# ---------------------------------------------------------------------------------------------
def generate_fullname():
    first_name = input('Enter First Name:')
    last_name = input('Enter Last Name:')
    space = ' '
    print(first_name + space + last_name)


# generate_fullname()
# ------------------------------------------------------------------------------------------------


def find_total():
    num1 = int(input())
    num2 = int(input())
    sum = num1 + num2
    return sum


# print(find_total())
# -----------------------------------------------------------------------------------------------
