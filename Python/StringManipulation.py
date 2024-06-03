

#How to access string
instituation="way2automation"
print(instituation[3])
print(instituation[-4]) #indexing the string
#print(instituation[100])#out of rnage string

# slicing the string
# slicing is an operation which gets you the part of the string
"""
how to get the substring out of string 
variable[begin: end : steps ]
begin: index value from 
end : index until the valuse 

"""

example="ABCDEFGHIJKLMNOP"
print(example[0:4])
print(example[2:10:2])
print(example[::])
#==========================
"""
Name = (input("enter your Name="))
Age = int(input("enter your age="))
print("My name is ", Name)
print("My age is ", Age)

#(f"My name is {Name} and my age is {Age})")
print("myname is {0}" . format(Name))
"""

#string operation anf function

e1=("example 1")
print(len(e1))
print(e1.upper())
print(e1.lower())
print('ba' + 'na' *2)
print('ba' in 'banana')
print ('ba' not in 'bananA')
print('abcd' is 'abcd')