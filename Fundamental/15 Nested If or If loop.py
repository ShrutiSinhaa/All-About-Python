Age = input("Enter your age:")
Age = int(Age)
# alternatively you can use : age = int(input("Enter your age:"))

if Age >= 16:
    print("eligible for driving")
    if Age >= 18:
        print("Eligible for voting")
        if Age >= 21:
            print("You are an eligible adult!!!!!!!!!!")

############################

#Enter your age:42
#eligible for driving
#Eligible for voting
#You are an eligible adult!!!!!!!!!!

#################################
#logic - logic would flow from 1st IF - in this case if age is more or equal to 16... again if its more than 16 and also more than 18 then more than 16, 18 and 21
