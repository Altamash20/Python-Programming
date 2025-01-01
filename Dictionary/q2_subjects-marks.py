marks1 = float(input("Enter marks of Physics:"))
marks2 = float(input("Enter marks of Chemitry:"))
marks3 = float(input("Enter marks of Maths:"))

marks = {}
marks.update({"phy" : marks1})
marks.update({"chem" : marks2})
marks.update({"maths" : marks3})

print(marks)
