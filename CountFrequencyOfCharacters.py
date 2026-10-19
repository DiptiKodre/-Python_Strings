name = "hello, how are you?"

#using dictinary
#TC: O(n)
#SC : O(k) where k is the number of unique characters in the string
freq = {}
for ch in name:
    freq[ch]= freq.get(ch,0)+1
print(freq)


#using counter from collections module
from collections import Counter
freq_counter = Counter(name)
print(freq_counter)

# ignore spaces
frequency ={}
for char in name:
    if char != " ":
        frequency[char]= frequency.get(char,0)+1
print(frequency)


#using dictinary comprehension
fr = {char:name.count(char) for char in name if char != ""}
print(fr)
