"""
# *------------------------*
# |                        |
# |   ~~~~ Functions ~~~~  |
# |                        |
# *------------------------*
Think of functions as verbs.

Functions
Think of functions as verbs, explaining a set of instructions to perform. Functions are a block of code that is ran only when it is called.
The usefulness comes from allowing to reuse code as many times as we want and allow modifications in just one place. 
All functions should return a value; which is the result of the function that ran -- which is what we want! 
This allows us to use that returned value anywhere we want as as many times as we wish until that function is ran again and possibly gain a new value.

Parameters
Parameters are a variable found in () of a function that allow you customize what the function can do and even how do it. 
These are specified within the parenthesis of the function and you can have as many as you want as long
as you separate them with a comma.

Methods
Also known as object modifiers, methods are functions that act upon a specified object to perform some sort of operation. 
They tend to alter, or modify the specified object, in a way so you can manipulate an object of that data type.
This way you can get further uses out of the object you're interacting with. When Python calls a method, 
it binds the first parameter of that call to the appropriate object reference. (For most methods, that's conventionally called self).

You can right click a function and peek a definition or declaration to conveniently look at a function's 
structure without having to move to a new file or whenever it was declared. 

Documenting
https://realpython.com/documenting-python-code/


Debugging
This is also a great time to start showing off debugging in an IDE. Sure, it can be IDE specific, but the process is conceptually the same.
Starting to show debugging practices now will allow to show how more intricate processes are completed later on. This will teach a valuable skill
while also building some intuition of how and why something may or may not work. 

Algorithms
An algorithm is the generalization of how a process is performed, but functions are the actual implementation to make it happen.
    1. Know the goal
    2. Understand the problem you're trying to solve or the thing you're trying to recreate
    3. Know what can and can't happen. As in, defining parameters to prevent rule breaking and impossibilities. 
    4. Design the set up and then the execution of logic. 

A final draft of the algorithm can be written out in comments. Then you just write out the code to accomplish the task. 


You can also bring in functions from other files by imports such as modules, packages, and libraries.
    Module - Individual file
    Package - Folder containing multiple modules
    Library - A collection of packages 

# Importing Modules
import my_module                 # Method 1: Entire import from the same folder
import my_module as MM           # Method 2: Same thing, but with an alias
from my_module import find_index # Method 3: Importing just a function. Can use commas to list out multiple imports.


courses = ["History", "Physics", "Chemistry", "Biology"]

# Method 1 usage
first_index = my_module.find_index(courses, "Physics")
print(first_index)

# Method 2 usage
second_index = MM.find_index(courses, "Biology")
print(second_index)

# Method 3 usage
third_index = find_index(courses, "History")
print(third_index)

# *------------------------*

*--------------------*
   ---- Syntax ----
*--------------------*


def Function_Name(parameter: datatype)
    "Doc string""
    instructions

Calling
Object_Name.method()

"""


# *------------------------*
#    ---- Common Use ----
# *------------------------*

# Importing
# import importedFileName as shortName

def Welcome_Message():
    """This will greet the user."""
    print("Hello and welcome, great to see you.\n")

Welcome_Message()

def Personal_Greeting(Name: str):
    print(f"Hello {Name}!")

Personal_Greeting("Alex")

def Custom_Greeting():
    nameInput = input("What is your name?")
    return f"Hello {nameInput}!"

print(Custom_Greeting())

def Email_Generator(Last_name):
    print(Last_name + "@gmail.com")

Email_Generator("Rufus")
Email_Generator("Alex")


def Sum(First_Number, Second_Number): 
    print(First_Number + Second_Number)

Sum(4, 6)  # 4 and 6 are the arguments for first and second number respectively.


# House Price Example
def get_expected_cost(beds, baths, has_basement):

    bedroom_contribution = beds * 30000
    baths_contribution = baths * 10000
    basement_contribution = 40000 if has_basement == True else 0
    base = 80000

    total_value = bedroom_contribution + \
        baths_contribution + basement_contribution + base
    return total_value

