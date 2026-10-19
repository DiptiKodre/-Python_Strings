# TC = O(n)
# SC = O(N)

str = "Hi hello how are you doing?"
words = str.split()
count = 0

for word in words:
    count += 1
print("Total number of words in given string : ",count)

print("total words : ", len(words))  #len(str.split())