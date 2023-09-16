class Character:

    # ~~~ Class Variables ~~~
    Number_Of_Characters = 0


    # ~~~ Constructor ~~~
    def __init__(self, First_Name, Last_Name, Species, Height, Gender):
        #Direct Attributes
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Species = Species
        self.Height = Height
        self.Gender = Gender

        # Derived Attributes
        self.Full_Name = First_Name + " " + Last_Name

        Character.Number_Of_Characters += 1


    # ~~~~~ Class Methods ~~~~~
    @classmethod
    def Summary(cls):
        return f"There are {Character.Number_Of_Characters} characters in this class."
    

    # ~~~~~ Static Methods ~~~~~
    @staticmethod
    def Class_Description():
        return "This is a character class, you can make characters!"


    # ~~~~~ Object Methods ~~~~~
    def Greeting(self):
        return f"Hey, I'm {self.First_Name} and I'm a {self.Species}."


Fiona = Character("Fiona", "Valentine", "Otter", "105", "Male")
Felix = Character("Felix", "Roswell", "Zebra", "80", "Male")

"""
# *--------------------------*
# |                          |
# |  ~~~~ Dictionaries ~~~~  |
# |                          |
# *--------------------------*

Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
Dictionaries are data structures used to map arbitrary keys to values; essentially creating key-value pairs.
Lists can be thought of as dictionaries with integer keys within a certain range.
Dictionaries can be indexed in the same way as lists, using square brackets containing keys.

Like an actual dictionary, a python dictionary pairs values with attributes who are listed with the item

*----------------*
   - Syntax -
*----------------*

Dictionary_Name = {
    Key_1: Value_1,
    Key_2: Value_2,
    Key_3: Value_3,}

"""

# *---------------------------*
#    ---- Create ----
# *---------------------------*

# *-------------------*
#    - 1-Dimension -
# *-------------------*

Rufus_B_Cobber = {
    "Name": "Rufus B. Cobber",
    "Species": "Red Kangaroo",
    "Fur_color": "Red",
    "Useless Key": "Useless Value"}

Rufus_B_Cobber["Gender"] = "Male"  # Adding a new key-value to the dictionary

# *--------------------*
#    - 2-Dimensions -
# *--------------------*

Items = {
    "Sword": {"Name": "Destroyer",
              "Value": 10,
              "Description": "It stabs",
              "Quantity": 0},

    "Potion": {"Name": "Health Potion",
               "Value": 25,
               "Description": "It heals",
               "Quantity": 0}
}

# *------------------*
#    ---- Read ----
# *------------------*


# 1-D
# Checking whether a given key already exists in a dictionary.  
def checkKey(dict, key): 
      
    if key in dict.keys(): 
        print("Present, ", end =" ") 
        print("value =", dict[key]) 
    else: 
        print("Not present") 

for key, value in Rufus_B_Cobber.items():  # Lists out each key-value pair.
    print(key, value)

print(Rufus_B_Cobber)  # Outputs a raw format of data.
print(Rufus_B_Cobber["Species"])  # Returns the value correlating to the key.

Item_List = Items.keys() # Returns all the keys as a list.
Item_Values = Items.values() # Returns all the values of the items as a list
Item_Info = Items.items() # Returns a list of tuples for each key-value pair.

# 2-D
print(Items["Sword"]["Value"])  # Very semantic statement for nested dictionaries.
print(Items["Sword"]["Quantity"])


# *--------------------*
#    ---- Update ----
# *--------------------*

def addItem(itemName):
    Items[itemName]["Quantity"] += 1

addItem("Sword")

print(Items["Sword"]["Quantity"])


# *--------------------*
#    ---- Delete ----
# *--------------------*

Rufus_B_Cobber.pop("Useless Key")


# Examples

itemName = {
    "costPrice": 32.67,
    "sellPrice": 45.00,
    "inventory": 1200
}
margin = itemName["sellPrice"] - itemName["costPrice"]
netProfit = round(margin * itemName["inventory"])
print(netProfit)


Char = {
    "Fiona":{
        "CharacterInfo":Fiona
    }
}
print(Char["Fiona"]["CharacterInfo"].Species)



# *--------------------------*
# |                          |
# |    ~~~~~ Title ~~~~~     |
# |                          |
# *--------------------------*

# *--------------------------*
#    ------ Header 1 ------
# *--------------------------*

# *----------------*
#    - Header 2 -
# *----------------*

# Header 3
# *------------*