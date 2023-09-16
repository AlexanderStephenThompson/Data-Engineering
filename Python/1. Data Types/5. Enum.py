import enum

# Using enum class create enumerations
class Days(enum.Enum):
    # Name = Value
    Sun = 1
    Mon = 2
    Tue = 3
   

# print the enum member as a string
print ("The enum member as a string is : ",end="")
print (Days.Mon)

# print name of enum member
print ("The name of enum member is : ",end ="")
print (Days.Tue.name)