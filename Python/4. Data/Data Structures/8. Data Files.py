# JSON

import json

#Convert JSON into Python

# some JSON:
JSON_Structure =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
PythonStructure = json.loads(JSON_Structure)

# the result is a Python dictionary:
print(PythonStructure["age"])


# Convert Python into JSON

# a Python object (dict):
PythonDataStructure = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
JSON_DataStructure = json.dumps(PythonDataStructure)

# the result is a JSON string:
print(JSON_DataStructure)
