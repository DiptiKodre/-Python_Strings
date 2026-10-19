# TC = o(n)
# SC = O(1)

str = " Hello How are You? Are You Doing WELL???"

upper_count = 0
lower_count = 0

for ch in str:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1

print("Total uppercase letters : " ,upper_count)
print("Total Lowercase Letters : ", lower_count)