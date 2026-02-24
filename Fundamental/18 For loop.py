# for loop - it is used to repeat block of code

x=[1,2,3,4,5,6]

for i in x:         #you can use another alphabet instead of i
    print(i)
#1
#2
#3
#4
#5
#6
#########################################
for i in range(4):
    print(i)

   # 0
   # 1
   # 2
   # 3
#############################################
l=[1,2,3,4,5,6]
sum=0
for i in l:
    sum=sum+i

print("total is ",sum)
#21

    ######################################
l=[1,2,3,4,5,6]
sum=0
for i in l:
    print (sum," + ", i, "=", sum+i)
    sum=sum+i

#0  +  1 = 1
#1  +  2 = 3
#3  +  3 = 6
#6  +  4 = 10
#10  +  5 = 15
#15  +  6 = 21

#####################################

l=[1,2,3,4,5,6]

for i in l:
    print(i)
else:
    print("No more number in list")