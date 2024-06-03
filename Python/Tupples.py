

empty=()
print(empty)
print(type(empty))

regular=('shashi','manoj', 0,1,4,5,46.7)
print(regular)

# packing
regular2="shashikumarsingh",True,'manoj', 0,1,4,5,46.7
print(regular2)
print(type(regular2))

# unpacking
regular3= "shashikumarsingh",True,'manoj', 0,1,4,5,46.7,[1,2,4,89,]

a,b,c,d,e,f,g,i,j=regular3
print(a)
print(j)
print(type(a))
print(type(b))
print(type(c))
print(type(j))
# print(a+f)

#Reading the value in tuiple
regular3= "shashikumarsingh",True,'manoj', 0,1,4,5,46.7,[1,2,4,89,]
print(regular2[2])
print(regular2[:4])
print(regular2[-2:-5])