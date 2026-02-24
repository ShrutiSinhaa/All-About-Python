# String is a sequence of characters
# a variable is a name (or "container") that stores a value in memory,
# while a string is a specific type of data (a sequence of characters) that can be stored in a variable
#  A variable can store a string, but a string itself is the value, not the container.
#  string formatting operators
#  %c for character, %s for string conversion, %i for decimal integer, %d for signed integer,
#  %u for unsigned decimal integer, %o for octal integer, and %x for hexadecimal integer
# example script

name = "Sam"
print("Welcome %s to the Summit" % name)

# Welcome Same to the Summit
dob = 2004
year = 2026
age = year-dob
print(age)
# 22
print("%s was born in year %i that means he is %i years old" % (name, dob, age))

# Sam was born in year 2004 that means he is 22 years old

