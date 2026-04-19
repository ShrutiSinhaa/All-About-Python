weather = "rain"
if weather == "rain":
    print("Take an umbrella !!")

######################################

weather = "Sunny"
if weather == "rain":
    print("Take an umbrella !!")
else:
    print("Hurray!! go out have fun")


##########################################

weather = "sunny"
if weather == "rain":
    print("Take an umbrella !!")   # first it would check it is raining... which is not true
elif weather == "sunny":            # then it would ccheck the second condition.... this is true
    print("Take an umbrella its Sunny out there!!")
else:                               # In case second condition also not met it would go for next statement.
    print("Hurray!! go out have fun")


#####################
# what if its raining and also windy

weather = input("Enter weather outside: (rainy / sunny / normal) : ")
windy = input("Is it Windy (yes/no) : ")



if weather == "rainy": #after first condition is met it would check the next if-else condition. other wise skip it
                        # this is the main difference in nested if-else and elif. Elif would move to second condition
                        #if first is not met. while nested would move to second condition if first is met.
    if windy == "yes":
        print("Umbrella is not safe take Rain Coat !!")
    else:
        print("Umbrella is safe take one with you !!")
elif weather == "sunny":
    print("Take an umbrella its Sunny out there!!")
else:
    print("Hurray!! go out have fun")

