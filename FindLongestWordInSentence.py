# TC = O(n)
# SC =  O(n)

# split() --> divides sentence into words

str = "Python is a powerful programming language"

words = str.split()
longest =""

for word in words:
    if len(word)> len(longest):
        longest = word
print("Longest word : ",longest)
print("length of ;longest word is : ",len(longest))