Name =[]
Grade=[]
roll=[]
while True:
    n=input("Enter the name of student")
    g=int(input("Enter the grade of student"))
    r=int(input("Enter the roll number of student"))
    Name.append(n)
    Grade.append(g)
    roll.append(r)
    print(Name)
    print(Grade)    
    print(roll)
    z= input("press y for another chance or q for quit") # this is deciding factor for "while" loop. this should stay inside loop
    if z != "y":
        break
print("Program ended")