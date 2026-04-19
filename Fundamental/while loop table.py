x = "y"

while x == "y":
    number = int(input("Enter a number: "))
    
    i = 1
    while i <= 10:
        if number * i == 50:
            i += 1
            continue

        
        print(number, "X", i, "=", number * i)
        i = i + 1

    x = input("Do you want to continue? (y/n): ").lower()

print("Loop ended")