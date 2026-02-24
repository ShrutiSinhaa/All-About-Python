# if-elif VS if-else
# if-else - Used when there are only two possible outcomes.
# if- elif - else ; Used when there are multiple conditions to check.
# Yes  you can nest if-else instead of using elif... but that would make it complicated and untidy

#################    ELIF   ###############
marks = int(input("Enter total score: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

####################### IF- else nested ####################

marks = int(input("Enter total score: "))

if marks >= 90:
    print("Grade A")
else:
    if marks >= 75:
        print("Grade B")
    else:
        if marks >= 50:
            print("Grade C")
        else:
            print("Fail")

