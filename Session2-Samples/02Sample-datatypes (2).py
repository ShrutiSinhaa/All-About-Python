# input() - input from user
# int() - integer input
# float() - Decimal number

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
status = input("are you already enrolled[True/false]: ")

status = status == "True"

print("\nStudent Card")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Enrolled", status)
