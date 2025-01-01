class Student:
    college_name = "ABC college"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new students in database...")


s1 = Student("karan", 97)
print(s1.name, s1.marks)

s2 = Student("arjun", 88)
print(s2.name, s2.marks)

print(s2.college_name)



class Student:
    college_name = "ABC college"
    name = "anonymous" #class attr

    def __init__(self, name, marks):
        self.name = name #obj attr > class attr
        self.marks = marks
        print("adding new students in database...")


s1 = Student("karan", 97)
print(s1.name, s1.marks)

s2 = Student("arjun", 88)
print(s2.name, s2.marks)

print(s2.college_name)