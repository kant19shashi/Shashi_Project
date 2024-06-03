"""
Flow control statement
"""

"""
PYTHON FLOW CONTROL STATEMENT 

    1. SELECTION STATEMENTS
        --> if
        --> if - else
        --> if - elif
        --> if - elif - else
        
    2. INTERACTIVE STATEMENTS
        --> while loop
        --> for loop
        
    3. TRANSFER STATEMENT
        --> break
        --> continue
        --> pass

"""

print("############# SELECTION STATEMENT #############")

print("------- IF BLOCK -------")
marks = 91
if marks > 90:
    print("The student has passed the exam successfully. ")

print("This is the next section of the code")

print("\n------- IF ELSE BLOCK -------")
marks = 88
if marks > 90:
    print("The student has passed the exam successfully. ")
else:
    print("Student FAILED")

print("This is the next section of the code")

print("\n------- IF ELIF BLOCK -------")
marks = 88
if marks > 90:
    print("GRADE --> A+ ")
elif 80 < marks <= 90:
    print("GRADE --> B+ ")
elif 70 < marks <= 80:
    print("GRADE --> C+ ")
elif 60 < marks <= 70:
    print("GRADE --> D+ ")

print("This is the next section of the code")

print("\n------- IF ELIF ELSE BLOCK -------")
marks = int(input("Enter the marks - "))
if marks > 90:
    print("GRADE --> A+ ")
elif 80 < marks <= 90:
    print("GRADE --> B+ ")
elif 70 < marks <= 80:
    print("GRADE --> C+ ")
elif 60 < marks <= 70:
    print("GRADE --> D+ ")
else:
    print("Student FAILED")

print("This is the next section of the code")