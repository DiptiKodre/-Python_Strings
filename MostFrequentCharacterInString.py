# Time Complexity: O(n + k),= O(n) where n is the string length and k is the number of distinct characters
# Space Complexity: O(k) for the frequency dictionary
str = "programming" 

freq = {}  # Dictionary to store each character and its count

for ch in str:  
    freq[ch] = freq.get(ch, 0) + 1  # Increase its count, starting from zero
max_char = max(freq, key=freq.get)  # Select the character with the highest count

print("Most frequent character is : ", max_char)  # Display the most frequent character
print("frequency : ", freq[max_char])  # Display how many times it occurs

# Dry run for "programming":
# Read p: {'p': 1}
# Read r: {'p': 1, 'r': 1}
# Read o: {'p': 1, 'r': 1, 'o': 1}
# Read g: {'p': 1, 'r': 1, 'o': 1, 'g': 1}
# Read r: {'p': 1, 'r': 2, 'o': 1, 'g': 1}
# Read a: {'p': 1, 'r': 2, 'o': 1, 'g': 1, 'a': 1}
# Read m: {'p': 1, 'r': 2, 'o': 1, 'g': 1, 'a': 1, 'm': 1}
# Read m: {'p': 1, 'r': 2, 'o': 1, 'g': 1, 'a': 1, 'm': 2}
# Read i: {'p': 1, 'r': 2, 'o': 1, 'g': 1, 'a': 1, 'm': 2, 'i': 1}
# Read n: {'p': 1, 'r': 2, 'o': 1, 'g': 1, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
# Read g: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
# The highest count is 2. Since r, g, and m tie, max() returns r (the first tied key).
# Output: Most frequent character is : r
# Output: frequency : 2