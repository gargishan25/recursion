a = 0
b = 0
c = 0
inp = "([)]"
list = []
for i in inp:
    if i == "{":
        a +=1

    elif i == "(":
        b+=1
    elif i == "[":
        c+=1
    if i == "}":
        a -=1
    elif i == ")":
        b-=1
    elif i == "]":
        c-=1
if a == 0 and b == 0 and c == 0:
    print("These are balanced parentheses.")
else:
    print("These are not balanced parentheses.")