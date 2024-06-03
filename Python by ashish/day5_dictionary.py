"""
DICTIONARY
"""

"""
PYTHON DICTIONARY
    
    A dictionary is a combination of key and value pair.
    
    key --> value
    word --> meaning
    
    --> The order of values is NOT PRESERVED. 
    --> Indexing and Slicing is NOT ALLOWED. 
    --> This is implemented using {}
    --> Dictionaries are MUTABLE in nature
        1. Creating a dict
        2. Reading a dict
        3. Updating a dict
        4. Deleting a dict
    --> Heterogeneous values are allowed. 
    --> Duplicate values are allowed, but not the duplicate keys. 
        
"""

"""
CREATING A DICTIONARY
"""

# How to create an empty dictionary ?
empty = {}
print(type(empty))

# How do we create a regular dictionary ?
regular = {
    "student_name": "Ashish",
    "student_roll": 10,
    "student_avg_marks": 88.4,
    10: 2+4j,
    "student_subjects": ["A", "B", "C"]
}
print(regular)
print(type(regular))

# Can we define the dictionary key as heterogeneous ?
# Any mutable object cannot be defined as a key to dictionary.
example = {
    "name": "Ashish",
    # TypeError: unhashable type: 'list'
    # [1, 2, 3, 4]: "Abhishek",
    (4, 5, 6, "A"): {
        "A": "B",
        "X": 2
    }
}
print(example)
print(type(example))

# How to convert a list of tuples into a dictionary ?
list_of_tuples = [
    ("name", "Ashish"),
    (10, 100.2),
    ("age", 10)
]
test = dict(list_of_tuples)
print(test)

"""
READING A DICTIONARY
"""

# How do we read a dictionary item ?
# dictionary_name[name_of_the_key]

example = {1: 2, "name": "Ashish", "isEmployed": True}

# How to access complete dictionary ?
print(example)

# How to read a single value in a dictionary ?
print(example[1])
print(example["name"])
print(example["isEmployed"])
# KeyError: 2
# print(example[2])

# How to access multiple values in a dictionary ?
# With loops

# How to access all the keys of the dictionary ?
print(example.keys())

# How to access all the values of the dictionary ?
print(example.values())

# How to access all the key value pairs in a dictionary ?
print(example.items())

"""
UPDATING A DICTIONARY 
"""

# How to update an entire dictionary ?
ex = {1: 2, "name": "Ashish"}
print(ex)
ex = {3: 4, "age": 20}
print(ex)

# How to update a single item in a dictionary ?
test = {"name": "Abhijeet", "age": 20, "salary": 3000.0, 1:3, (1, 2, 3): "Aryan"}
print(test)
test["name"] = "Anshul"
test[1] = 48
test[(1, 2, 3)] = "Ashish"
print(test)

# Can we add a new key value pair in a dictionary ?
test["new"] = "Item"
print(test)

# How to update multiple item in a dictionary ?
# Taking up later.

"""
DELETING A DICTIONARY
"""

# Can we delete an entire dictionary ?
test_2 = {"name": "Abhijeet", "age": 20, "salary": 3000.0, 1:3, (1, 2, 3): "Aryan"}
print(test_2)
del test_2
# NameError: name 'test_2' is not defined
# print(test_2)

# Can we delete single items from dictionary ?
test_2 = {"name": "Abhijeet", "age": 20, "salary": 3000.0, 1:3, (1, 2, 3): "Aryan"}
print(test_2)
del test_2[1]
print(test_2)

# What is the difference between pop() and popitem() ?
test_2 = {"name": "Abhijeet", "age": 20, "salary": 3000.0, 1:3, (1, 2, 3): "Aryan"}
print(test_2)
# KeyError: 'ages'
# del test_2["ages"]
test_2.pop("age")
print(test_2)
test_2.popitem()
print(test_2)

