### Sets

"""
Summary
~~~~~~~~~~
Set is a collection which is unordered and unindexed. No duplicate members allowed. Great for working with unique values.
Good to test if a specified value is part of the set (Membership test) and to remove duplicates. 
Can determine what values they share or don't share with other sets.

Abstraction
~~~~~~~~~~
Set_Name = {"Item 1", "Item 2", "Item 3"}
"""


"""
Methods
~~~~~~~~~~

add()	                        Adds an element to the set
clear()	                        Removes all the elements from the set
copy()	                        Returns a copy of the set
difference()	                Returns a set containing the difference between two or more sets
difference_update()	            Removes the items in this set that are also included in another, specified set
discard()	                    Remove the specified item
intersection()	                Returns a set, that are the intersection of to other sets
intersection_update()	        Removes the items in this set that is not present in other, specified set(s)
isdisjoint()	                Returns whether two sets has a intersection or not
issubset()	                    Returns whether another set contains this set or not
issuperset()	                Returns whether this set contains another set or not
pop()	                        Removes the specified element
remove()	                    Removes the specified element
symmetric_difference()	        Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                        Return a set containing the union of sets
update()	                    Update the set with the union of this set and others
"""


#Examples
#~~~~~~~~~

print("\nComparing info with sets.")
My_favorite_colors = {"Black", "Blue", "Orange"}
Your_Favorite_colors = {"Red", "Black", "Purple",}

#The best use of sets is to compare data with the intersection method.
Common_Favorite_Colors = My_favorite_colors.intersection(Your_Favorite_colors)
print(Common_Favorite_Colors)

Word ="Hello"
CreatedSet = set(Word)

for letter in CreatedSet:
    print(letter)
