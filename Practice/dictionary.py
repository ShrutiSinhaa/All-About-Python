price={"apple":10,"bread":15,}
print(price["apple"])
purchase = int(input("enter the quantity  :"))
print("total cost = ",price["apple"]*purchase)


price["Milk"] = 35
print(price)
price.update({
    "water":30,
    "fish":180,
    "Chicken": 150,
    "apple":15
})
print(price)