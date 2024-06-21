name="shashi"
age=30
print(f"my name is {name} and my age is {age}")


# factorial

# num=int(input("enter integer number"))
num=5
factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i
#
#
# print("factorial of five=",factorial)

while num>0:
    factorial=factorial*num
    num=num-1

print(factorial)