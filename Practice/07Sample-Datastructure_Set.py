# set is defined by {} But not key value / its defined as list in {} :)

# no duplicate values allowed // unindexed //  unordered

a = {1,2,3,4}
print(a)
a={1,1,2,2,3,3,4,4}
print(a)
a={1,2,3,4,3,5,2,6,1,2,3,4,5,6,7}
print(a) # unordered / unindexed means what order input was made is not considered by set
Names={"Rahul","Hannah"} #it can be string
print(Names)
mixed={"happy",25,"lucky",22.5,"Happy",22.5} #it can be mixed value
print(mixed)




#++++++++++++++++++++++++++++++++++++++++++++++
numbers={1,3,4,2,6,5,7,8,9}
print(numbers)
# add value
numbers.update([10,20,20,30,40,10,9,7])
print(numbers)
# remove value

numbers.difference_update([1,2,3])
print(numbers)

#loop
for x in numbers:
    print(x) #output sorted and listed

#lets sort a list using set

a=[1,2,3,4,2,3,5,6,7,45,65,2,55,45,43] # a is a list with duplicate value not sorted as well
uniq_list= set(a)

for i in uniq_list:
    print(i)
