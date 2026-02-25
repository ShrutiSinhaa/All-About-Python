# A function is a block of reusable code that performs a specific task.
name = input("Enter your name: ")
def greeting(name):
    print("Hello " + name)

greeting(name)

###############   result  ###########

# Enter your name: ss
# Hello ss

############# lets add while loop
while True: ## would create a loop
    name = input("Enter your name: ")
    def greeting(name):
        print("Hello " + name)

    greeting(name)   # Before running the next section remove this section else it wont let the next section run. as this is an endless loop.

############ Loop wont end - lets add a break

while True: ## would create a loop
    name = input("Enter your name: ")
    def greeting(name):
        print("Hello " + name)

    greeting(name)
    ex = input("Do you wanna continue? (y/n): ")
    if ex != "y":
        break