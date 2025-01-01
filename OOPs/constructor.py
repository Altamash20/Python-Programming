class Student:
    name = "rohan"
    def __init__(self):
        print(self)
        print("adding new student in database...")


s1 = Student()
print(s1)




class Student:

    #default constructors
    def __init__(self):
        pass
    
    #parameterized constructor
    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in database...")


s1 = Student("rohan")
print(s1.name)

s2 = Student("shyam")
print(s2.name)