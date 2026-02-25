for x in range(1,11):
    if x == 5: ## skip 5 but print other numbers from 1 to 11
        continue
    print(x)

print("end")

############################################

for v in "Orange":
    if v == "O":  #would skip O to print
        continue
    else:
        print('Fruit') # after printing every letter it would print Fruit
    print(v)
print("end")

# Fruit
# r
# Fruit
# a
# Fruit
# n
# Fruit
# g
# Fruit
# e
# end

####################################

for v in "Orange":
    if v == "O":  #would skip O to print
        continue
    else:
        break # loop would be terminated # the end result would be "end" as the break would not let the loop continue
    print(v)
print("end")

