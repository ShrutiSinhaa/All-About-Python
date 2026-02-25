import sys
from selectors import SelectSelector

print(sys.version)


# sys : that it can print all the errors or exceptions inside your program

x=['a','b',3,4,5,6,7,8,9,10]

for i in x:
    try:
        print("The list value is ",i)
        b=1/int(i)
        break

    except:
        print("oops error!!!", sys.exc_info())
        print("lets see next value in list")

print("the reciprocal of ",i,"is",b)

# The list value is  a
# oops error!!! (<class 'ValueError'>, ValueError("invalid literal for int() with base 10: 'a'"), <traceback object at 0x0000025924F29900>)
# lets see next value in list
# The list value is  b
# oops error!!! (<class 'ValueError'>, ValueError("invalid literal for int() with base 10: 'b'"), <traceback object at 0x0000025924F29900>)
# lets see next value in list
# The list value is  3
# the reciprocal of  3 is 0.3333333333333333