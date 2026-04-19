x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))

result = (x / y) * y

print("Actual result:", result)
print("Rounded result:", round(result, 2))

if round(result, 2) == x:
    print("Equal to original number after rounding")
else:
    print("Not equal")