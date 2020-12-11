stack = []
stack2 = []
c = 1
t = True

for i in range(int(input())):
    n = int(input())
    while c <= n:
        stack.append(c)
        stack2.append('+')
        c += 1
    if n == stack[-1]:
        stack.pop()
        stack2.append('-')
    else:
        t = False
        break

if not t:
    print('NO')
else:
    for i in stack2:
        print(i)