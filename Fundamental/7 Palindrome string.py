# Palindrome strings =remains same from LTR or RTL
# example ABCBA or Abcba //it ignores case
####################################
str = "abcba"
print(str)
a = reversed(str)
print(a)
b=list(str)
print(b) #['a', 'b', 'c', 'b', 'a']

if list(str) == list(a):
    print("reversed")
else:
    print("not reversed") #reversed//


################################

a = "hello"
b = list(a)
c = list(reversed(a))
print(a)
print(b)
print (c)
# hello
# ['h', 'e', 'l', 'l', 'o']
# ['o', 'l', 'l', 'e', 'h']

if b==c:
    print("is palindrome")
else:
    print("not palindrome")

    #not palindrome

######################
# lets see case sensitive string

a = "Level" #is this Palindrome ?
b = list(reversed(a))

if list(a)==b:
    print("palindrome")
else:
    print("not palindrome") #result is  // not palindrome ///

# to ignore the case we can add following:
a = "Level"
a = a.casefold()
b = list(reversed(a))
if list(a)==b:
    print("palindrome")
else:
    print("not palindrome") #as the case is ignored now the result is //   Palindrome //

