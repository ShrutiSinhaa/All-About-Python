# constructors are like methods inside Python programming which we can use.
# there are two types of constructors inside Python programming: first is default constructor,
# second is parameterized constructor. So, the differences in parameter constructor, you need to provide the various
# parameters or arguments.

class Student: #this is class
    def __init__(self): # this is default constructor
        print("Student object created")

s1 = Student() # this is object

class Student1:
    def __init__(self, name, age): #this is parameter constructor
        self.name = name
        self.age = age

s1 = Student1("Bipeen", 25)

print(s1.name, s1.age)
