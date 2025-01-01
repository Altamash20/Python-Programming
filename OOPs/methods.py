class Student:
    college_name = "ABC college"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student")


s1 = Student("rahul", 97)
print(s1.name, s1.marks)
s1.welcome()