# String compression in Python usually refers to Run-Length Encoding (RLE), 
# where consecutive repeating characters are replaced by the character
#  followed by its count (e.g., "aaabcc" becomes "a3b1c2")


# First approach: scan the string and count each consecutive run.
# Algorithm: count matching adjacent characters, then append the character and its count.
# TC: O(n^2), SC: O(n).
def stringCompression(s):  # Compress consecutive repeated characters in s.
    result = ""  # Store the compressed output.
    count = 1  # Count the current character run.

    for i in range(1, len(s)):  # Start at the second character.
        if s[i] == s[i - 1]:  # Check whether the current run continues.
            count += 1  # Increase the run length.
        else:  # Finish the run when the character changes.
            result += s[i - 1]  # Append the run's character.
            if count > 1:  # Add a count only for repeated characters.
                result += str(count)  # Append the run length.
            count = 1  # Start counting the new run.
    result += s[-1]  # Append the character in the final run.

    if count > 1:  # Check whether the final run repeats.
        result += str(count)  # Append the final run length.
    return result  # Return the compressed string.

s = "abbbaaaaaaccdaaab"  # Set the sample input.
print(stringCompression(s))  # Compress and print the sample.

# Dry run: a | bbb | aaaaaa | cc | d | aaa | b -> ab3a6c2da3b

# Second approach: use itertools.groupby to collect consecutive character runs.
# Algorithm: get each run, count its characters, and append the character and count.
# TC: O(n^2), SC: O(n).
from itertools import groupby  # Import the consecutive-grouping helper.

def compressString(s):  # Compress s by processing consecutive groups.
    result = ""  # Store the compressed output.
    for char, group in groupby(s):  # Get each character and its consecutive group.
        count = len(list(group))  # Count the characters in the current group.
        if count == 1:  # Keep single characters without a count.
            result += char  # Append the character.
        else:  # Include the count for repeated characters.
            result += char + str(count)  # Append the character and run length.
    return result  # Return the compressed string.

print(compressString(s))  # Compress and print the sample using groupby.

# Dry run: a(1), b(3), a(6), c(2), d(1), a(3), b(1) -> ab3a6c2da3b
