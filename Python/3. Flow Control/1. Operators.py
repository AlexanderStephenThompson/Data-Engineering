"""
https://www.w3schools.com/python/python_operators.asp

   *--------------------------------------*
      ------ Comparison Operators ------
   *--------------------------------------*
   ===   Exactly
   ==	   equal to
   !=	   not equal
   >	   greater than
   <	   less than
   >=	   greater than or equal to
   <=	   less than or equal to
   is    Checks object identity. Since objects can be similar, but may not be the same, we want to check for that.
"""

"""

   *-----------------------------------*
      ------ Logical Operators ------
   *-----------------------------------*
   Used to combine conditional statements

   and
   or
   not
"""

isRaining = False
isSunny = True

# AND
# true and true   --> true
# false and true  --> false
# true and false  --> false
# false and false --> false

if isRaining and isSunny:
   print("We might see a rainbow")

# OR
# true and true   --> true
# false and true  --> true
# true and false  --> true
# false and false --> false

if isRaining or isSunny:
   print("It might be rainy or it might be sunny")

# NOT
# true   --> false
# false  --> true

if not isRaining:
   print("It must be raining")

ages = [12, 18, 39, 87, 7, 2]
for age in ages:
   isAdult = age > 17
   if not isAdult:
      print(f"Being {str(age)} does not make you an adult.")


"""
   *--------------------------------------*
      ------ Membership Operators ------
   *--------------------------------------*
   Used to combine conditional statements

   in
   not in
"""
# Membership
choices = ["Zebra", "Roo", "Bun"]

isComplete = False
while isComplete == False:

   print("Choose between a Zebra, roo, or bun")
   userInput = input("I choose: \n")

   if userInput not in choices:
      print("That wasn't an option, try again.")
   else:
      print("Wonderful!")
      isComplete = True
