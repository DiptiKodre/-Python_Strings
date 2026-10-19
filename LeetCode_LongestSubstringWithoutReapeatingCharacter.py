#Brute force solution using set
#TC: O(n^2)
#SC: O(n)
s ="CADBZABCD"
def lengthOfLongestSubstring(s):
    maxi = 0
    n = len(s)
    for i in range(0,n):
        myset = set()
        for j in range(i,n):
            if s[j] in myset:
                break
            else:
                maxi = max(maxi, j-i+1)
                myset.add(s[j])
    return maxi

print(lengthOfLongestSubstring(s))


########################################################

# Optimal solution using sliding window technique AND  dictionary
#TC: O(n)
#SC: O(n)

def lengthOfLongestSubstringUsingDictionary(s):
    n = len(s)
    maxi = 0
    left = 0
    right = 0
    maxi = 0

    mydict = {}    #Creates an empty dictionary.It stores each character and its latest index in the string.
    while right < n:   #Checks whether the current character has already appeared before.
        if s[right] in mydict:    #If yes, we need to move the left pointer forward so that duplicates are excluded.
            left = max(left, mydict[s[right]]+1)     #If the character is repeated, this updates left to the position just after the previous occurrence.max(...) is used so left never moves backward.
        maxi = max(maxi, right-left+1)     #Computes the length of the current window:right - left + 1 Updates maxi with the largest window length seen so far.
        mydict[s[right]] = right   #Stores the current index of the character in the dictionary.This updates the latest seen position of the character.
        right +=1   #Moves the right pointer forward to expand the window.
    return maxi


print(lengthOfLongestSubstringUsingDictionary(s))