# A string is said to be a rotation of another if it can be
# obtained by shifting some leading characters of the original
# string to its end without changing the order of characters.

str = "abcde"  # Store the original string to check.
goal = "cdeab"  # Store the string that may be a rotation of the original.

# Brute-force logic: rotate the string one position at a time and compare with goal.
# TC: O(N^2), SC: O(N).
def checkStringRotation(str, goal): 
    if len(str) != len(goal): 
        return False
    curr_str = str 
    n = len(curr_str) 

    for i in range(0,n):  # Check the original and each of the next N - 1 right shifts.
        if curr_str == goal: 
            return True 
        curr_str = curr_str[-1] + curr_str[:-1]  # Move the last character to the front.
    return False  


print(checkStringRotation(str,goal))  # Run the brute-force check and display its result.


# Optimized logic: every rotation appears as a substring in the string joined to itself.
# TC: O(N) average, SC: O(N).

def chcekStringRotaionOptimize(str,goal): 
    if len(str) != len(goal): 
        return False 
    double_str = str+str  # Concatenate the string with itself to contain all rotations.
    if goal in double_str:  
        return True
    return False 