"""
*-------------------*
   ---- Scope ----
*-------------------*
Determines where our variables can be accessed from within the program and what values they will be under different contexts.
In short: Accessability of a variable widens when you outdent, and vice vera when you indent. You can reach out of different scopes, but not in deeper. 
Checks variables this order: Local, Enclosing, Global, Built-in

The higher level of detail, the more scoped and limited the accessability is. 
Local and enclosing look relative to their current position. 

Local - Variables declared within a function and is relative to its own current scope and acts as the highest level of detail. 
This is the parameters and variables of the current function and will take the highest priority if there was a variable with the same name in a different range of the scope.

Enclosing - Deals with nested functions. Essentially looking for variables from the next level of scope. Looks at adjacent levels of detail until it reaches global scope (No indentation).
Global - Root level, as in no indentation. Lowest level of detail. This can be accessed anywhere by anyone.

Think of scope as a tree structure.
Items at the root are accessible to the branches and leaves, but items declared in a branch can't be seen in other branches.

Enclosing refers to nested functions.

*------------------------*
   - Template Example -
*------------------------*
X = "Global X"

def outer():
    X = "Outer X" # Local to the outer function, enclosing to the inner function.

    def inner():
        X = "Inner X"
        print(X) #Local - "Inner X" Would be "Outer X" if the local variable wasn't created.

    inner()
    print(X) #Enclosing - "Outer X"

outer()
print(X) # Global - "Global X"

------------------------------
X = "Level 1"

def outer():
    X = "Level 2"

    def inner():
        X = "Level 3"
        print(X) #Level 3

    inner()
    print(X) # Level 2

outer()
print(X) # Level 1
"""

# *--------------------*
#    - Tree Example -
# *--------------------*
Root = "A global variable"


def Tree():
    First_Function_Variable = "I enclose nested functions"
    Second_Function_Variable = "I can be used locally relative to this function too -- of course"
    Third_Function_Variable = "However, I can't be reached from the outside"

    def Branch_1():
        Local_Variable = "Local branch variable"
        print(Local_Variable)

    def Branch_2():
        print(First_Function_Variable)  # Gets the enclosing variable since there wasn't a local one.

    def Branch_3():
        """print(Local_Variable) #Unable to reach other same level branch function variables."""
        """print(Root) #Can, however, always reach global variables"""
        pass

    Branch_1()
    Branch_2()
    Branch_3()
    print(Second_Function_Variable)
    print(Root)


Tree()
"""print(Third_Function_Variable) #Can't reach into function variables"""

# *---------------------------------------------------------*
#    ------ Positional and Named/Keyword Parameters ------
# *---------------------------------------------------------*
"""
A positional argument is a name that is not followed by an equal sign (=) and default value.
A keyword argument is followed by an equal sign and an expression that gives its default value.

def Test_Function (a, b, c = 1):          # a/b required, c optional.
    return a * b + c

print Test_Function (1, 2)                # returns 3, positional and default.
print Test_Function (1, 2, 3)             # returns 5, positional.
print Test_Function (c = 5, b = 2, a = 2) # returns 9, named.
print Test_Function (b = 2, a = 2)        # returns 5, named and default.
print Test_Function (5, c = 2, b = 1)     # returns 7, positional and named.
print Test_Function (8, b = 0)            # returns 1, positional, named and default.
"""
def Greeting_Message(Name="John"):
    print(Name + ", it's nice to meet you")

Greeting_Message()  # Uses John as a default if nothing is added to the parameters
Greeting_Message("Alex")

def documentFunction(): # <-- Hover over the function name
    """ Some summary info about the function. 

        Extended description of the function. This way you can give a more detailed summary of what's going on.

        # Heading 1
        ## Heading 2
        ### Heading 3

        - Note 1
        - Note 2
        - Note 3
        
        Parameters
        ----------
        - `Argument 1`: data type - 
            Description of the `argument`

        - `Argument 2`: data type -
            Description of the `argument`

        - `Argument 3`: data type -
            Description of the `argument`


        Examples
        --------
        You can provide some `code` examples to help the reader such as:
        >>> Custom_Greeting("Rufus")
    """
    pass # Just kidding, this function does nothing.

# Return statements
"""Return statements
Return statements offer much greater capabilities. Understanding a return statement's data type 
will allow you to chain together functionality, essentially performing another function upon the 
result of other function.
"""
def Simple_Greeting():
    return "Hello!"

print(Simple_Greeting().upper) # Takes the result of the function then perform another function on it.

# Cooking Example
def mix_and_cook():
    print("Mixing the ingredients")
    print("Grease the cooking surface")
    print("Pouring the mixture")
    print("Cooking first side")
    print("Flip it")
    print("Cooking the other side")

def makeOmelette(ingredient):
    mix_and_cook()
    omelette = f"A {ingredient} omelet was made"
    return omelette

def makePancake(ingredient):
    mix_and_cook()
    pancake = f"A {ingredient} pancake was made"
    return pancake

