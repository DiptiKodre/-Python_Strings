def count_consonants_vowels(s):
    consonants = 0
    vowels = 0
    vowel_set = set("aeiou")

    for ch in s.lower():
        if ch.isalpha():
            if ch in vowel_set:
                vowels += 1
            else:
                consonants += 1
    return consonants, vowels

s = "hello, how are you?"
print("Total consonants and vowels in the string:", count_consonants_vowels(s))

#TC: O(n)
#SC: O(1)


#using set
#TC: O(n)
#SC: O(1)
vowel_set = set("aeiou")
v = 0
c = 0
for ch in s.lower():
    if ch.isalpha():
        if ch in vowel_set:
            v += 1
        else:
            c += 1
print("Total vowels:", v)
print("Total consonants:", c)