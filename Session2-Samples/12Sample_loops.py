# print Welcome 5 times
# type ---  print("Welcome") -- 5 times or use loops

for i in range(5): # i is loop variable / range(5) = 1 to 5
    print("Welcome")

for a in range(1,6): #here a is loop variable / range(1,6) = 1 to 5
    print(a)
#print a list

fruits = ["apple", "banana", "cherry"]
for x in fruits: print(x)
# Use for loop when you know how many times you want to run the loop
# when you dont know the number of time but condition to be met then we use - While loop

count = 1
while count <= 8:
    print(count)
    count += 1 #this would keep adding 1 to count and keep printing till count =5

#lets print a table

num = int(input("Enter a number: "))

for i in range(1,11):
    print(num,"X",i,"=",num*i)