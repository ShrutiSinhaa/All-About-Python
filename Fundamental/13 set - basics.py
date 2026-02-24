# set is ordered. means is I define set as {3,4,5,6,0,1,2,3} - but when It prints as 0,1,2,3,4,5,6
# set do not support duplication. that means if set is defined as {1,1,1,2,3,4,4,4} the print is 1,2,3,4
# set do not support list inside . means you can not define a set as {1,2,3,[1,2,3,4]}
# it is defined using {}


a={}
print(type(a)) #<class 'dict'>
############### To create empty set ##############
a=set()
print(type(a))  #<class 'set'>
a.update([1,2,3,4])
print(a)  ##{1, 2, 3, 4}
################# other type of set ###########################
b={1,2,3,4,5,6,7,8,9}
c={1.0,"hello","world",4.19,'a'}
print(c) #{1.0, 'a', 'hello', 4.19, 'world'}
print(a)
b.update([11,12,13])
print(b) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13}
c.add(6)
print(c) #{'a', 'hello', 4.19, 6, 'world'}
c.remove(4.19)
print(c) #{1.0, 'hello', 'world', 6, 'a'}
c.discard(1.0)
print(c) #{'a', 'hello', 'world', 6}
c.discard(4.19)
print(c) #{'a', 'hello', 'world', 6}
############# remove vs discard ##################
# remove would throw error and stop proceeding if the element not found in set.
#discard would show the same set and ignore the error


################################ use of operator ############################
a1={1,2,3,4,5,6,7,8,9}
a2={5,3,4,6,7,8,9,10}
print(a1) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(a2) #{3, 4, 5, 6, 7, 8, 9, 10}
a3=a1-a2
print(a3) #{1, 2}
a4=a2-a1
print(a4) #{10}

#######################
a1={1,2,3,4,5,6,7,8,9}
a2={5,3,4,6,7,8,9,10}

a3=a1 | a2 # or operator - will add both sets
print(a3) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a4= a1 & a2 # and operator - only common elements
print(a4) # {3, 4, 5, 6, 7, 8, 9}



