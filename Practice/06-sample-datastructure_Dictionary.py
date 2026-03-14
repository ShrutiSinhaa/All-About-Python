# Mathematical processing

Student = {
    "name":"Patrice",
    "Grade":7,
    "Maths":75,
    "Science":98,
    "English":55
}

# add more value
Student["Social Study"] = 65
Student["Art"] = 25
print(Student)


total_marks = Student["Maths"] + Student["English"]+ Student["Science"]+ Student["Social Study"] + Student["Art"]
percetage = total_marks*(1/5)
print("\nreport card")
print("============================")
print("Name:",Student["name"])
print("Grade:",Student["Grade"])
print("Maths:",Student["Maths"])
print("Science:",Student["Science"])
print("English:",Student["English"])
print("Social Study: ",Student["Social Study"])
print("Art:",Student["Art"])
print("============================")

print("\nTotal",total_marks)
print("Percentage %",percetage)


# remove value
Student.pop("Social Study")
print(Student)

# loop

for key, value in Student.items():
    print(key,":", value)

total = 0
for key, value in Student.items():
    if isinstance(value, int):
        total += value
    print (total)




