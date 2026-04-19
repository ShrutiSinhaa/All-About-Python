# users select the items from the list
# a bill should be generated

# define a dictionary for item prices [key:value]

Prices={"apple":10,"banana":7,"egg":5,"bread":50,"milk":25}
cart={}

# take input from cashier / Buyer

for item in Prices:
    qty=int(input("Enter the quantity of " + item + ":"))
    cart[item]=qty

print("\n++++++ Reciept ++++++\n")
total=0
for item in Prices:
    qty=cart[item]
    cost=qty*Prices[item]
    print(item,"-",qty,"=",cost)
    total+=cost
print("\n+++++++++++++++++++++++")
print("\nTotal: ",total)
