"""
Objects and how they do what they do can be complex, but who they are and what
they do aren’t. When designing your class for your program, you ask not what the
person class look like, but what should the person class look like for this application,
under the program’s circumstances, at this time. It’s about relevancy. 

Like functions, you can peek objects, classes, and methods by right clicking any of those 
and choosing a peek command from the contextual menu. 

Classes Define Objects
    Name: What is it?
    Attributes: What describe the object? This is data about the object.
    Behavior: What can it do?

Self allows the context of the operation to be relative to the object performing that task -- handy!
With that known, object methods always have a self parameter to be able to work in that context. 
This way, the code interpreter always knows what object to work with. 

Syntax
class Class_Name:

    # Class Variables
    Class_Variable = "Some Value"  # This will apply variables to all class instances and objects; optional

    # Behavior Variables - Unassigned for concrete classes to implement how they wish
    interface_Name behavior_Name = null ?? Figure this out


    # ~~~ Constructor ~~~ - Defining the attributes of each object. Can also use data classes
    def __init__(self, First_Attribute, Second_Attribute, Third_Attribute):
        self.First_Attribute = First_Attribute
        self.Second_Attribute = Second_Attribute
        self.Third_Attribute = Third_Attribute

    # ~~~~~ Class Methods ~~~~~ - Work with class variables
    @classmethod
    def Class_Method(cls):
        pass  # Some Instructions

    # ~~~~~ Static Methods ~~~~~ - Doesn't depend on an object of a class. This gives us a way to gain access to a method in a class without the need or creation an object first.
    @staticmethod
    def Static_Method():
        pass  # Some instructions

    # ~~~~~ Object Methods ~~~~~ - Working with objects of the class, often interacting with its attributes in some way
    @property
    def Some_Method(self):
        pass  # Some instructions. The type of return value will determine what kind of objects can use this method.

    # -- Calling --
    # Object Creation:    ObjectName = ClassName(First_Attribute, Second_Attribute, Third_Attribute )
    # Class Method:       ClassName.ClassMethodName()
    # Static Method:      ClassName.StaticMethodName()
    # Object Method:      ObjectName.ObjectMethodName() 
    # Object Attribute:   ObjectName.Attribute




Notes:
 - Classes with object methods that refer to their own properties should be topped with the @property decorator
 - Every concrete class should have a corresponding unittest too
 - The __str__() method returns the string representation of the object. This method is called when print() or str() function is invoked on an object.
 - Python __repr__() function returns the object representation in string format

"""

# *----------------------------------*
#    ------ Classic Examples ------
# *----------------------------------*

# *----------------*
#    - Example 1 -
# *----------------*

from inspect import Parameter
from logging import exception

class Character:

    # ~~~ Class Variables ~~~
    Number_Of_Characters = 0

    # ~~~ Constructor ~~~
    def __init__(self, First_Name, Last_Name, Species, Age, Height, Gender):

        # Class Variables
        Character.Number_Of_Characters += 1

        # Parameters
        genders = ["male", "female"]
        min_Age = 0
        max_Age = 100

        #Direct Attributes
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Species = Species

        if Age > min_Age and Age < max_Age:
            self.Age = Age
        else:
            raise Exception("Age must be 0-100")

        self.Height = Height

        if (Gender.lower() in genders):
            self.Gender = Gender.lower()
        else:
            raise Exception("Only male or female.")

        # Derived Attributes
        self.Full_Name = f"{First_Name} {Last_Name}"

        # Composed Attributes
        

       


    # ~~~~~ Class Methods ~~~~~
    @classmethod
    def Class_Summary(cls):
        return f"There are {Character.Number_Of_Characters} characters in this class."
    

    # ~~~~~ Static Methods ~~~~~
    @staticmethod
    def Class_Description():
        return "This is a character class, you can make characters!"


    # ~~~~~ Object Methods ~~~~~
    def Introduce_Self(self):
        return f"Hey, I'm {self.First_Name} and I'm a {self.Species}."

    def Speak(self):
        if (self.Species == "Dog"):
            print("Bark!")
        elif (self.Species == "Cat"):
            print("Meow!")
        elif (self.Species == "Horse" or self.Species == "Zebra"):
            print("Neigh!")
        elif (self.Species == "Otter"):
            print("Squeak!")
        elif (self.Species == "Dragon"):
            print("Rawr!")
        else:
            print("I speak something else...")

    def Happy_Birthday(self):
        self.Age += 1


