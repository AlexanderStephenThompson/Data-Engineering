"""
*--------------------------*
|                          |
|    ~~~~~ Loops ~~~~~     |
|                          |
*--------------------------*
Loops allow us to repeat a block of code multiple times. When thinking of a repeating/looping pattern, 
determine if it's indefinite or predetermined. It's useful to know that through each loop, you can 
implement logic to specify more fine-grained control over what happens within each loop.

Useful video: https://www.youtube.com/watch?v=wd1JqBWm3lQ

Iterable vs Iterator
    Iterable: [Noun] Something that can be looped/iterated over such as a string, any data structure, generators, files, or special objects like range(). 
    Iterator: [Adjective] An object with a state so that it remembers where it is during iteration as well as know how to get their next value. Essentially, memory of where it is comparing to where it can go next.

Determinate vs Indeterminate
    Determinate (For) loops: Sequentially execute instructions for each item of an iterable object.
    Indeterminate (While) loops: Will do something as long as a condition is true or when a control keyword like break or continue is used.

Control Keywords
    break: Terminates the entire loop process, proceeding with the next statement following the loop block. 
    continue: Terminates the current loop iteration, re-evaluates the condition, then loops if the condition is still true.
    pass: Does nothing at all.


In terms of algorithm optimization, loops are quite slow. So, you should be always on the lookout for builtin 
methods or generators that will accomplish the same thing since they're probably more efficient. 

# Summation
numbers = [10, 20, 33, 40, 50, 60, 70, 80]
total = 0

# With loop
for number in numbers:
    total += number

# Without loop
total = sum(numbers)

# Listing out elements of an array
data = [0, 1, 2, 3, 4 ,5]
print(*data)

"""

# *---------------------------*
#    ------ For Loops ------
# *---------------------------*
"""A for loop is used for iterating over a sequence often good for data structures.
Another way to say it is "For every item within this structure... do something."
The range() is often used with for loops to iterate through something."""



Fruits = ["Apple", "Banana", "Cherry"]
for Each_Item in Fruits:
    print(Each_Item)  # So this code prints out each item in the list.

# Counts starting at 0 to, but not including, 10. Essentially saying do this 10 times.
for Number in range(0, 10):
    print(Number)

# Counts by 2. Keep in mind the counting goes by 1 unless otherwise specified like here.
for Number in range(0, 10, 2):
    print(Number)

Total = 0 
for Number in range(101):
    Total += Number  # 0 + 1 + 2 + 3 +... 99 + 100
print(Total)


# Logic implementation
Numbers = [1, 2, 3, 4, 5]
# Break
for number in Numbers:
    if number == 3:
        print("We found the number three!")
        break  # Terminates the looping process.
    print(number)

# Continue
for number in Numbers:
    if number == 3:
        print("We found the number three!")
        continue
    print(number)

# Check for a trait of each character
text = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'

for char in text:
    if char.isupper():
        print(char, end='')


def has_lucky_number(nums):
    """Remember that return causes a function to exit immediately. We can only return False if we've looked at every element of the 
    list and confirmed that none of them are lucky. Otherwise, we return true as soon as we've found a lucky number."""

    for num in nums:
        if num % 7 == 0:
            return True # Return true if there was a lucky number found. No need to keep looking.
    
    return False # We've exhausted the list without finding a lucky number.


# *-----------------------------*
#    ------ Comprehensions ------
# *-----------------------------*
"""
Comprehensions in Python provide us with a short and concise way to construct new data structures 
based on pre-existing sequences following a for loop structure.

Types
    - List Comprehensions        list_comp = [x*x for x in range(10)}
    - Dictionary Comprehensions  dict_comp = {i: i*i for i in range(10)]
    - Set Comprehensions         set_comp = {i % 3 for i in range(10)}
    - Generator Comprehensions   gen_comp = ((2*x)+5 for x in range(10))
"""

#Lists
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
short_planets = [planet for planet in planets if len(planet) < 6] # Going to make new planet for each planet in planets if...
loud_short_planets = [f"{planet.upper()}!" for planet in planets if len(planet) < 6]


def greater_than_loop(List, threshold):

    greater_than = []

    for number in List:
        greater_than.append(number > threshold)

    return greater_than


def greater_than_comprehension(List, threshold):
    return [number > threshold for number in List]


# *-----------------------------*
#    ------ While loops ------
# *-----------------------------*
"""
    With the while loop we can execute a set of statements while a condition is true.
    You're essentially telling the program "While a condition is true, do this". As long
    as you adjust the condition or use a break or continue keyword, you'll avoid infinite loops.

    while some_condition_is_true:
        Do something
    else: # Optional
        Do something else

    Preventing infinite loops
        Can just be "while true" and terminating the loop with either "break" or "continue" keywords.
        Can be with a pre-existing condition and alter the condition during at some point of the loop.

 """

Number = 1  # This is the starting point
while Number < 10:  # Saying "While the number is less than, but not including 10..."
    print(Number)  # Print the number
    Number += 1  # Then add one to the number variable
