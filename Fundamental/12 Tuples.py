# its similar to list. but its ordered and unchangeable. it allows duplicate elements.
#######################  define tules #####################
#black tuple
a=()
print(a) #()
# integer tuple
a=(1,2,3) #(1, 2, 3)
print(a)
b=1,2,3,4
print(b) #(1, 2, 3, 4)
# list and tuple inside tuple
d=("mouse","apple",(1,2,3,4),['a','b','c'])
print(d) #('mouse', 'apple', (1, 2, 3, 4), ['a', 'b', 'c'])

############## a tuple with single string or element is not considered by tuple in python ############

byta = ("mouse")
print(type(byta))  # result - <class 'str'>
byta = ("apple", "banana", "cherry")
print(type(byta))   #result <class 'tuple'>
gama = (10)
print(type(gama)) #result - <class 'int'>
gama = (10, 20, 30)
print(type(gama))  #result<class 'tuple'>

################ Basic operations ################

print(gama[0:2]) #(10, 20)
print(gama[:2]) #(10, 20)
print(gama[2:]) #(30,)
print(gama[-2:]) #(20, 30)
print(byta[0][2]) #p
print(byta[1][2]) #n
print(byta[2][2:5]) #err

#########################################

alpha=1,2,3,4,5,6,7,8,9
print(alpha) # (1, 2, 3, 4, 5, 6, 7, 8, 9)
####   Tuples are immutable, meaning you cannot change, add, or remove items after the tuple is created.
# there is a subtle but important "loophole" to tuple immutability.
# While you cannot change which objects the tuple points to,
# you can change the contents of those objects if they are mutable ############

alpha=("hello","world",[1,2,3,4,5],['a','b','c','d'])
print(alpha)  #('hello', 'world', [1, 2, 3, 4, 5], ['a', 'b', 'c', 'd'])

alpha[2][0]='H' #('hello', 'world', ['H', 2, 3, 4, 5], ['a', 'b', 'c', 'd']) #string is not supported # can not chane hello or world
print(alpha) #('hello', 'world', ['H', 2, 3, 4, 5], ['a', 'b', 'c', 'd'])
alpha[3][3]=2
print(alpha) #('hello', 'world', ['H', 2, 3, 4, 5], ['a', 'b', 'c', 2])


alpha=1,1,2,2,2,2,3,3,4,4,5,5,2,2
print(alpha.count(2)) #result 6

alpha[2]=10
print(alpha) #will get error ; TypeError: 'tuple' object does not support item assignment








