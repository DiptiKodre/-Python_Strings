#Brute force
#TC : O(n^2)
#SC : O(n)
def remove_duplicates(str,result):
    for ch in str:
        if ch not in result:
            result += ch
    return result

print(remove_duplicates("hello", ""))

#USING SET
#TC : O(n)
#SC : O(n)

s = "programming"
seen = set()
result = "" 
for ch in s:
    if ch not in seen:
        seen.add(ch)
        result += ch

print(result)

#Using dictionary
#TC : O(n)
#SC : O(n)

str = "programming"
res = " ".join(dict.fromkeys(str))
print(res)