# Object Creation
Fiona = Character("Fiona", "Valentine", "Otter", 28, 105, "Female")
Felix = Character("Felix", "Roswell", "Zebra", 24, 80, "Male")

# Class Method: ClassName.ClassMethodName()
print(Character.Class_Summary())

# Static Methods: ClassName.StaticMethodName()
print(Character.Class_Description())

# Object Method: ObjectName.ObjectMethodName() 
print(Felix.Introduce_Self()) # Or print(Character.Introduce_Self(Felix))
Felix.Speak()

# Object Description: ObjectName.Attribute
print(Felix.Gender)
print(Felix.Full_Name)


# Now that we know more about objects, we can do some interesting things

# The is keyword
# Meant to test if two variables refer to the same object, which is different from using === to check if two objects contain the same value
# With an is check, The test returns False if they are not the same object, even if the two objects are 100% equal in value



# *----------------------------------------*
#    ------ Tying Classes Together ------
# *----------------------------------------*
# The fun begins here: https://youtu.be/JeznW_7DlB0?t=1364

# *----------------*
#    - Example 1 -
# *----------------*
class Students:

    # ~~~ Constructor ~~~ - Defining the attributes of each object. Can also use data classes
    def __init__(self, Name, Age, Grade):
        self.Name = Name
        self.Age = Age
        self.Grade = Grade

    # ~~~~~ Object Methods ~~~~~ - Working with objects of the class, often interacting with its attributes in some way
    def getGrade(self):
        return self.Grade

  
class Courses:

    # ~~~ Constructor ~~~ - Defining the attributes of each object. Can also use data classes
    def __init__(self, Name, Student_Capacity):
        self.Name = Name
        self.Student_Capacity = Student_Capacity
        self.Student_List = []

    # ~~~~~ Object Methods ~~~~~ - Working with objects of the class, often interacting with its attributes in some way
    def Add_Student(self, student): # Uses an student object as a parameter. 
        if len(self.Student_List) < self.Student_Capacity:
            self.Student_List.append(student)
            return True
        return False

    def Show_Students(self):
        Last_Student = self.Student_List[-1]

        print("Here's the student list:")     
           
        for student in self.Student_List:
            if student == Last_Student: # Last item doesn't need a comma
                print(student.Name) 
            else:
                print(student.Name, end=", ")

    def Class_Average(self):
        Total_Grade_Points = 0
        Total_Students = len(self.Student_List)
        
        for student in self.Student_List:
            Total_Grade_Points += student.getGrade()

        Class_Average = Total_Grade_Points / Total_Students

        return f"Class average is: {Class_Average}."

Tim = Students("Tim", 19, 95)
Bill = Students("Bill", 19, 75)
Jill = Students("Jill", 19, 70)

Science = Courses("Science", 24)
Science.Add_Student(Tim)
Science.Add_Student(Bill)
Science.Add_Student(Jill)

Science.Show_Students()
print(Science.Class_Average())
print(Science.Student_List[0].Name) # Think of something more semantic. Transform array to dictionary? Or just a variable.


# *----------------*
#    - Example 2 -
# *----------------*
# Make example with a character, backpack and objects to illustrate association, composition, and other relationships.



"""
Relationships
"""


# Inheritance


# Example 1

class Cook:

    def Make_Quesadilla(self):
        print("The cook makes a quesadilla.")

    def Make_Soup(self):
        print("The cook makes a soup.")

    def Make_Burger(self):
        print("The cook makes a burger.")


Jack = Cook()  # Creating an entity, we've assigned Jack as a cook.
Jack.Make_Burger()

print("\nChinese cook")


# The "Cook" in the () is telling Python we want to inherit traits from the cook class.
class Chinese_Cook(Cook):

    def Make_Ramen(self):
        print("The chinese cook made a spicy ramen dish!")


Kaoru = Chinese_Cook()  # Creating an entity
Kaoru.Make_Ramen()
Kaoru.Make_Burger()
