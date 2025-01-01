num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))
num4 = float(input("Enter fourth number:"))

if(num1>num2 and num1>num3 and num1>num4):
    print("First number is greatest")
elif(num2>num3 and num2>num4):
    print("Second number is greatest")
elif(num3>num4):
    print("Third number is greatest")
else:
    print("Fourth number is greatest")