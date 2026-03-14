# List - ordered, duplicate allowed, number/string / mix / blank
# it is mutable
a = [] # it's represented by []
print(a)
a.append(10)
print(a)
a.append(20)
print(a)

b = [1,2,3,4,5,6,7,8,9,10]
print(b)

c = [5,2,3,4,1,6,7]
print(c)
# add multiple values to c
c.extend([4,5,7,8])
print(c)
c.append("hello") # for single value
print(c)

d = [1,5,7,"dev",5,3,5,"fax"]
print(d)

# list are ordered - means it prints in the same order as they are defined

# lists are indexed - every input get indexed

print(d[0])
print(d[1])
print(d[2])
print(d[3])
print(d[4])

students = ["shruti","Ramya","Bips","Vins","David"]
grades = ["A","B","A","C","D"]

print("Hello", students[0],"you earned grade", grades[0])
print("Hello", students[1],"you earned grade", grades[1])
print("Hello", students[2],"you earned grade", grades[2])
print("Hello", students[3],"you earned grade", grades[3])
print("Hello", students[4],"you earned grade", grades[4])





Maths=[10,45,23,76,77]
Science=[34,54,32,18,17]
students = ["Davis","Romal","Naidu","Haidar","Jess"]
print(students[0],":total marks =",Maths[0]+Science[0])
print(students[1],":total marks =",Maths[1]+Science[1])
print(students[2],":total marks =",Maths[2]+Science[2])
print(students[3],":total marks =",Maths[3]+Science[3])
print(students[4],":total marks =",Maths[4]+Science[4])