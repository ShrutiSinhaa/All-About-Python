a = input("Enter a string that you want to split and sort:")

a = a.split()
print(a)
for word in a:
    print(word)
# Enter a string that you want to split and sort: hello world good morning
# ['hello', 'world', 'good', 'morning']
# hello
# world
# good
# morning

# RESULT - Enter a string that you want to split and sort: GOOD MORNING WORLD
# ['GOOD', 'MORNINNG', 'WORLD']

a.sort()
for word in a:
    print(word)
# split and sorted
# am
# for
# i
# is
# my
# name
# shruti,
# today
# trainer
# your

