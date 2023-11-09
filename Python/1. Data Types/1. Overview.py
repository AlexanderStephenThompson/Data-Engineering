#!/usr/bin/env python3
# https://docs.python.org/3/library/datatypes.html

# Getting started with good habits...
# The shebang line in any script determines the script's ability to be executed like a standalone executable without typing python beforehand in the terminal 
# or when double clicking it in a file manager (when configured properly). It isn't necessary but generally put there so when someone sees the file opened
# in an editor, they immediately know what they're looking at. 


"""
*-----------------------*
|                       |
|  ~~~~ Variables ~~~~  |
|                       |
*-----------------------*
Python variables are weakly typed
A variable is a container for a value or object of which we can access, use, and manipulate later.

Explain static vs dynamic types
    Static - Variables stay consistent during their life cycle
    Dynamic - Variables can change data types during their life cycle during run time. 
Weakly vs strongly type
    Weak - Allow automatic conversion from one data type to another.
    Strong - Require manual conversion from one data type to another.
Mutability
    Mutable: Can be changed after it's created.
    Immutable: Can not be changed after it's created -- But could possibly be reassigned.

*----------------*
   - Syntax -
*----------------*
Variable_Name = Associated data value
"""


# *------------------------*
#    ---- Common Use ----
# *------------------------*
# Variables simply assign a meaning/information to whatever you assign it to.

First_name = "Alexander"
Last_name = "Thompson"

Greeting = f'Hello, {First_name} {Last_name}. Welcome!'
print(Greeting)

"""
*----------------------------------*
   ---- Assignment Operators ----
*----------------------------------*
Addition:       x + 2   same as x+=2
Subtraction:    x - 2   same as x-=2
Multiplication: x * 2   same as x*=2
Division:       x / 2   same as x/=2
Floor Division: x // 2  same as x//=2
Exponent:       x ** 2  same as **=2
Modulus:        x % 2   same as x%=2
"""

# *--------------------------*
#    ------ Strings ------
# *--------------------------*
Name = "Felix Roswell" # Name[] = ('F','e','l','i','x',' ','R','o','s','w','e','l','l',) (This is how strings are literally strung together.)


# *--------------------------*
#    ------ Numbers ------
# *--------------------------*
Some_Number = 357 # Can be whole or decimal numbers


# *--------------------------*
#    ------ Boolean ------
# *--------------------------*
True_Statement = True
False_Statement = False


""" 
Converting (Type Casting)


int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), 
or a string literal (providing the string represents a whole number)

float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals


#Int
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Floats
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# Strings
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0

# Type Checking

# Strings
some_string.isupper()
some_string.islower()

# Numbers
some_number.isDigit() # 34 and "34" will return true. However, it will return false for negative numbers
some_number.isFloat() # 3.4 and "3.4" will return true. However, it will return false for negative numbers
some_number.isInt() # 3 and "3" will return true. However, it will return false for negative numbers

"""
