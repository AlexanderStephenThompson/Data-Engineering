"""
# *--------------------------*
# |                          |
# |    ~~~~ Strings ~~~~     |
# |                          |
# *--------------------------*
Encoding is the process of transforming a set of Unicode characters into a sequence of bytes. 
In contrast, decoding is the process of transforming a sequence of encoded bytes into a set of Unicode characters. 

Universal string formats for computers
--- Unicode --- (https://unicode-table.com/en/#0220)
Unicode is a computer industry standard that defines how to represent text for use in computers. 
Full support characters in any written language, icons, emojis, math symbols, currency and other special characters
It is common written as the letter U plus a four-digit hexadecimal number.

-- ASCII -- (http://www.asciitable.com/)
To insert an ASCII character, press and hold down ALT while typing the character code. However,
You must use the numeric keypad to type the numbers, and not the keyboard. Make sure that the 
NUM LOCK key is on if your keyboard requires it to type numbers on the numeric keypad

Do note the difference between the code itself and the keystroke shortcut (At least for Windows)

-- UTF -- 
# UTF-8, UTF-16, and UTF-32 are all different encodings
 
Strings are iterable. So, you can perform loops or data structure like operations on them. More on this later.

https://www.programiz.com/python-programming/methods/string

Python allows you to use single or double quotes.

----------------------------------------

The end parameter is used to append any string at the end of the output of the print statement in python.
By default, the print method ends with a newline. This means there is no need to explicitly specify the parameter end as '\n'. 
The sep is what goes between each word/object, the default is just a space.


"""

# *----------------------------*
#    ------ Common Use ------
# *----------------------------*

# Single Line comment

# Multiple line comment
"""This is a
multiple line
comment"""

# TODO: Something you have to do.

# Printing
print('Hello, world!')  # Single quotes
print("Hello, world!")  # Double quotes

# print() function comes with a parameter called ‘end’. 
# By default, the value of this parameter is ‘\n’, i.e. the new line character.

# The sep= parameter allows you to overwrite the space separator by default
print('G','F','G', sep='') # GFG
print('09','12','2016', sep='-') # 09-12-2016
print('KelstonUniversity','gmail.com', sep='@') # KelstonUniversity@gmail.com

# The end= parameter allows you to overwrite Python's way of ending a print statement (A newline with \n)
print("I'm so excited", end="!") # I'm so excited!


# User Input
Name = input("What is your name? ")

# Interpolation
print(f"It's good to meet you, {Name}. Let's move onto the next example.")

import platform
Version = platform.python_version()
Language = "Python"

print(f"This is {Language.upper()} version {Version}")

# Line breaks
print("This is the first line \n"
      "This is the second \n"
      "Then this is the last")

# Escape characters
#  \'	      Single Quote
#  \\	      Backslash
#  \n	      New Line
#  \r	      Carriage Return
#  \t	      Tab
#  \b	      Backspace
#  \f	      Form Feed
#  \ooo     Octal value
#  \xhh     Hex value

# Raw Text
print(r"This is raw text. \t")

# *-----------------------------------*
#    - String Based Object Methods -
# *-----------------------------------*
# Methods are actions that can be performed on objects.

# https://docs.python.org/3/library/string.html
# https://www.w3schools.com/python/ref_string_format.asp 


# Formatting
Example = "I'm a test!"

Example.upper # I'M A TEST!
Example.lower # i'm a test!

# int() - Converts string to numbers
print(int("357"))

# len()
print("Number of characters your name has is " + str(len(Name)))  # len() function here

# replace()
Welcome_Message = "Hello, universe!"
print(Welcome_Message.replace("universe", "world"))  # Replaced the word "universe" with "world".

"""
Index & Slice - Slicing allows you to grab a subsection of multiple characters

Syntax:
[Start:Stop:Step]
Start - Numerical index for the slice to start
Stop - Index you will go up to, but not include
Step - Size of the jump you make.

[:] Extracts the entire sequence from start to end
[start:] Specifies where to start and goes all the way to the end
[:end] Start from the start until the specified end
[start:end] Specifies both a start and an end.
"""

#Greeting
slicedGreet = "Hello, World!"
print(slicedGreet[1:5])

