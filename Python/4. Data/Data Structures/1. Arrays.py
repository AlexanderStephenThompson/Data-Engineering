# Lists/ Arrays


"""
Summary
~~~~~~~~~~
Arrays, also know as lists in Python, are a collection of items which are ordered and changeable.
The values can be strings, integers, other lists and many other possibilities. Allows duplicate members.
A lot of the functionality in arrays can also be found in other data structures too. 

Creation Syntax
List_Name = [Item_1, Item_2, Item_3]

Methods

insert()	Adds an element at the specified position
append()	Adds an element at the end of the list
extend()	Add the elements of a list, to the end of the current list
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value

index()	    Returns the index of the first element with the specified value
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Return the number of times whatever value is passed appears in the specified list
len()       Counts the total number of items in a list

sort()	    Sorts the list ascending. sort(reverse = True) will reverse in decending. 
reverse()	Reverses the order of the list

min()
max()
sum()

*---------------------------------------*
   ------ Iterables & Iterators ------
*---------------------------------------*

Definitions:
Iterable - (Adjective) Something that can be looped over, like lists with for loops.
Iterator - (Verb)  Object with a state so it remembers which instance of iteration it is in a given list. Can only make forward increments.
"""


# *--------------------*
#    ---- Create ----
# *--------------------*


# *-------------------*
#    - 1-Dimension -
# *-------------------*
Empty_List = []  # Sometimes you need to create an empty list and populate it later during the program

# user enters the number of elements to put in list
List_Count = int(input('How many numbers? '))

# iterating till count to append all input elements in list
for Item in range(List_Count):
    number = int(input('Enter number: '))
    Empty_List.append(number)  # Adds an item to the list

Grocery_list = ["Thyme", "Chicken", "Garlic", "Russets", "Asparagus"]

last_grocery_item = Grocery_list[-1] # Gets the last item of an array regardless of its size.

# *--------------------*
#    - 2-Dimensions -
# *--------------------*

Multi_Array = [[1, 2, 3, 4, 5],
               [1, 2, 3, 4, 5],
               [1, 2, 3, 4, 5]]

# *--------------------*
#    - Transforms -
# *--------------------*
## Converting to a list - Strings, tuples or dictionaries

vowel_string = 'aeiou' #String
print(list(vowel_string))

vowel_tuple = ('a', 'e', 'i', 'o', 'u') #Tuple
print(list(vowel_tuple))

