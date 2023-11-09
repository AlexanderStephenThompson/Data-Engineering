# https://docs.python.org/3/library/numeric.html

from math import *
"""
# *--------------------------*
# |                          |
# |    ~~~~ Numeric ~~~~     |
# |                          |
# *--------------------------*
If you want more math functions you can import more to a file by typing: from math import *

Arithmetic Operators
    Addition:       3 + 2
    Subtraction:    3 - 2
    Multiplication: 3 * 2
    Division:       3 / 2
    Floor Division: 3 // 2
    Exponent:       3 ** 2
    Modulus:        3 % 2
    
Arithmetic Rules Of Operation
    P Parentheses ()
    E Exponents **
    M Multiplication *
    D Division /
    A Addition +
    S Subtraction -

Increment/Decrement
    Number = 0  # Initializing
    
    Number += 1  # Adds 1
    Number -= 1  # Subtracts 1
    
"""

# *---------------------------*
#    ------ Common Use ------
# *---------------------------*

Whole_Number = 357
Decimal = 3.14

# Arithmetic Operations
print(3 + 2)    # Addition
print(3 - 2)    # Subtraction
print(3 * 2)    # Multiplication
print(3 / 2)    # Division
print(3 // 2)   # Floor division is dividing one number by another and rounding down to the closest smallest whole integer.
print(3 ** 2)   # Exponent / Finding the power of
print(3 % 2)    # Modulus does division and returns the remainder. So 2 can go into 3 only once and have a remainder of 1. The remainder of 1 is the answer printed.

Case_Size = 6
Bottles = 17

Remaining_Bottles = Bottles % Case_Size

# Rules of Operation
print(3 * (2 + 1))      # Example 1, adding 2 and one first before multiplying by 3 to get a answer of 9
print(7 % (5 // 2))     # Two goes into five 2.5 times. Floor division rounds it down to two. Then 7 divided by 2 goes into 7 three times with a leftover of one. One is the answer printed out.
print(9 / 3)
# Note any number which is divided is turned into a float, meaning it has a decimal, like the 3.0 above.")

# Comparison operators
print(3 == 2)   # False. Three is not two
print(3 != 2)   # True. Three is not two
print(3 > 2)    # True. Three is greater than two
print(3 < 2)    # False. Three is not less than two
print(3 >= 2)   # True. Three is greater than or equal to two
print(3 <= 2)   # False. Three is not less than or equal to two


# *---------------*
#    - Floats -
# *---------------*
# A float is also produced by running an operation on two floats, or on a float and an integer.

print(8 / 2)
print(6 * 7.0)
print(4 + 1.65)

# *---------------*
#    - Decimal -
# *---------------*
from decimal import *
# This allows for greater accuracy in numeric data types, especially useful with currency.

Default_Result = 0.1 + 0.1 + 0.1 - 0.3
print(Default_Result)


Dime = Decimal('0.10')
Cost = Decimal('0.30')

Accurate_Result = (Dime * 3) - Cost
print(Accurate_Result)

# *------------------*
#    - Formatting -
# *------------------*

# Scientific Notation
print(format(5482.52291, "10.2E"))  # 5.48E+03

# Thousands Seperator
print(format(73817.71, "5,.2f")) # 73,817.71

# Percentage
DecimalNumber = 1/3
DecimalCount = 2
Percentage = f"{DecimalNumber:.{DecimalCount}f}%" # Two diits after the decimal: 0.33%

print(Percentage)


# https://www.w3schools.com/python/module_math.asp

# *-----------------------------------*
#    - Different Numeric Systems -
# *-----------------------------------*
# Summary
# Binary uses bin() and ‘0b’.
# Hexadecimal uses hex() and ‘0x’.
# Octal uses oct() and ‘0o’.

# Binary
binary_number = "ob100"

# Octal
octal_number = "0o10"

# Decimal

# Hex
hex_number = "0x10"


#Conversion
print(hex(255))  # decimal
print(hex(0b111))  # binary
print(hex(0o77))  # octal
print(hex(0XFF))  # hexadecimal
