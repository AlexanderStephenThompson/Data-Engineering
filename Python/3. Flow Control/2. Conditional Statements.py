"""
# *-------------------------------------*
# |                                     |
# |   ~~~~ Conditional Statements ~~~~  |
# |                                     |
# *-------------------------------------*
UML
UML isn't a separate topic but rather an integrated one as you learn programming. When you start working with flow control
is about the ideal time to start learning to use UML. As a project grows, documentation of how it works will help you and other out.
The first being flow charts for conditional statements. Then heavy use starts when developing classes, design patterns, and project wide parameters.

# *--------------------*
#    ---- Syntax ----
# *--------------------*

if (condition1):
    //  block of code to be executed if condition1 is true
else if (condition2):
    //  block of code to be executed if the condition1 is false and condition2 is true
else:
    //  block of code to be executed if both condition1 and condition2 are false

To ensure some code runs no matter what errors occur, you can use a finally statement.
The finally statement is placed at the bottom of a try/except statement. Code within a finally statement always runs
after execution of the code in the try, and possibly in the except, blocks.
"""

from typing import Any


Number_1 = ()
Number_2 = ()

print("Enter your first number")
Number_1 = input()
print("Enter your next number")
Number_2 = input()

if Number_1 == Number_2:
    print("These two numbers are the same")
elif Number_1 < Number_2:
    print(f"{Number_1} is more than {Number_2}")
else:
    print(f"{Number_2} is less than {Number_1}")


# Ternary Conditionals - Useful for simple, consolidated expressions

Condition = False
X = 1 if Condition else 0
print(X)


# Condition lists - Predefine lists

Subs = 2400
Likes = 200
Comments = 56

Conditions = [
    Subs > 150,
    Likes > 200,
    Comments > 10
]

if all(Conditions): # And conditional
    print("Awesome video!")

if Any(Conditions): # Or conditional
    print("Awesome video!")


# Grade provision
def get_grade(score):
    if (score >= 90 and score <= 100):
        grade = "A"
    elif (score >= 80 and score <= 89):
        grade = "B"
    elif (score >= 70 and score <= 79):
        grade = "C"
    elif (score >= 60 and score <= 69):
        grade = "D"
    else:
        grade = "F"

    return grade

# Alternative method
def calculate_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