"""
*------------------------------*
   ---- *Args & **kwargs ----
*------------------------------*
Both args and kwargs lets you pass one or many parameters to a function. *args returns a list and **kwargs returns a dictionary.
Then you can use those data structures however you'd normally use them. 

When ordering arguments within a function or function call, arguments need to occur in a particular order:
    Formal positional arguments
    *args
    **kwargs
"""

# *----------------*
#    - Args -
# *----------------*

def fancy_omelette(*ingredients):
    mix_and_cook()
    omelette = f"A fancy omelette with {len(ingredients)}"
    return omelette


def Undetermined_Sum(*args):
    result = 0  # Starting value

    for Number in args:
        result += Number

    return result

print(Undetermined_Sum(1, 2, 3))
print(Undetermined_Sum(10, 14, 29))


def Print_Scores(Student, *Scores):
    print(f"Student Name: {Student}")
    for Score in Scores:
        print(Score)

Print_Scores("Jonathan", 100, 95, 88, 92, 99)

def AddNumbers(*Numbers):
    Total = 0
    for Number in Numbers:
        Total += Number
    return Total

print(AddNumbers(4, 6))
print(AddNumbers(4, 6, 12, 43))


# *----------------*
#    - Kwargs -
# *----------------*
def Concatenate(**kwargs):
    result = ""

    for arg in kwargs.values():
        result += arg
    return result

print(Concatenate(a="Python ", b="Is ", c="Great", d="!"))


def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)


def Print_Values(**kwargs):
    for key, value in kwargs.items():
        print(f"The value of {key} is {value}")

Print_Values(
    User_1 = "Alex",
    User_2 = "Gray",
    User_3 = "Harper",
    User_4 = "Phoenix",
    User_5 = "Leon",
    User_6 = "Val")


# *---------------------*
#    ---- Logging ----
# *---------------------*
# Not exactly providing functionality, but rather insights on the functionality of our project.


# *--------------------*
#    ---- Events ----
# *--------------------*
"""
An event is a function to be called when a condition is met.
	Signal Event:  A named object thrown by one object and caught by another object.
	Call Event: A synchronous event representing dispatch of an operation.
	Time Event: An event representing passage of time.
	Change Event: An event representing change in state.

"""

"""
*------------------------*
   ---- Exceptions ----
*------------------------*
https://www.tutorialspoint.com/python/standard_exceptions.htm
Checking if an action of function can be completed based on some conditions or possible limitations.

try: Code you'll try to complete
except: Ways you'll handle errors
else: What happens when there aren't errors (The intended functionality.)
finally: Is ran regardless of a pass or fail. 

Used in Easier to ask for forgiveness than permission. We'll try to do something and if it doesn't work, we'll handle it. 

Exception Types:
•	BaseException
•	Exception
•	SystemExit
•	KeyboardInterrupt
•	abstract exceptions
•	ArithmeticError
•	LookupError
•	IndexError
•	KeyError
•	TypeError
•	ValueError

"""

def divide(x, y):
    try:
        print(f'{x}/{y} is {x / y}')
    except ZeroDivisionError as error:
        print(f"There was an error: {error}")
    except:
        print("Some generic error")
    else:
        print("divide() function worked fine.")
    finally:
        print("Finished")


divide(10, 2)  # Success
divide(10, 0)  # Failure

# ---
print("What is your favorite number?")
Favorite_Number = input()

try:
    if int(Favorite_Number) !=7:
        print("That's a good number to like.")
    else:
        print("Awesome, lucky number seven!")
except ValueError:
    print("You were suppose to enter a number")

attempts = 0
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        attempts += 1
        print(
            f"Oops!  That was no valid number.  Try again... {attempts + 1} is the charm, right? ")
        if attempts == 3:
            print("You clearly can't follow directions.")
            break


isComplete = False
while isComplete == False:

    userInput = input("Say Zebra\n")

    if userInput != "Zebra":
        print("You didn't say zebra, try again")
    else:
        print("Wonderful!")
        isComplete = True


# Membership - Great for data validation
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



# *--------------------------*
#    ---- Unit Testing ----
# *--------------------------*

