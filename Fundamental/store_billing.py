# item price dictionary
prices = {
    "apple": 20,
    "banana": 10,
    "milk": 50,
    "bread": 30,
    "eggs": 60
}

print("\nEnter quantity for each item\n")

total_bill = 0

for item, price in prices.items():

    qty = int(input("Enter quantity for " + item + ": "))
    cost = qty * price
    total_bill = total_bill + cost


    bill_entry = (item, qty, cost)   # tuple

    print(bill_entry[0], "-", bill_entry[1], ":", bill_entry[2])

print("\nTotal Bill:", total_bill)