#using split() and reverse()
s = "The sky is blue"
words =s.split()
words.reverse()
result = " ".join(words)
print(result)

#using slicing
rev = " ".join(s.split()[::-1])
print(rev)

#without reverse() or slicing
wordss = s.split()
resultt = " "
for word in wordss:
    resultt = word +" "+resultt
print(resultt.strip())