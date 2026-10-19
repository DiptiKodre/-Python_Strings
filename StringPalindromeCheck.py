str = "madam"


# TC = O(N/2)= O(N)
#SC = O(1)
def palindromeString(str):
    n = len(str)
    left = 0
    right = n-1
    
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True

print(palindromeString(str))

# Using recursion
#TC =  O(N/2)= O(N)
#SC = O(N/2) --> stack space

def palindromeCheck(str, left, right): 
    if left >= right:
        return True

    if str[left] != str[right]:
        return False

    return palindromeCheck(str,left+1, right-1)

result = palindromeCheck(str,0,len(str)-1)
if result:
    print("Palindrome")
else:
    print("Not a palindrome")


#using string slicing
#TC = O(n)
#SC = O(n)
if str == str[:: -1]:
    print("Palindrome string")
else:
    print("Not a palindrome string")


# using loop
#TC = O(N^2) --> each string concatenation can create a new string
#SC = O(N)
rev = ""
for ch in str:
    rev = ch+rev
if str == rev:
    print("Plaindrome")
else:
    print("Not a Palindrome")