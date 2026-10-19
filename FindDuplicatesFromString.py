#using dictionary
#Tc : O(n)
#sc : O(n)
s = "programming"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0)+1
for ch in s:
    if freq[ch]>1:
        print(ch)


#USING SET
#TC : O(n)
#SC : O(n)

str = "programming"
seen = set()
duplicates = set()

for ch in str:
    if ch in seen:
        duplicates.add(ch)
    else:
        seen.add(ch)
print(duplicates)

#if we want duplicates in original order
#TC : O(n)
#SC : O(n)

saw = set()
repeated = []
for ch in str:
    if ch in saw and ch not in repeated:
        repeated.append(ch)
    else:
        saw.add(ch)

print(repeated)
print(type(repeated))
print(type(saw))