# Time Complexity: O(n^3), because there are O(n^2) substrings and each
# slice/print can process up to O(n) characters.
# Auxiliary Space Complexity: O(n), for the largest temporary substring.
# Printed output is not retained in memory.
str = "abc"  # Set the input string whose substrings will be generated.

for i in range(len(str)):  # Choose each character index as a substring's starting point.
    for j in range(i+1,len(str)+1):  # Try every valid end index after the start.
        print(str[i:j])  # Print the substring from index i up to, but not including, j.

# Dry run for str = "abc":
# i = 0: j = 1 -> str[0:1] = "a"
#       j = 2 -> str[0:2] = "ab"
#       j = 3 -> str[0:3] = "abc"
# i = 1: j = 2 -> str[1:2] = "b"
#       j = 3 -> str[1:3] = "bc"
# i = 2: j = 3 -> str[2:3] = "c"
# Output:
# a
# ab
# abc
# b
# bc
# c
