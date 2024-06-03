"""
VARIABLES

--> It is a container to a value.

"""

# How will I get the memory address for the below ?
print(123456)
roll_number = 123456.0
print(id(roll_number))

# How does the PL knows about the type of data being stored in the varibale ?
# Integer, Float, Strings
print(type(roll_number))

"""
VARIABLES RULES (LEXICAL WAY)

variable ::= (letter | "_")(letter | digit | "_")
letter ::= lowercase | uppercase
lowercase ::= "a" ... "z"
uppercase ::= "A" ... "Z"
digit ::= 0 ... 9
"""

#  Reserved keywords cannot be used as variable names.
# 32 reserved items

import keyword

print(keyword.kwlist)

# Assert = 10
# assert = 10

# How do we define the variables ?
# variable_name = value

name, age, dept_id = "Ashish", 30, 123456
print(name)
print(age)
print(dept_id)

Department_ID = d_ID = 23456
print(Department_ID)
print(d_ID)

"""
HOW DO WE SWAP VALUES ? 
"""
a, b = 10, 20
print("Before A = ", a)
print("Before B = ", b)

a, b = b, a
print("After A = ", a)
print("After B = ", b)

"""
DATA TYPES PYTHON SUPPORTS

1. INTEGERS
2. FLOAT
3. STRINGS
4. COMPLEX NUMBERS
5. LIST
6. TUPLES
7. DICTIONARY
8. SET
"""

# What does the data type NUMERIC contains ?
# INTEGERS, FLOAT and COMPLEX NUMBERS

# What is the limit for JAVA in integers ?
# -2147483648 to 2147483647

# What is the limit for PYTHON in integers ?
# No limit. Only our own system memory limits the data.

age = 20
print(type(age))

salary = 20.23323232323235
print(salary)

# How do we handle exponential numbers ?
print(2e5) # 2 * 10 ^ 5

# How to write 2 raise to the power 5 ?
print(2 ** 5)

# How to handle complex numbers ?
print(2+3j + 3+4j)
print(type(2+4j))

"""
STRINGS
"""

"""
--> Sequence of characters 
a|z or A|Z or even including digits to make it alphanumeric

1. Using ' '
2. Using " "
3. Using """ """

"""

print('Hey, my name is ashish')
print("Hey, my name is abhishek")
print(""" 

######## MY NAME IS TEJA ########

""")

print("Hey, \n" 
      "my\n"
      "name\n"
      "is\n"
      "ashish")


print("Hey, my name is - 'Ashish'")
print('Hey, name is - "Ashish" and teaching "Python"')