vowel_dictionary = {'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5} # Dictionary
print(list(vowel_dictionary))

# copying a list
my_list = [8, 0, 6]
new_list = my_list.copy() 

# Reverse a list
data = [1, 2, 3, 4, 5, 6]
data = data[::-1]

# *------------------*
#    ---- Read ----
# *------------------*

print(", ".join(Grocery_list)) # Shows the list separated with commas
print(Grocery_list[1]) # Returns a specific value of the array. This case: chicken

listSize = len(Grocery_list)
print(f"The grocery list has {listSize} items in it")


Input = input("What is your favorite fruit? ").capitalize().strip()

if Input in Grocery_list: # "not in" can also be used
    print(f"Yes, {Input} is in the fruits list")
else:
    print(f"No, {Input} is not in the fruits list")

"""
The list index() method can take a maximum of three arguments:
    element - the element to be searched
    start (optional) - start searching from this index
    end (optional) - search the element up to this index
"""

ItemIndex = Grocery_list.index("Thyme") # Tells us where this item is in the list.

GroceryListItem = iter(Grocery_list)

def nextItem():
    print(next(GroceryListItem))

nextItem()
nextItem()
nextItem()


UserInput = input("What's your favorite color? ")

Colors = ["Blue", "Red", "Pink", "Green"]

if UserInput in Colors:
    print("The color you mentioned was in a color list.")
else:
    print("There wasn't a match")
    
# *-----------------*
#    - Generators -
# *-----------------*
# https://www.youtube.com/watch?v=bD05uGo_sVI
# The yield keyword is what makes the block of code a generator and acts like next()
# Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.

def Square_Numbers(Numbers):
    for Number in Numbers:
        yield (number * number)

Generated_Numbers = Square_Numbers([1,2,3,4,5])

for Number in Generated_Numbers:
    print(Number)

Generator_List = list(Generated_Numbers)

# *--------------------*
#    ---- Update ----
# *--------------------*

Grocery_list.insert(-1, "Heavy cream") #Adds an item to the end of the list
Grocery_list.append("Rosemary") # Another way to add an item to the end of the list

# List out the items
for item in Grocery_list:  
    print(item)

# List out the items with numbers
for index, item in enumerate(Grocery_list, start=1):  # Indexing is counting with the enumerate function, starting at 1 rather than 0.
    print(index, item)

Grocery_list.sort()


# Checking if an item is in a list
if "Milk" in Grocery_list:
    print("We have milk!")
else:
    print("We need milk!")

# Combine two lists
inventory = ["Sword", "Helm", "Boots"]
chest = ["Potion", "Map", "Gold"]

inventory.extend(chest)

print(inventory) 


# *--------------------*
#    ---- Delete ----
# *--------------------*

Grocery_list.remove("Chicken")
Grocery_list.pop(-1) #Removes the last item of the list

# Examples
# ~~~~~~~~~

words = ["Python", "fun"]
words.insert(1, "is")

# Grocery Example - Sum of just one column
Item = [
    ["Butter", 2],
    ["Milk", 4],
    ["Eggs", 3]
]
"""Index map for array"""
Item_Name = 0
Prices = 1

"""Calculations"""
Total_Price = sum(column[Prices] for column in Item)
Average_Price = sum(column[Prices] for column in Item) / len(Item)
Most_Expensive = max(column[Prices] for column in Item)

print(f"${Total_Price}")        # $9
print(f"${Average_Price}")      # $3
print(f"${Most_Expensive}")     # $4

# Examples
Numbers = [7, 2, 3, 4, 6, 1, 4, 5]

Sum = sum(Numbers)
print(Sum)

# Adding to a list
nums = [1, 2, 3]
nums.append(4)  # Adds 4 to the end list

# Zip - Converts an iterable into a tuple. You can turn that tuple into an array with list()
Names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
Heros = ["Spiderman", "Superman", "Dead Pool", "Batman"]

for Name, Hero in zip(Names, Heros):
    print(f"{Name} is actually {Hero}")


DNA_Sequence_1 = 'atgcttcggcaagactcaaaaata'
DNA_Sequence_2 = 'atgcttcggcaagactaaaaaata'

Paired_Sequences = zip(DNA_Sequence_1, DNA_Sequence_2)
# print(list(Paired_Sequences))

Enumerated_Sequences = enumerate(Paired_Sequences)
# print(list(Enumerated_Sequences))


for instance, (first,second) in Enumerated_Sequences:
    if first != second:
        print(f'Mismatch found at index:{instance}.')

# *----------------------*
#    ---- Unpacking ----
# *----------------------*

inputs = [
    'John',
    'Smith'
    'United States',
    'Blue'
    'Brown',
    29
]

first, last, *_, age = inputs

print(f'{first} {last} is {age} years old.')


# Comprehensions
# Corey: https://www.youtube.com/watch?v=3dt4OGnU5sM
# https://towardsdatascience.com/python-list-comprehensions-in-5-minutes-40a68cbe4561
# https://www.freecodecamp.org/news/list-comprehension-in-python/

# Comprehensions offer an easier, more readable way to create a list 


# New_List = [expression returned for item in iterable]
list = [1,2,3,4,5,6,7,8,9,10]

new_list = []
for number in list:
    new_list.append(number*number)

new_list = [number*number for number in list] 


names = [
    'Rufus B. Cobber',
    'Levent Roswell',
    'Felix K. Rockwell',
    'Jessica Lune'
]

last_names = [name.split(' ')[-1] for name in names]

print(last_names)