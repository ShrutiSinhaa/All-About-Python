# while - execute statement as long as the condition is true


while True:

    x=int(input("enter the score"))

    if x>=50:
        print("You are an eligible")

    elif x>=30:
            print("you are behind 20 more points")

    else:
        print("Try again")



    z= input("press y for another chance or q for quit") # this is deciding factor for "while" loop. this should stay inside loop
    if z != "y":
        break
print("Program ended")



