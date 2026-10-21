s1 ="anagram"
s2 ="nagaram"


#Brute force approach
# TC = O(nlogn)
# SC = O(n)
def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(isAnagram(s1, s2)) 

#Optimal approach
# TC = O(n)
# SC = O(1)

def isValidAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    frequency = {}
    for ch in s1:
        frequency[ch]= frequency.get(ch,0)+1
    for ch in s2:
        if ch not in frequency:
            return False
        else:
            
            if frequency[ch]==0:
                return False
            else:
                frequency[ch]-=1
    return True

print(isValidAnagram(s1, s2))
        