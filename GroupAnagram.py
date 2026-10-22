# We are given a list we need to group all anagrams present inside the list. 
# For example, we are having a list w = ["eat", "tea", "tan", "ate", "nat", "bat"] 
# we need to group all anagrams so that output should be 
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']].

# First approach: sort each word to create a shared key for its anagrams.
# Algorithm: sort each word's letters, group words by the sorted-letter key, then return the groups.
# TC: O(n * k log k), SC: O(n * k).
def groupAnagram(strs): 
    group = {}  #
    for word in strs:  # Process every word.
        key = "".join(sorted(word))  # Create a canonical key by sorting its letters.
        if key not in group:  # Create the group the first time this key appears.
            group[key] = []  # Initialize an empty anagram group.
        group[key].append(word)  # Add the word to its matching group.
    return list(group.values())  # Return all groups as a list.

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]  
print(groupAnagram(strs))  

# Dry run: aet -> [eat, tea, ate]; ant -> [tan, nat]; abt -> [bat].

# Second approach: use each word's character-frequency tuple as its grouping key.
# Algorithm: count each lowercase letter, group by the 26-count tuple, then return the groups.
# TC: O(n * (k + 26)), SC: O(n * (k + 26)).
from collections import defaultdict  # Import a dictionary that creates missing lists.

def group_anagram(strs):  
    groups = defaultdict(list)  # Map each frequency tuple to its word group.
    for word in strs:  # Process every word.
        count = [0] * 26  # Initialize the counts for lowercase English letters.
        for ch in word:  # Count each character in the word.
            count[ord(ch) - ord("a")] += 1  # Increment that letter's position.
        groups[tuple(count)].append(word)  # Group words with identical frequencies.
    return list(groups.values())  # Return all groups as a list.

print(group_anagram(strs))  

# Dry run: eat/tea/ate -> same counts; tan/nat -> same counts; bat -> its own counts.