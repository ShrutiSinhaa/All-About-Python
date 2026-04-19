status = input("Enter your employement status (Employed/Unemployed): ").lower()
if status == "employed":
    salary = float(input("Enter your salary: "))
    if salary > 50000:

        print("Approved")
    else:

        print("Rejected")

elif status == "unemployed":
    asset = float(input("Enter your total assets: "))
    if asset > 100000:
        print("Approved")
    else:
        print("Rejected")
else:
    print("Invalid input. Please enter 'Employed' or 'Unemployed'.")

