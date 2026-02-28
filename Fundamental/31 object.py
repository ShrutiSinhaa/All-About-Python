# object is collection of data and method
# Class = Blueprint
# Object = Real item made from that blueprint

class Student:
    def __init__(self, name):
        self.name = name
    def intro(self):
        return self.name + " is student of class 10"
# using print command would result in giving a 'none' after every intro because:
# Run intro()
#
# Print whatever intro() returns
#
# Since intro() returns nothing → it returns None
#
# So Python prints None.
s1 = Student("Bipeen")
s2 = Student("Rahul")

print(s1.intro())
print(s2.intro())
print(s1.name)
# s1 is one object

# s2 is another object
# Bipeen is student of class 10
# Rahul is student of class 10
# Bipeen