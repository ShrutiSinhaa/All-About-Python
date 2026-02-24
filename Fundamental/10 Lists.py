# list is collection of elements that is ordered, changeable and allows duplicate items
# you can have integer, string , another list , decimal number or even blank in a list

##################### DEFINE LIST  ########################

a=[]
a1 = [1,2,3,4,5]
a2 = ["date","of", "birth", "is", 26 ]

print(a2[0]) ##result = date
print(a2[1][1]) ## RESULT = f  // first "1" is "of" another "1" is "f" from 'of'
print(a2[2][3]) ## RESULT = t  // first "2" is "birth" another "3" is "t" from 'birth'
print(a2[2][1:4]) # RESULT = irt

a3=["hello",[1,2,3,4,5],["date","of", "birth", "is", 26]]
print(a3[0]) ## result is hello
print(a3[1][1]) ## result is 2
print(a3[2][3]) ## result = is


