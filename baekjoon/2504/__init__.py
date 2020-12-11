n = input()
l = []
s = 0
c = True
for i in n:
    if i == '(' or i == '[':
        l.append(i)
    elif i == ')':
        if len(l) > 0 and l[-1] == '(':
            del l[-1]
            s = s + 2
        else:
            print(0)
            c = False
            break
    elif i == ']':
        if len(l) > 0 and l[-1] == '[':
            del l[-1]
            s = s + 3
        else:
            print(0)
            c = False
            break

print(s)