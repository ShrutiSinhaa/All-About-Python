print(range(10))   #range(0, 10)
print(list(range(10)))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range(5,19))      #range(5, 19)
print(list(range(5,19)))    #[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

for i in range(5,10):
    print(i)

#5
#6
#7
#8
#9

print(list(range(5,35,5))) #here range is 5-35 while the third number 5 is skip
# result - [5, 10, 15, 20, 25, 30]

for i in range(5,35,4):
    print(i)

    #5
#9
#13
#17
#21
#25
#29
#33

##########################################

l=['sun','earth','mars','venus']

for i in range(len(l)):
    print(l[i])
    # sun
    # earth
    #mars
    #venus
