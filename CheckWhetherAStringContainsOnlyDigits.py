# Using isdigit()( Simplest Approach)
#TC = o(n)
#SC = o(1)

str = "12345"

if str.isdigit():
    print("String Contains Only Digits")
else:
    print("String does not contain only digit")

# Using Loop (interview approach)
#TC = o(n)
#SC = o(1)
is_digit = True
if len(str) == 0:
    is_digit = False
else:
    for ch in str:
        if ch < '0' or ch > '9':
            is_digit = False
            break
if is_digit:
    print("String contains only digits")
else:
    print("String does not contains digits") 