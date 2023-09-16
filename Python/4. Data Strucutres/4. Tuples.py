### Tuples

"""
Summary
~~~~~~~~~~
Tuple_Name = (Item 1, Item 2, Item 3)

Think of a tuple as being the same as creating a constant since it isunchanging.
Tuples are great for information that will not change, like coordinates, dish formulas, and identification

Tuple is a collection which is ordered and unchangeable. Allows duplicate members. Maintains data integrity
Since tuple are immutable, iterating through tuple is faster than with list. So there is a slight performance boost.
Tuples that contain immutable elements can be used as key for a dictionary. With list, this is not possible.
Implementing unchanging data as a tuple will guarantee that it remains write-protected.
"""

"""
Methods
~~~~~~~~~~
"""


#Examples
#~~~~~~~~~
Secret_Location = (-35.787315, 137.230444)
Quesadilla_Formula = ("Wrap", "Meat", "Cheese", "Roasted-vegetables", "Sour-cream", "Salsa")
Rufus_B_Cobber = ("Rufus B. Cobber", "Male", "Kangaroo", "375")
Color = (120, 30, 50)

print(Secret_Location)
print(Quesadilla_Formula)
print(Rufus_B_Cobber)

#Unpacking Tuples
Tuple_List = [(1,2),(3,4),(5,6),(7,8),(9,10)]

for Tuple in Tuple_List:
    print(Tuple)

#Or

for (First_Number, Second_Number) in Tuple_List:
    print(First_Number)
    print(Second_Number)