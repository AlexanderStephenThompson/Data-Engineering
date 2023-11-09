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