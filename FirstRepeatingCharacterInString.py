
# USING SET (OPTIMAL SOLUTION)
# Time Complexity = O(n)  
# Space Complexity = O(n) 
str = "programming"      
seen = set()

for ch in str:           
    if ch in seen:        # If the character was seen before, it's the first repeating character
        print("First repeating character : ", ch) 
        break            
    seen.add(ch)          # Add the current character to the set if it is new

else:                     # This runs only if the loop completes without breaking
    print("No repeating character found") 



# WITHOUT USING SET
# Time Complexity = O(N^2)  # For each character, we compare against all later characters
# Space Complexity = O(1)    # No extra data structure is used

s = "programming"        

for i in range(len(s)):  
    for j in range(i+1, len(s)):  # Compare with every next character
        if s[i] == s[j]:          
            print("First repeating character : ", s[i]) 
            break                 # Stop checking for this i value
    else:                     # If characters do not match, continue searching later
        continue              # Move to the next j value
    break                     # Stops the outer loop after finding the first repeating character
else:                         # prints the msg only if outer loop finishes without a break
    print("No repeating character found")  
