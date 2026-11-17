# TC = O(n)
# SC = O(1)
def validPalindrome(s):
    n  = len(s)
    left = 0
    right = n-1

    while left < right:
        # Skip non-alphanumeric characters from the left
        if not s[left].isalnum():
            left += 1
            continue

        # Skip non-alphanumeric characters from the right
        if not s[right].isalnum():
            right -= 1
            continue
        
        # Compare characters in a case-insensitive manner
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

s = "A man, a plan, a canal: Panama"
print(validPalindrome(s))


# Dry run for "A man, a plan, a canal: Panama":
# Matching index pairs (after skipping non-alphanumeric characters):
# (0, 29): A/a, (2, 28): m/m, (3, 27): a/a, (4, 26): n/n,
# (7, 25): a/a, (9, 24): p/P, (10, 21): l/l, (11, 20): a/a,
# (12, 19): n/n, (15, 18): a/a. All pairs match, so the result is True.