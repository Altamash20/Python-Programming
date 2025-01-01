marks = float(input("Enter your marks:"))

if(marks>=90):
    print("You got Grade:A")
elif(90>marks>=80):
    print("You got Grade:B")
elif(80>marks>=70):
    print("You got Grade:C")
elif(70>marks>=60):
    print("You got Grade:D")
elif(60>marks>=50):
    print("You got Grade:E")
else:
    print("You failed in the Examination...")



# same program using logical operators

marks = float(input("Enter your marks:"))

if(marks>=90):
    print("You got Grade:A")
elif(marks<90 and marks>=80):
    print("You got Grade:B")
elif(marks<80 and marks>=70):
    print("You got Grade:C")
elif(marks<70 and marks>=60):
    print("You got Grade:D")
elif(marks<60 and marks>=50):
    print("You got Grade:E")
else:
    print("You failed in the Examination...")