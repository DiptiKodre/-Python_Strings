s1 = "anagram"
s2 = "nagaram"

def isValidAnagram(s1,s2):
    if len(s1)!= len(s2):
        return False

    frequency = {}
    for ch in s1:
        frequency[ch] = frequency.get(ch,0)+1
    for ch in s2:
        if ch not in frequency:
            return False
        else:
            if frequency[ch] == 0:
                return False
            else:
                frequency[ch]-=1
    return True

print(isValidAnagram(s1,s2))