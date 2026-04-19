status = input("is borrower employed:yes/no: ")
score = int(input("Enter your credit score: ")) 
if status == "yes":
    age = int(input("Enter your age: "))
    if age > 45:
        print("Approved loan = 500,000")
    elif age < 45:
        if score > 9:
            print("Approved loan = 1,000,000")
        elif score > 7:
            print("Approved loan = 500,000")
        else:
            print("Rejected")
elif status == "no":
    asset = float(input("Enter your total assets: "))
    if asset > 100000 and score > 7:
        print("Approved loan = 800,000")
    else:
        print("Rejected")
else:
    print("Rejected")