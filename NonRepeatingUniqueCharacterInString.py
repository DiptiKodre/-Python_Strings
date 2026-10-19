s = "level"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0)+1
for ch in s:
    if freq[ch] == 1:
        print(ch)
        break

#TC : O(n)
#SC : O(k) where k is the number of unique characters in the string