# This loops until the statement is false (When it reaches 10).
# With the break keyword we can stop the loop even if the while condition is true

Number = 1 # Initial state
while Number < 10:
    print(Number)
    if Number == 5:
        print("Number found!")
        break
        print("Done!") # Will not be printed since anything after the break keyword is not executed
    Number += 1

Count = 0
while (Count < 10):
    # This is essentially telling python to print "Hey" 10 times.
    print("Hey")
    Count = Count + 1

# While else - With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# Password Example
Password = "Secret"
Input = ""
Authorized = False
Attempts = 0
Attempt_Limit = 3

while Input != Password:
    Attempts += 1
    if Attempts > Attempt_Limit:
        print("You're in trouble!")
        break
    Input = input(f"Attempt {Attempts}/{Attempt_Limit}: What's the password?")
else:
    Authorized = True
    print("Welcome")


# Menu Example
print("Welcome to my menu")

while True:
    choice = input("Do you want to play? (yes, no, or q to quit): ").lower()

    if choice == "q": #Guard clause
        print("Darn...")
        break

    if choice == "yes":
        print("Yay!")
        break
    elif choice == "no":
        print("Fine then...")
        break
    else:
        print("Please enter yes or no")
        continue # Kind of like a "try again", restarting the loop until you provide valid input



# RPG Bank example -- plus error/exception handling

balance = 659.75

# Entering a state of input collection and waiting for only the right input type.
while True:
    try:
        deposit = float(input('Deposit: $'))
        break
    except ValueError:
        print("You can only enter numeric values")

balance += deposit

print(f'Balance is: ${balance}')



# *------------------------------------------*
#    ------ Transformation Functions ------
# *------------------------------------------*

# map(): iterates through all items in the given iterable and executes the function we passed as an argument on each of them.

# filter() - Creates a new list that contains only elements that satisfy a certain specified condition

# reduce(): Essentially aggregating by returning a single value based on what to aggregate on. IE: reducing to one value.


# *-----------------------------*
#    ------ Generators ------
# *-----------------------------*
"""
Allow us to pause functions in the middle of execution to be resumed later. 
Generators allow for efficient looping by iterating one item at a time rather than creating a full list of memory. 

Generators are used for making easy to read iterators. They look a lot like a function; however, 
instead of returning a result they instead yield a single value. That value is remembered until it is called by the generator.

Iterators/generators just remember one value at a time rather than a whole collection. It remembers 
its own value, the most recent one, and is updated accordingly per the generator's functionality. This saves a ton of memory and time.

Really you call each item in a list one at a time of your choosing. The generator remembers which instance you're on
and will give you the correct next item if there is one left.
"""
# Traditional Method


def Traditional_Square_Numbers(Numbers):
    Result = []
    for Number in Numbers:
        Result.append(Number * Number)
    return Result


Traditional_Number_List = Traditional_Square_Numbers([1, 2, 3, 4, 5])
print(Traditional_Number_List)


# Generator Method
def Generator_Square_Numbers(Numbers):
    for Number in Numbers:
        yield (Number * Number)  # This is what makes a generator


Generator_Number_List = Generator_Square_Numbers([1, 2, 3, 4, 5])


def printNextGeneratorNumber():
    print(next(Generator_Number_List))


printNextGeneratorNumber()
printNextGeneratorNumber()
printNextGeneratorNumber()
printNextGeneratorNumber()
printNextGeneratorNumber()


# Extra Generator Example

# Without Generator
events = [("learn", 30), ("learn", 15), ("relaxed", 20)]

minutes_studied = 0
for event in events:
   if event[0] == "learn":
      minutes_studied += event[1]
print(minutes_studied)

# With Generator
study_times = (event[1] for event in events if event[0] == "learn")
minutes_studied = sum(study_times)
print(minutes_studied)




# *-----------------------------*
#    ------ Recursion ------
# *-----------------------------*
"""
Recursion: A function that calls itself to perform an action, adjusting some value upon each
iteration to avoid an infinite loop and eventually satisfy a base case for the function to 
finally unwind the build up call stack and determine the solution. 

Acts like an internal loop, a function calling itself to perform an action, but defining a base case 
and adjusting something with each recursive call to prevent an infinite loop – just like any other loop
technique. Once things are solved, the function then catches up on the call stack to unwind and finally
give the final result since each recursive call was waiting on the result of the call ahead of it. You
can probably utilize a recursive leap of faith if the pattern is reliably predictable enough. 

Process
    1. What's the simplest possible input? This often acts as the base case of the recursive function. 
    2. Since the sub problems are dependent on each other, look for relationships. 
    3. Generalize the pattern so we can represent it in code.

"""
def factorial(number):

    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(5))

# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)


# --- Unwinding ---
# factorial(2) = 2 * 1 --> 2
# factorial(3) = 3 * 2 --> 6
# factorial(4) = 4 * 6 --> 24
# factorial(5) = 5 * 24 --> 120
