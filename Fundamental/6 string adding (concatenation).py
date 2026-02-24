a = "Hello"
b = "World"

# Concatenating is called when you want to add to string

c=a + b
print(c) # HelloWorld

d = a * 2
print(d) #HelloHello

e = a + " " + b
print(e) # added space in between - Hello World

f = (a + " " + b).split()
print(f) #['Hello', 'World']
print(list(c))  # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
