"""
SET
"""

"""
PYTHON SET 

    --> Collection of different types of items
    --> Order is NOT maintained
    --> Set are MUTABLE in nature
        CRUD:
            1. Create
            2. Reading / Accessing
            3. Updating 
            4. Deleting 
    --> DUPLICATES ARE NOT ALLOWED
    --> Indexing and Slicing is NOT SUPPORTED
    --> Set is represented using {}
    --> Set does not have any kind of key - value pair
    
"""

"""
CREATING A SET
"""

# How do we create an empty set ?
empty = set()
print(type(empty))

# How do we create a regular set ?
regular = {1, 2, "Ashish", 3.4, True}
print(regular)
print(type(regular))

# Is duplicate allowed ?
duplicate = {1, 2, 2, 2, 3, 4, "A", "A", "B", False, True, True}
print(duplicate)

# Can we add MUTABLE data inside a set ?
mutable = {1, 2, (1, 2, 5, 6, 7)}
print(mutable)
# Any kind of mutable data is not allowed inside a set.

# Can we create a set inside a set ?
# data = {1, 2, 3, {4, 5, 6}}
# print(data)
# TypeError: unhashable type: 'set'

"""
Reading / Accessing a SET
"""

test_data = {1, 2, 3, "A", "B", 2+4j, (3, 4, 5, 6)}

# How do we read a single value inside a set ?
# print(test_data[0])
# TypeError: 'set' object is not subscript-able

print(test_data)

# How do we read multiple values inside a set ?
# TypeError: 'set' object is not subscript-able


"""
Updating a SET
"""

test_data = {1, 2, 3, "A", "B", 2+4j, (3, 4, 5, 6)}

# Can we add a single element inside a set using index ?
# test_data[0] = "Ashish"
# TypeError: 'set' object does not support item assignment
test_data.add("Ashish")
print(test_data)

# Can we add multiple elements inside a set ?
# This is not supported directly
test_data.update([1, 2, "Ahmed", "Anshul", 3.4])
print(test_data)


"""
Deleting a SET
"""
delete_data = {1, 2, 3, 3.4, 'Ashish', 'Anshul', (2+4j), (3, 4, 5, 6), 'Ahmed', 'B', 'A'}

# Can we delete a single item from a set ?
# del delete_data[0]
# print(delete_data)
# TypeError: 'set' object doesn't support item deletion

# What is the difference between different types of delete functions ?

delete_data.pop()
print(delete_data)

delete_data.remove(3.4)
print(delete_data)

delete_data.discard("Anshul_1")
print(delete_data)

"""
FUNCTIONS AND OPERATIONS OF A SET
"""

set_1 = {1, 2, 3, 4, 5, "Ashish", "Garg"}
set_2 = {4, 5, "A", "B"}
set_3 = {1, 2, "A", "C", "D", 3.4}

# How to get union ?
union = set_1.union(set_3, set_2)
print(union)

# How to get intersection ?
inter = set_1.intersection(set_3)
print(inter)

# Can we have identity operation ?
print(set_1 is not set_2)

# Can we have membership operation ?
print("Ashish" in set_1)
print("Garg" in set_2)
print("Abhishek" not in set_3)

# Can we have concatenation operation ?
# print(set_1 + set_2)
# TypeError: unsupported operand type(s) for +: 'set' and 'set'

# Can we have repetition operation ?
# print(set_1 * 3)
# TypeError: unsupported operand type(s) for *: 'set' and 'int'
