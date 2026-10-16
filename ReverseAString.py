str = "hello, how are you?"
 
#using for loop
#TC : O(n)
#SC : O(n)
rev = "" 
for ch in str:
    rev = ch + rev
print(rev)

#using slicing
#tc: O(n)
#sc: O(n)
reverse = str[::-1] 
print(reverse)

#using reversed() function
#tc: O(n)
#sc: O(n)
reverse = "".join(reversed(str))
print(reverse)

#using two pointer approach
#TC: O(n)
#SC: O(n)
s = list(str)
left = 0
right = len(s)-1
while left <right:
    s[left],s[right] = s[right],s[left]
    left += 1
    right -= 1
print("".join(s))