"""
Corey: https://www.youtube.com/watch?v=6tNS--WetLI&t
Search for assertions: https://docs.python.org/3/library/unittest.html

Process
1. Create a test file with test_fileName.py of the file you're testing. 
2. Import the unittest module and the file we want to test. 
3. Create test cases. 
4. Create name = main to allow for easier testing with python test_fileName.py
5. Run the test cases.

"""
def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

  
import unittest
class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertEqual(divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()


# *----------------------*
# ---- Importing - ---
# *----------------------*
# Finally, to wrap up the basics of functions, we want to learn to import them so we can use them elsewhere in our projects for clean segmentation.
# You'll use some sort of package manager, like pip or conda, to work with external modules like to install, update, or remove modules. 

# Referenced file (In same folder): importedFileName.py
myVariable = "This is my variable"

def myFunction():
    print("Hello!")



#Main file: main.py
import importedFileName as shortName # Import whole file
from importedFileName import myVariable, myFunction # Import individual variables, functions, and other things. 

if __name__ == "__main__":
    shortName.myFunction() #Have to specify where and what function
    myFunction() #Just have to specify the function, like any regular function.


"""
*------------------------*
   ---- Decorators ----
*------------------------*
Essentially: Functions making new extending and/or altering the functionality of existing functions.

A decorator is a enhancement function that takes an original function as an argument then adds and enhances some sort
of functionality to that original function before returning a new and improved function. All of which is done without altering
the source code of the original function you passed in. So it's like the original function inherits the
decorator's functionality without anything being added to the original function's code.


If you understand scope and how to use parameters in functions as well as appreciate the use of return statements from
functions, you'll be able perform decorators.


To appreciate and understand decorators in Python you need to understand the usefulness of the return statement for functions. Because that's how we can put functions in as arguments into another function.
The decorator allows us to easy implement the extended capabilities in one location while keeping the original function intact.

Syntax
~~~
def Decorator_Function(Original_Function): #Name of the decorator

    def Wrapper_Function(): #What the decorator will do
        print("Some new functionality. Whatever is in the wrapper function is the new functionality added.") 
        return Original_Function() #Original functionality

    return Wrapper_Function #Combined result


@Decorator_Function # Calling the decorator to apply additional functionality onto the function below.
def Original_Function(): 
    return "Display function ran."
"""

# *---------------*
#    - Example -
# *---------------*


def Capitalize(Original_Function):
    def Uppercase():
        Result = Original_Function()
        return Result.upper()  # The upper method is the new functionality.

    return Uppercase

# Greeting = Capitalize(Greeting)


@Capitalize
def Greeting():
    return "Hello!"


print(Greeting())


# *-----------------------*
#    ---- Recursion ----
# *-----------------------*
""" A recursive function is a function that calls itself (The recursive case) until it meets some condition to stop (The base case)."""

# Factorials


def FindFactorial(Number):
    if Number == 1:  # Base case
        return Number
    else:  # Recursive case
        return Number*FindFactorial(Number - 1)


# *-----------------------*
#    ---- Callbacks ----
# *-----------------------*
"""A call back is a function that calls another function sometime during its execution or by passing a function as an argument to another function.
This can be great if you want to separate steps into their own function so that a process can be modularized. This is why breaking down functions into 
very small sets of instructions is very beneficial since you get much more control of what happens, how it does, and when it's performed.
"""

# Nested function execution


def MakeCoffee():
    print("Making coffee!")


def MakeToast():
    print("Making toast!")


def MakeEggs():
    print("Making eggs!")


def MakeStandardBreakfast():
    MakeCoffee()
    MakeToast()
    MakeEggs()

# Nested function arguments


def AddSomething(FirstNumber, SecondNumber):
    return FirstNumber + SecondNumber


def CombineTwoThings(ThingOne, ThingTwo):
    return ThingOne + ThingTwo


CombineTwoThings(AddSomething(2, 4), AddSomething(5, 7))


# *---------------------*
#    ---- Lambdas ----
# *---------------------*
"""
Lambdas are an alternate way of creation a function, but for short term use.
If you know you're only going to use that functionality once, it can be worth 
it to create a lambda instead;  however, it's still perfectly acceptable to still
use a normal function. Lambdas may or may not provide cleaner alternatives. 

Syntax
lambda arguments : expression
"""


def CelsiusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahrenheitToCelsius(temp):
    return (temp-32) * 5/9


CelsiusTemperatures = [0, 12, 34, 100]
FahrenheitTemperatures = [32, 65, 100, 212]

# Use regular functions to convert temps
print(list(map(FahrenheitToCelsius, FahrenheitTemperatures)))
print(list(map(CelsiusToFahrenheit, CelsiusTemperatures)))

# Use lambdas to accomplish the same thing
print(list(map(lambda Temperature: (Temperature-32) * 5/9, FahrenheitTemperatures)))
print(list(map(lambda Temperature: (Temperature * 9/5) + 32, CelsiusTemperatures)))


# *------------------------*
#    ---- Delegation ----
# *------------------------*


# *----------------------------*
#    ---- Multithreading ----
# *----------------------------*
