# Report Card Generator

# Input student details
name = input("Enter Name: ")
class_ = input("Enter Class: ")
roll_no = input("Enter Roll No: ")

# Input marks
math = float(input("Enter Mathematics marks (out of 100): "))
english = float(input("Enter English marks (out of 100): "))
social = float(input("Enter Social marks (out of 100): "))
science = float(input("Enter Science marks (out of 100): "))
computers = float(input("Enter Computers marks (out of 100): "))

# Calculate total and percentage
total = math + english + social + science + computers
percentage = (total / 500) * 100

# Determine grade and result
if percentage >= 90:
    grade = 'A'
    result = 'Pass'
elif percentage >= 70:
    grade = 'B'
    result = 'Pass'
elif percentage >= 60:
    grade = 'C'
    result = 'Pass'
elif percentage >= 40:
    grade = 'Pass'
    result = 'Pass'
else:
    grade = 'Fail'
    result = 'Fail'

# Print report card
print("--------------Report Card-----------")
print(f"Name: {name}")
print(f"Class: {class_}")
print(f"Roll no: {roll_no}")
print("===========================")
print(f"Mathematics : {math}")
print(f"English     : {english}")
print(f"Social      : {social}")
print(f"Science     : {science}")
print(f"Computers   : {computers}")
print("============================")
print(f"Total : {total}")
print(f"Percentile : {percentage:.2f}%")
print(f"Grade : {grade}")
print(f"Result : {result}")