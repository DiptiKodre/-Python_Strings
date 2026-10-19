#TC = O(n*m)
#AC = O(1)

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return " "
    result = ""
    base = strs[0]
    for i in range(0,len(base)):  #Loops through every character index of the first string.
        for word in strs[1: ]:    # Loops through all strings except the first one.
            if i==len(word) or word[i]!= base[i]:    # Stops and returns the current prefix if: i == len(word): the current word is too short.
                                                      #word[i] != base[i]: characters do not match
                return result    
        result += base[i]      #Adds the matching character to result.
    return result

strs = ["flower","flow","flowers"]
print(longestCommonPrefix(strs))
