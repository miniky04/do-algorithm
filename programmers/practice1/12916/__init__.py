def solution(s):
    answer = True
    c1 = 0
    c2 = 0
    l = list(s.lower())
    for i in range(len(l)):
        if l[i] == 'y':
            c1 += 1
        elif l[i] == 'p':
            c2 += 1
        else:
            continue
    if c1 == c2:
        answer = True
    else:
        answer = False
    return answer


# def numPY(s):
#     # 함수를 완성하세요
#     return s.lower().count('p') == s.lower().count('y')


s2 = "Pyy"
print(solution(s2))