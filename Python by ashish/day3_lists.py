"""
LISTS
"""

"""
PYTHON LIST

    --> Collection of heterogeneous items
    --> String, int, float etc. 
    --> The order in which we add the data, that is maintained. 
    --> Duplicate items can be added inside a list
    --> Should be implemented using []
    --> MUTABLE in nature
        1. Create a list
        2. Read / Access a list
        3. Update a list
        4. Delete a list
    --> CRUD Operations
"""

"""
CREATING A LIST
"""

# How to create an empty list ?
empty = []
print(type(empty))
print(empty)

# How to create a regular list ?
regular = ["Ashish", 10, 99.34, 3 + 4j, True, "Automation"]
print(regular)
print(type(regular))

# Can a list contain another list inside it ?
sublist = ["Ashish", 10, ["Garg", 30], True, 20.4, "Ashish"]
print(sublist)
print(type(sublist))

# Can you convert a string into a list ?
place = "INDIA"
print(list(place))

# Create a list with first 10 integers ?
"""
range(begin, end, step)
    begin ::    From where to start ?
    end ::      Where to stop ? 
    step ::     increment / decrement ? 
    END IS ALWAYS NOT INCLUDED
"""
first10Intergers = list(range(0, 10, 1))
print(first10Intergers)

"""
READ / ACCESS A LIST
--> Index values always starts from 0.
"""
example = ["Ashish", 1, 2, 3, 4.5, ["Abhishek", True, 4 + 3j], 5, ("Shashank", 34, 2.3), 6, {"name": "Ahmed"}]
print(example)

# How is the order maintained in a list ?
print(example[0])
print(example[5])
print(example[5][0])

# How to we read inside a multidimensional list ?
multi = [
    [1, 2, 3, ["A", "B", ["C", ["D"]]]],
    [4, 5, 6],
    [7, 8, 9]
]
print(multi[0])
print(multi[2])
print(multi[0][1])
print(multi[1][2])
print(multi[0][3][2][0])

# Can we access multiple items from a list ?
# SLICING Operation is supported in a list
print(example[0:3])

"""
UPDATING A LIST 
"""

# Can we update a complete list ?
shopping_items = ["T-Shirt", "Glasses", 10]
print(shopping_items)
shopping_items = [10, 20, 30, 40, "Bag"]
print(shopping_items)

# Can we update a single item in a list ?
shopping_items = [10, 20, 30, 40, "Bag"]
shopping_items[2] = "Fruits"
print(shopping_items)

# Can we update multiple items in a list ?
shopping_items = [10, 20, "Fruits", 40, "Bag"]
shopping_items[0:3] = [1, 2, "Milk"]
print(shopping_items)

# What will happen if I give the last + 1 index value to update ?
shopping_items = [1, 2, 'Milk', 40, 'Bag']
# shopping_items[5] = "Fruits"
print(shopping_items)

"""
DELETE A LIST
"""

# Can we delete an entire list ?
test = [1, 2, 3, 4, "Ashish"]
print(test)
del test
# print(test)

# Can we delete a single item inside a list ?
test = [1, 2, 3, 4, "Ashish"]
del test[1]
print(test)

# Can we delete multiple items inside a list ?
test = [1, 2, 3, 4, "Ashish"]
del test[1:3]
print(test)

"""
DIFFERENT OPERATIONS ON A LIST 
"""
list_1 = [1, 2, 3, 4, 5, "Ashish"]
list_2 = [1.2, 2.3, 3.4, 4.5, "Abhishek", True]

# CONCATENATION
combined = list_1 + list_2
print(combined)
print(list_1 + list_2 == list_2 + list_1)

# REPETITION
repeated = list_1 * 3
print(repeated)

list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(len(list_3))
print(max(list_3))
print(min(list_3))

# How to we append items in the end of the list ?
list_3.append("Ashish")
print(list_3)

list_3.append(["A", "B", 1, 2, 3])
print(list_3)

# How to we add some items at a given index position ?
list_3.insert(1, ["Ashish", 1, 2])
print(list_3)

list_3.insert(100, "Ahmed")
print(list_3)

# How to we remove items using value from a list ?
list_3.remove("Ashish")
print(list_3)

# How do we remove items using index value ?
list_3.pop(2)
print(list_3)