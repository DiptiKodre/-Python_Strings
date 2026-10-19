def nonReapeatingCharater(s):
    frequency = {}
    for ch in s:
        frequency[ch] = frequency.get(ch,0)+1
    for ch in s:
        if frequency[ch] == 1:
            return ch  #returns the first non-repeating character

s = "stress"
print(nonReapeatingCharater(s))