# Email Generation
First_Name = "Alexander"
Last_Name = "Thompson"

Email = First_Name + Last_Name + "@gmail.com"
print(Email)

# Split() - Returns a list of items
# Syntax string.split(separator, max number of splits performed)
def format_date(date):
      d, m, y = date.split()
      return f"{y}{m}{d}"


email = 'user@example.com'
domain = email.split('@')[1] # First instance of the array from the split function. 
print(domain)  # Fetches just the domain by splitting the string and selecting the second index of the result


# *----------------------------*
#    ------ Formatting ------
# *----------------------------*
Power_Level = 9001
print(f"{Power_Level:,}") # 9,001

# Finance
housePrice = 299999.99
print(f"The price of the house is ${housePrice:,}")

# Number Systems
number = 157
print(f"{number}")      # Normal
print(f"{number:b}")    # Binary
print(f"{number:o}")    # Octal
print(f"{number:x}")    # Hexadecimal
print(f"{number:d}")    # Decimal

# Percentage
Passes = 18
Attempts = 29
print(f"The completion percentage is {Passes/Attempts:.2%}")

# Assigning strings to the variables 
left_alignment = "Left Text"
center_alignment = "Centered Text"
right_alignment = "Right Text"
  
# Printing out aligned text 
print(f"{left_alignment : <20}{center_alignment : ^15}{right_alignment : >20}") 

sectionDivisor = "Section"
print(f"{sectionDivisor:=^50}")

# Tables
names = ['Raj', 'Shivam', 'Shreeya', 'Kartik'] 
marks = [7, 9, 8, 5] 
div = ['A', 'A', 'C', 'B'] 
id = [21, 52, 27, 38] 
  
# Printing Aligned Header 
print(f"{'Name' : <10}{'Marks' : ^10}{'Division' : ^10}{'ID' : >5}") 
  
# Printing values of variables in Aligned manner 
for i in range(0, 4): 
  print(f"{names[i] : <10}{marks[i] : ^10}{div[i] : ^10}{id[i] : >5}") 





# *-------------*
#    - Dates -
# *-------------*
"""
The datetime object has a method for formatting date objects into readable strings.
The method is called strftime(), and takes one parameter, format, to specify the format of the returned string

Directive   Description	                                                      Example	
%a	      Weekday, short version	                                          Wed	
%A	      Weekday, full version	                                          Wednesday	
%w	      Weekday as a number 0-6, 0 is Sunday	                        3	
%d	      Day of month 01-31	                                          31	
%b	      Month name, short version	                                    Dec	
%B	      Month name, full version	                                    December	
%m	      Month as a number 01-12             	                        12	
%y	      Year, short version, without century	                        18	
%Y	      Year, full version	                                          2018	
%H	      Hour 00-23	                                                      17	
%I	      Hour 00-12	                                                      05	
%p	      AM/PM	                                                            PM	
%M	      Minute 00-59	                                                41	
%S	      Second 00-59	                                                08	
%f	      Microsecond 000000-999999	                                    548513	
%z	      UTC offset	                                                      +0100	
%Z	      Timezone                            	                        CST	
%j	      Day number of year 001-366	                                    365	
%U	      Week number of year, Sunday as the first day of week, 00-53	      52	
%W	      Week number of year, Monday as the first day of week, 00-53	      52	
%c	      Local version of date and time	Mon Dec 31 17:41:00           2018	
%x	      Local version of date	                                          12/31/18	
%X	      Local version of time	                                          17:41:00	
%%	      A % character	                                                %
"""

# *-----------------------*
#    ------ Regex ------
# *-----------------------*
# Define a search pattern to find, replace or validate string in your code

import re
# https://www.w3schools.com/python/python_regex.asp


# Search
Text_To_Search = "The rain in Spain"
Pattern = r"^The.*Spain$" # The regular expression

Result = re.search(Pattern, Text_To_Search)

if Result:
  print("Yes, we have a match!")
else:
  print("No match was found")

# findall
#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

"""The list contains the matches in the order they are found.
If no matches are found, an empty list is returned"""

txt = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

# Split
#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# Sub
#Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub("\s", "9", txt) # You can ontrol the number of replacements by specifying the count parameter
print(x)