"""
TUPLES
"""

"""
TUPLES

    --> Tuples are the READ ONLY version for a LIST
    --> Tuples are IMMUTABLE in nature 
    --> Order is preserved
    --> Duplicates are allowed
    --> Tuples are represented using ()
    --> Heterogeneous values are allowed. 
    --> Indexing and Slicing operations are allowed in this. 
    
    CRUD
        1. Create a tuple ✔︎
        2. Reading / Accessing a tuple ✔︎
        3. Update a tuple ✘ (Partially allowed)
        4. Delete a tuple ✘ (Partially allowed)
"""

"""
CREATING A TUPLE
"""

# How to we create an empty tuple ?
empty = ()
print(empty)
print(type(empty))

# How do we create regular tuple ?
regular = ("Ashish", 10, 10.2, True, 3+2j, [1, 2, 3, 4, 5])
print(regular)

# Can we have a tuple inside a tuple ?
regular2 = ("Ashish", 10, 10.2, True, 3+2j, [1, 2, 3, 4, 5], ("Abhishek", "A", 1, 2, 3))
print(regular2)
print(type(regular2))

# What is tuple packing ?
tuple_1 = "Ashish", 10, 10.2, True, 3+2j, [1, 2, 3, 4, 5]
print(tuple_1)
print(type(tuple_1))

t2 = 10
t3 = 20,
print(type(t2))
print(type(t3))

# What is tuple un-packing ?
regular = ("Ashish", 10, 10.2, True, 3+2j, [1, 2, 3, 4, 5])
a, b, c, d, e, f = regular
print(a)
print(f)
print(c)

# Convert a string to a tuple
string = "Ashish"
print(tuple(string))

"""
READING / ACCESSING A TUPLE 
"""

# How do we read a complete tuple ?
regular = ("Ashish", 10, 10.2, True, 3+2j, [1, 2, 3, 4, 5])
print(regular)

# How do we read a single value inside a tuple ?
regular = ("Ashish", 10, 10.2, True, 3+2j, [1, 2, 3, 4, 5])
print(regular[0])
print(regular[4])
# print(regular[10])

# How do we read multiple values inside a tuple ?
regular = ("Ashish", 10, 10.2, True, 3+2j, [1, 2, 3, 4, 5])
print(regular[:5])
print(regular[3:5])

"""
UPDATING A TUPLE
"""

# How do we update an entire tuple ?
initial_regular = ("Ashish", 10, 10.2, True, 3+2j, [1, 2, 3, 4, 5])
print(initial_regular)
initial_regular = ("Abhishek", 100, 100.2, False)
print(initial_regular)

# How do we update a single value inside a tuple ?
# TypeError: 'tuple' object does not support item assignment
# regular = ("Ashish", 10, 10.2, True, 3+2j, [1, 2, 3, 4, 5])
# regular[2] = "Abhishek"
# print(regular)

"""
DELETING A TUPLE
"""

# How do we delete an entire tuple ?
regular = ("Ashish", 10, 10.2, True, 3+2j, [1, 2, 3, 4, 5])
print(regular)
del regular
# NameError: name 'regular' is not defined.
# print(regular)

# How do we delete a single item from a tuple ?
regular = ("Ashish", 10, 10.2, True, 3+2j, [1, 2, 3, 4, 5])
# TypeError: 'tuple' object doesn't support item deletion
# del regular[2]
print(regular)