for i in range(int(input())):
    l = []
    vps = input()
    c = True
    for j in vps:
        if j == '(':
            l.append(j)
        elif j == ')':
            if len(l) > 0:
                del l[0]
            elif len(l) == 0:
                print('NO')
                c = False
                break
    if c:
        if len(l) > 0:
            print('NO')
        else:
            print('YES')