
e = "yes"
while True: # this will create an infinite loop until we break it
    weather = input("Enter weather outside: (rainy / sunny / normal) : ").lower() # to convert the input to lowercase for easier comparison
    windy = input("Is it Windy (yes/no) : ").lower()
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
