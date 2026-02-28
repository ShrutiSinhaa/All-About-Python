# A class is a blueprint (template) used to create objects.
#
# Think of it like a design for something.
#
# Blueprint → Class
#
# Real object created from blueprint → Object

class dog:
    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed

    def intro(self):
        print(self.name,"is a sweet dog aged", self.age, "its a", self.breed)

dog1 = dog('rox', 2 ,'Lab')
dog1.intro()
#  rox is a sweet dog aged 2 its a Lab
###################
# here dog is a object
# in this blueprint we defined the object dog has 3 features - name, age, breed
# then structured the intro.
# now we an use the class to introduce the dog
# this may look like function
# Function → temporary work
# Class → permanent structure
# Use a class when:
#
# You want to group data + behavior together
#
# You need multiple similar objects
#
# You want to model real-world things
#
# You need to store data inside objects
