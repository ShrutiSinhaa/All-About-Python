str = "good morning people and welcome to the session"
# lets split the words

print(str.split())
#['good', 'morning', 'people', 'and', 'welcome', 'to', 'the', 'session']

split = str.split()

split.sort()
print(split)
# print the words from the sentence in sorted order:
# ['and', 'good', 'morning', 'people', 'session', 'the', 'to', 'welcome']

#print as a sorted array

for words in split:
    print(words)
# and
# good
# morning
# people
# session
# the
# to
# welcome

