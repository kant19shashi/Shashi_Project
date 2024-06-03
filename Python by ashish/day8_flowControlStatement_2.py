"""
Iterative Statements
"""

"""
For Loops
    --> Executing a group of statements in a order multiple times. 
    --> SYNTAX:
            for x in sequence:
                _________________________
                _________________________
                _________________________
    --> WHEN: Whenever we want to execute a sequence multiple times, we use a loop
    --> SEQUENCE: Any kind of mutable or immutable data type
            1. List
            2. Tuple
            3. String
            4. Dictionary
            5. Set
            6. Range()
"""

# How to execute a loop for a sequence of STRINGS ?
print(" #################### SEQUENCE OF STRINGS  ####################")
for i in "Apple":
    print(i)

# How to execute a loop for a sequence of LIST ?
print(" #################### SEQUENCE OF LIST  ####################")
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
    if i % 2 == 0:
        print(f"Even - {i}")
    else:
        print(f"Odd - {i}")

# How to execute a loop for a sequence of TUPLE ?
print(" #################### SEQUENCE OF TUPLE  ####################")
x = 0
for i in ("Ashish", 1, 2.3, True, "Apple"):
    print(f"Index = {x}, Value - {i}")
    x = x + 1

# How to execute a loop for a sequence of DICTIONARY ?
print(" #################### SEQUENCE OF DICTIONARY  ####################")
data = {
    "student_name":     "Ashish",
    "student_roll":     12,
    "marks":            [50, 100, 80, 90],
    "Address":          {
        "street":       14,
        "block":        "H",
        "Area":         "Saket",
        "State":        "Delhi"
    },
    1:                  False,
    2:                  2.3
}

# How to get all the keys of the dictionary ?
for key in data:
    print(f"Key = {key}")

# How to get all the values of the dictionary ?
for value in data.values():
    print(f"Value = {value}")

# How to get all the key value pairs of the dictionary ?
x = 0
for item in data.items():
    print(f"Item - {x} is - {item}")
    x = x + 1

# How to execute a loop for a sequence of SET ?
print(" #################### SEQUENCE OF SET  ####################")
student_info = {"Ashish", 7011197716, "1-A", "Delhi", 3.2}
for info in student_info:
    print(f"Student data is = {info}")
    if info == 3.2:
        print("Height is good. ")

# How to execute a loop for a RANGE function ?
print(" #################### RANGE FUNCTION  ####################")
"""
range() --> function
    1. range(n): Start from 0 to n-1
    2. range(m, n): Start from m to n-1
    3. range(m, n , inc/dec): Starts from m to n-1 and take a given step at a time
"""

# How to iterate through a list of top 10 integers ?
print("---------------------------------------")
for i in range(10):
    print(i)

# How to iterate through a list of integers between 10 and 20 ?
print("---------------------------------------")
for i in range(10, 20):
    print(i)

# How to iterate through a list of integers between 10 and 20 and only print even?
print("---------------------------------------")
for i in range(10, 20, 2):
    print(i)

# How to iterate through reverse order ?
print("---------------------------------------")
for i in range(10, 1, -1):
    print(i)


"""
WHILE LOOP

    WHEN: When we do not know how many times the loop will be executed.
    SYNTAX:
            while condition:
                _________________________
                _________________________
                _________________________
"""

print(" #################### PASSWORD CHECK  ####################")

password = ""
while password != "Tester123":
    # password = input("Enter the password - ")
    password = "Tester123"
    if password != "Tester123":
        print("INCORRECT PASSWORD. TRY AGAIN")
    else:
        print("Welcome to the Website!!")

"""
PYTHON ELSE LOOPS
    --> To indicate that the loop has been successfully completed
"""

for i in "Ahmed":
    print(i)
    if i == "e":
        break
else:
    print("Loop completed")

print("This is out of loop statement.")