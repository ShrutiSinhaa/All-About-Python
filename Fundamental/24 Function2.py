
def f(x):
    return 2*x
print("double is", f(7)) #double is 14

##########################################
def f(x):
    return 2*x
x=int(input("Enter a number: "))
print("double is", f(x))
# Enter a number: 6
# double is 12

##########################################

def intro(name,msg = "Hello World!"):
    print("My name is ",name, msg)

intro("XYZ") ## My name is  XYZ Hello World!
################################
def intro(name,msg):
    print("My name is ",name, msg)

name = input("Enter your name: ")
msg = input("Enter your message: ")
intro(name,msg)

# Enter your name: shruti
# Enter your message: Good Morning
# My name is  shruti Good Morning

##########################################

def intro(*name):
    for i in name:
        print("My name is ",i)

intro("shruti","Dev","Bip")

# My name is  shruti
# My name is  Dev
# My name is  Bip

#################################### to combine more than one value we can use list

def intro(names,roles):
    for i,j in zip(names,roles): # to combine two list we are using - zip
        print("My name is ",i," and my role is ",j)

names=["shruti","bipeen"]
roles=["TDM","GDM"]
intro(names,roles)

############
# My name is  shruti  and my role is  TDM
# My name is  bipeen  and my role is  GDM


