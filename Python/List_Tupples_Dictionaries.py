#list

"""
Creating the list
"""

"""
Creating the list
"""

empty=list([])
print(empty)
marks=list([])
print(type(marks))

example=list([1,2,3,"Shashi","manoj",True ,False,[3,5,7,"dinesh"]])
print(type(example))
print(example[0])
print(example[6])
place ='new delhi'
print(list(place))

#verify the below statement
print("Apple"== ['a','p','p','l','e'])
print(list("apple")==['a','p','p','l','e'])

# what is range function
#range (begin,and , start )
ab=list(range(1,10,1))
print(ab)
date="15 september 2023"
print(date)
print(date.split())

"""
updating the list

"""
access= [1,2,3,'shashi',3.6]
print(access[1])
#How to we read inside a multinational list
multi= [

    [1,2,3,'shashi',3.5,[1,5,60,[4.6],'manoj']],
    [4.5,6],
    [7,8,9]

]

print(type(multi))
print(multi)
print(multi[0])
print(multi[0][3])
print(multi[2][2])
print(multi[0][5][4])

#slicing

print(example[0:2])
print(multi[0:3])
print(type(multi))

#Updating the list
shoping_items=['manogo','banana',34,87,90]
print(shoping_items)
shoping_items[3]='Applle'
shoping_items [4]=100
print(shoping_items)

#updating mulltiple ittems
shoping_items[0:3]=[1,'milk',400]
print(shoping_items)
