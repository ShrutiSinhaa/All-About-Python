# Tuple is like a list but immutable - can not be changed once defined
# its defined by ()

a=(10,20,30,40)
print(a)
# a.add=(30)#not allowed
#its indexed like list
print(a[0])
print(a[1])

b=("Rahul",25,5.8,True)
print("Name : ",b[0])
print("Age : ",b[1])
print("Height : ",b[2])
print("Enrolled : ",b[3])

#lets try changing the value
#b[0]= "Rahil #not allowed

total=a[0]+a[1]+a[2]+a[3]
print(total)
for x in a:
    print(x)

total=0
for x in a:
    total+=x
    print(total)

print(total)