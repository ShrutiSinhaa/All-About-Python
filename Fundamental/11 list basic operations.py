a = [1, 2, 3, 4, 5, 6]
for number in a:
    print(number) # print as an array
#1
#2
#3
#4
#5
#6

print(a[0:5]) ##(1, 2, 3, 4, 5)
print(a[:])  ##(1, 2, 3, 4, 5, 6)
print(a[-4:])  # (3, 4, 5, 6)
print(a[0:]) # (1, 2, 3, 4, 5, 6)

############### update the list #######################
a[1]='hello'
print(a[:]) ##[1, 'hello', 3, 4, 5, 6]

a[:]=[10,20,30,40,50,60,70,80,90]

print(a[:])  ## [10, 20, 30, 40, 50, 60, 70, 80, 90]
################## delete and remove ##############
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
del b[0] #remove the element number 0 i.e 'a'
print(b[:]) # ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

del b[3]
print(b[:]) #['b', 'c', 'd', 'f', 'g', 'h', 'i', 'j']

b.remove('j') #remove the particular element 'j' irrespective to the element number
print(b[:]) #['b', 'c', 'd', 'f', 'g', 'h', 'i']

c = [1, 1, 1, 2, 3, 2, 2, 3, 1]
print(c[:]) # [1, 1, 1, 2, 3, 2, 2, 3, 1]
c.remove(1) # only first 1 is removed
print(c[:]) # [1, 1, 2, 3, 2, 2, 3, 1]
print(c.pop()) #print the last element
c.clear()
print(c[:])

c=[1,2,3,4,0,9,8,7,6,5]
c.sort()
print(c) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c.sort(reverse=True)
print(c) #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

c.append(5) #add 5 at end
print(c)  #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 5]
print(c.count(5)) #count 5s in the list  #result =2

