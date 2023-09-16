"""
•	JSON: syntax, structure, data types (numbers, strings, Boolean values, null), compound data (arrays and objects), sample JSON documents and their anatomies
•	the json module: serialization and deserialization, serializing Python data/deserializing JSON (the dumps() and loads methods), serializng and deserializing Python objects
•	XML: syntax, structure, sample xml documents and their anatomies, DTD, XML as a tree
•	processing xml files

"""


# *-------------------------*
# |                         |
# |    ~~~~~ JSON ~~~~~     |
# |                         |
# *-------------------------*
import json

# *---------------------------*
#    ------ Serialize ------
# *---------------------------*
# JSON --> Dictionary

Rufus_JSON = '{"Name": "Rufus", "Species": "Kangaroo", "Gender": "Male"}'
Rufus_Dictionary = json.load(Rufus_JSON)  
print(Rufus_Dictionary['Species'])


# *-----------------------------*
#    ------ Deserialize ------
# *-----------------------------*
# Dictionary --> JSON

Rufus_Dictionary = {
    "Name": "Rufus",
    "Species": "Kangaroo",
    "Gender": "Male"
}

Rufus_JSON = json.dumps(Rufus_Dictionary)  
print(Rufus_JSON)


# *-------------------------*
# |                         |
# |    ~~~~~ CSV ~~~~~      |
# |                         |
# *-------------------------*
