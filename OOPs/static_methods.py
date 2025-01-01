class Student:
    college_name = "ABC college"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def welcome(self):
        print("welcome student")


s1 = Student("rahul", 97)
print(s1.name, s1.marks)
s1.welcome()
s1.hello()