num1 = int(input("enter num1\n"))
num2 = int(input("enter num2\n"))
num3 = int(input("enter num3\n"))

if num1 > num2 and num2 > num3:
    print("num1 is greater", num1)
elif num2 > num3 and num2 > num1:
    print("number2", num2)
else :
    print("number3", num3)

