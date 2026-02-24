# its collectionn of elements that is unordered and changable.
# elements are defined as key value example :

mydictionary = {}
print(mydictionary)

Mydictionary = {'a':1,'b':2,'c':3}
print(Mydictionary) # {3, 4, 5, 6, 7, 8, 9}

Mydictionary = {'Name':'Shruti','Age':18}
print(Mydictionary) # {'Name': 'Shruti', 'Age': 18}
print(type(Mydictionary)) # <class 'dict'>

print(Mydictionary['Name']) #Shruti
print(Mydictionary['Age']) #18

####################### Change / update Value ######################

newdictionary = {'Name':'Shruti','Gender':'Female','DOB':'1 Mar'}
print(newdictionary)
print(type(newdictionary))
print(f"{newdictionary['Name']} {newdictionary['Gender']} {newdictionary['DOB']}") ## using f string to combine multiple key
## Result     :     Shruti Female 1 Mar

print("My name is %s" % (newdictionary['Name'])) ## My name is Shruti

Mydictionary = {'Name':'Shruti','Age':18}
Mydictionary['Name']="Michael"
print(Mydictionary) # {'Name': 'Michael', 'Age': 18}
print(type(Mydictionary)) # <class 'dict'>

print("My name is %s" % (Mydictionary['Name'])) ## Mydictionary = {'Name':'Shruti','Age':18}
########### add More value ################
Mydictionary['Location']="Singapore"
print(Mydictionary) ##  {'Name': 'Michael', 'Age': 18, 'Location': 'Singapore'}



################### Delete or pop from dictionary #################

print(Mydictionary)   # {'Name': 'Michael', 'Age': 18, 'Location': 'Singapore'}

print(Mydictionary.pop('Age')) #18
print(Mydictionary) # {'Name': 'Michael', 'Location': 'Singapore'}
print(Mydictionary.popitem()) # ('Location', 'Singapore') #Removes the last inserted key-value pair
print(Mydictionary) # {'Name': 'Michael'}


a={1:'a',2:'b',3:'c'}
print(a)
print(a.popitem()) #Removes the last inserted key-value pair
print(a)  #{1: 'a', 2: 'b'}

del a[2]
print(a) #{1: 'a'}
del a #DELETE THE DICTIONARY a


a={1:'a',2:'b',3:'c'}
print(a) #{1: 'a', 2: 'b', 3: 'c'}
a.clear()
print(a) #{}

a[1]='a'
a[2]='b'
print(a) #{1: 'a', 2: 'b'}
a['welcome']="Hello"
print(a) #{1: 'a', 2: 'b', 'welcome': 'Hello'}

############################## Basic Operations ###########################

test={1:'a',2:'b',3:'c',4:'d',5:'e'}
print(len(test)) ##it would show the length - that is 5 in this dictionary
print(test.keys()) ## only keys---   dict_keys([1, 2, 3, 4, 5])
print(test.values()) ## only values ----   dict_values(['a', 'b', 'c', 'd', 'e'])
print(test.items()) ## dict_items([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')])
print(sorted(test)) ## sort keys - [1, 2, 3, 4, 5]
print(sorted(test.keys()))
print(sorted(test.values()))
print(sorted(test.items()))
############## for loop ################
for j in test:
    print(test[j])
#a
#b
#c
#d
#e
for key, value in test.items():
    print(key, value)
# 1 a
#2 b
#3 c
#4 d
#5 e

#

