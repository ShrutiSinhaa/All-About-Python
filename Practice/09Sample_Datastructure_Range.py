# Range represents a sequence of numbers
# its immutable
# defined by (n)

a=(5)
a=range(5) #from 0 to 5
print(a)
for x in a:
    print(x)

b=range(4,9)
print(b)
for x in b:
    print(x)
#last number -1 [4,9 means 4 till 9 thatt is 4,5,6,7,8

c=range(5,50,5) #last number is the step value between the value
print(c)
for x in c:
    print(x)

#lets convert a range to list

d=list(range(5,100,5))
print(d) # prints the list
for x in d:
    print(x)