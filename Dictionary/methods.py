student = {
    "name" : "john charlie",
    "sub_marks" : {
        "phy" : 98,
        "chem" : 95,
        "maths" : 91
    }
}

print(student)
print(student.keys())
print(list(student.keys()))
print(tuple(student.keys()))

# number of keys
print(len(student.keys()))
print(len(list(student.keys())))
print(len(tuple(student.keys())))



print(student.values())
print(list(student.values()))
print(tuple(student.values()))



print(student.items())
print(list(student.items()))
print(tuple(student.items()))



print(student["name"])
print(student.get("name"))



student.update({"city" : "pune"})
print(student)